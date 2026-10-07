"""Overnight DeepTutor deep-research runner with quota-aware retries."""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

OUT = Path(r"C:\Workspace\Amsham\research\overnight")
EXE = r"C:\Users\Shai\AppData\Local\hermes\hermes-agent\venv\Scripts\deeptutor.exe"
WORKSPACE = r"C:\Users\Shai"  # where the ChatGPT (Codex) login lives
PROMPT = (OUT / "prompt.txt").read_text(encoding="utf-8")
# manual_subtopics <= 3 makes DeepTutor research one section at a time (series), which avoids
# the ChatGPT burst rate limit; the confirmed outline still supplies all sections.
BASE_CFG = {"mode": "report", "depth": "manual", "manual_subtopics": 3, "manual_max_iterations": 5}
MAX_ATTEMPTS = 8
WAIT_ON_QUOTA_S = 30 * 60
QUOTA_MARK = "quota exceeded"


def log(msg):
    line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(OUT / "status.log", "a", encoding="utf-8") as f:
        f.write(line + "\n")


def run(cfg, out_name):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    with open(OUT / out_name, "w", encoding="utf-8") as fo, open(OUT / "deeptutor_stderr.log", "a", encoding="utf-8") as fe:
        subprocess.run(
            [EXE, "run", "deep_research", PROMPT, "-t", "paper_search", "-t", "web_search",
             "--config-json", json.dumps(cfg), "-f", "json"],
            cwd=WORKSPACE, stdout=fo, stderr=fe, env=env,
        )
    events = []
    for line in (OUT / out_name).read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("{"):
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return events


def result_of(events):
    res = [e for e in events if e.get("type") == "result"]
    errs = [e for e in events if e.get("type") == "error"]
    return (res[-1]["metadata"] if res else None), errs


def quota_hit(meta, errs, events):
    text = json.dumps(meta or {}) + json.dumps(errs)
    return QUOTA_MARK in text.lower()


def with_retries(cfg, out_name, label):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        log(f"{label}: attempt {attempt}")
        events = run(cfg, out_name)
        meta, errs = result_of(events)
        if quota_hit(meta, errs, events):
            log(f"{label}: ChatGPT quota hit, waiting {WAIT_ON_QUOTA_S // 60} min")
            time.sleep(WAIT_ON_QUOTA_S)
            continue
        if errs and not meta:
            log(f"{label}: error: {errs[-1].get('content')!s:.300}")
            time.sleep(120)
            continue
        return meta, events
    return None, []


def main():
    log("=== overnight run started ===")
    outline_file = OUT / "outline.json"
    if outline_file.exists():
        outline = json.loads(outline_file.read_text(encoding="utf-8"))
    else:
        meta, _ = with_retries(BASE_CFG, "outline_output.jsonl", "outline")
        if not meta or not meta.get("sub_topics"):
            log("FAILED: no outline produced")
            sys.exit(2)
        outline = [{"title": s["title"], "overview": s.get("overview", "")} for s in meta["sub_topics"]]
        outline_file.write_text(json.dumps(outline, indent=1, ensure_ascii=False), encoding="utf-8")
    log(f"outline: {len(outline)} sections: " + " | ".join(s["title"] for s in outline))

    cfg = dict(BASE_CFG, confirmed_outline=outline)
    meta, events = with_retries(cfg, "full_output.jsonl", "full research")
    report = (meta or {}).get("response", "")
    if not report or QUOTA_MARK in report.lower():
        log("FAILED: no clean report after all attempts")
        sys.exit(3)
    (OUT / "NeuroChain_deep_research_report.md").write_text(report, encoding="utf-8")
    n_tools = sum(1 for e in events if e.get("type") == "tool_call")
    log(f"DONE: report {len(report)} chars, {n_tools} search calls")


if __name__ == "__main__":
    main()
