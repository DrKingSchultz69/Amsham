# READ ME FIRST: NeuroChain overnight research

> ⏱️ **This page takes 5 minutes.** You don't need to read the big report today.

---

## 🟢 TL;DR (the 5 things that matter)

1. **The research worked.** DeepTutor (GPT-5.6-Sol, high effort) ran 42 searches and wrote a 19,000-word report.
2. **The citations hold up.** All 41 arXiv papers exist. The 9 papers behind the novel ideas have correct titles.
3. **Your best paper idea:** a **"formant-safety projection layer"**. It mathematically limits how far the AI can move a singer's formants.
4. **Recommended paper:** combine 3 ideas: safety projection + confidence weighting + artifact fallback.
5. **Next step:** build a small Python prototype that shows the projection actually limits formant shift.

---

## 💡 The paper idea in plain words

**Problem:** AI vocal enhancers clean up audio but can quietly change *how the singer sounds*. They move formants, which carry the vowels and the voice's identity.

**Your fix:** before the AI's EQ is applied, a tiny math step checks:
*"Would this EQ push any formant more than δ Hz?"* If so, it softens the EQ just enough.

**Why it's new:** other papers *measure* formant damage after the fact. Yours *prevents* it, with a formula.

**Working title (from the report):**
*NeuroChain: Confidence-Aware Formant-Safe Neural DSP for Low-Latency Vocal Enhancement*

---

## 🏆 Ranked ideas (from the report)

| # | Idea | In one line | Novelty | Doable in 3 months? |
|---|---|---|---|---|
| **1** | **Formant-safety projection** | Math limit on formant shift | 🟢 High | 🟡 Medium |
| **2** | **Confidence-weighted strength** | Less processing when unsure where the formants are | 🟢 Med-High | 🟡 Medium |
| **3** | **Artifact sentinel** | Switch to safe mode when audio glitches | 🟡 Medium | 🟢 High |
| 4 | State-space control | Smooth knob changes, no "pumping" | 🟡 Medium | 🟢 High |
| 5 | Formant-safe effect chain | AI turns real EQ/comp/de-ess knobs | 🟡 Medium | 🟡 Medium |
| 6 | Vowel-trajectory loss | Train the AI to keep vowel movement | 🟡 Medium | 🟡 Medium |

👉 **Paper = #1 + #2 + #3.**

---

## ✅ How trustworthy is this?

| Check | Result |
|---|---|
| arXiv papers exist? | ✅ 41 / 41 real |
| Titles match for the papers behind the ideas? | ✅ 9 / 9 match |
| Other web links work? | ✅ 28 / 28 real (some sites block bots, but the pages exist) |
| Off-topic papers? | ⚠️ 6, but only dumped inside reference [9], **not used for any claim** |
| Statements tagged FACT / INTERPRETATION / HYPOTHESIS? | ✅ 48 FACT, 116 INTERPRETATION/HYPOTHESIS |

**Honest limits:**
- ⚠️ I checked that the papers are *real*. I did **not** read every paper to confirm every sentence. Before citing a fact in your paper, open that paper.
- ⚠️ About 10 of the sources are *about how to do literature reviews* (PRISMA etc.), not audio. So the audio-specific evidence is roughly **35–40 sources**, not 70.
- ⚠️ "Novel" means *"not found in the retrieved papers."* Still search IEEE Xplore and Google Scholar before submitting.
- ⚠️ DeepTutor skipped some formatting I asked for (no TL;DR at the top), so this page replaces it.

---

## 📖 Reading plan (3 short sessions, ~20 min each)

| Session | Read this | Where |
|---|---|---|
| 1 | The 6 ideas + ranking | [Report §6.4–6.5](NeuroChain_deep_research_report.md) (search "Idea A") |
| 2 | Research gaps + contradictions | [Report §6.3](NeuroChain_deep_research_report.md) (search "Open research gaps") |
| 3 | Validation plan + paper outline | [Report §6.5–6.6](NeuroChain_deep_research_report.md) (search "Baseline matrix") |

Skip §2 (review methodology) unless a reviewer asks how you searched.

---

## 📂 Files in this folder

| File | What it is |
|---|---|
| `READ_ME_FIRST.md` | ⭐ this page |
| `NeuroChain_deep_research_report.md` | full report (long) |
| `citation_check.md` | every arXiv paper checked against arXiv |
| `url_check.txt` | every web link checked |
| `prompt.txt` | exactly what DeepTutor was asked |
| others | logs and scripts (ignore) |

---

## ▶️ Next step (pick one, tell Claude)

- **A.** "Build the prototype": Python demo of the safety projection on real vocals ⭐ recommended
- **B.** "Write the Related Work section" in IEEE style
- **C.** "Do a deeper novelty check" on idea #1
