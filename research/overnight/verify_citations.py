"""Check every arXiv citation in the DeepTutor report against the real arXiv record."""
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

OUT = Path(r"C:\Workspace\Amsham\research\overnight")
report = (OUT / sys.argv[1] if len(sys.argv) > 1 else OUT / "NeuroChain_deep_research_report.md").read_text(encoding="utf-8")

ids = sorted(set(re.findall(r"arxiv(?:\.org/(?:abs|pdf)/|:\s?)(\d{4}\.\d{4,5})", report, flags=re.I)))
NS = {"a": "http://www.w3.org/2005/Atom"}
rows = []
for i in range(0, len(ids), 20):
    batch = ids[i:i + 20]
    url = "https://export.arxiv.org/api/query?max_results=50&id_list=" + ",".join(batch)
    for wait in (0, 10, 30, 60, 120):
        time.sleep(wait)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "citation-check/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                root = ET.fromstring(r.read())
            break
        except Exception as exc:
            print(f"arXiv retry after error: {exc}")
    else:
        raise SystemExit("arXiv API unavailable")
    found = {}
    for entry in root.findall("a:entry", NS):
        eid = entry.findtext("a:id", default="", namespaces=NS)
        m = re.search(r"(\d{4}\.\d{4,5})", eid)
        title = " ".join((entry.findtext("a:title", default="", namespaces=NS) or "").split())
        cats = [c.get("term") for c in entry.findall("a:category", NS)]
        if m and title and title.lower() != "error":
            found[m.group(1)] = (title, cats)
    for aid in batch:
        title, cats = found.get(aid, ("NOT FOUND ON ARXIV", []))
        audio = any(c.startswith(("eess.AS", "cs.SD", "eess.SP")) for c in cats)
        rows.append((aid, title, ",".join(cats[:3]), "yes" if audio else "CHECK"))
    time.sleep(3)

lines = ["| arXiv ID | Real title on arXiv | Categories | Audio/speech category? |", "|---|---|---|---|"]
lines += [f"| [{a}](https://arxiv.org/abs/{a}) | {t} | {c} | {ok} |" for a, t, c, ok in rows]
(OUT / "citation_check.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
missing = sum(1 for r in rows if r[1] == "NOT FOUND ON ARXIV")
offtopic = sum(1 for r in rows if r[3] == "CHECK")
print(f"{len(rows)} arXiv citations | not found: {missing} | not in audio/speech categories: {offtopic}")
