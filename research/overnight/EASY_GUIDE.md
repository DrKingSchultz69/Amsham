# NeuroChain: The Easy Guide

> **Start now:** read Part 1 only (3 minutes). Then stop or continue, your choice.
>
> This guide condenses the full 19,000-word report into 8 short parts.
> You never need to open the big report unless you want the details.

---

## ✅ Your progress

| Part | Topic | Time | Done? |
|---|---|---|---|
| 1 | The problem | 3 min | ☐ |
| 2 | 8 words you need | 3 min | ☐ |
| 3 | What other researchers built | 4 min | ☐ |
| 4 | The gap (what nobody has done) | 2 min | ☐ |
| 5 | **Your main idea** ⭐ | 5 min | ☐ |
| 6 | 3 helper ideas | 3 min | ☐ |
| 7 | The paper plan | 4 min | ☐ |
| 8 | 5 papers to read first | 2 min | ☐ |

**Total: about 26 minutes.** Do it in 2–3 sittings.

---

## Part 1: The problem (3 min)

**One sentence:** AI vocal tools make a voice *cleaner* but can make it *sound like a different person*.

```
  Singer's voice ──► AI cleaner ──► Clean voice ✅
                                     ... but vowels and voice identity changed ❌
```

**Why it happens:**
- Your voice has resonance peaks called **formants**.
- Formants tell the listener *which vowel* you sing (a, e, i, o, u) and *who* is singing.
- AI tools boost and cut frequencies. If a boost lands on the side of a formant, the formant **moves**.
- A moved formant = a different vowel colour or a different-sounding singer.

**The extra challenge:** live singers need the processed sound back in their ears **within 10 ms**. Longer delays feel like an echo and throw off their timing.

> 🎯 **Takeaway:** NeuroChain must do 3 things at once: **clean** the voice, **keep the formants**, and stay **under 10 ms**.

☐ Part 1 done.

---

## Part 2: 8 words you need (3 min)

| Word | Simple meaning |
|---|---|
| **Formant** | A resonance peak in the voice; it shapes vowels and identity |
| **F1, F2, F3** | The 1st, 2nd and 3rd formants (F1 + F2 mostly decide the vowel) |
| **Spectral envelope** | The overall "shape" of the voice's frequencies; formants are its hills |
| **EQ (equalizer)** | A tool that boosts or cuts frequencies |
| **Latency** | The delay between singing and hearing the processed sound |
| **Causal** | Uses only past and present audio, never the future (required for live use) |
| **DSP** | Classic, predictable audio math (EQ, compressor, de-esser) |
| **Neural vocoder** | An AI that *re-creates* the voice from scratch (risky for identity) |

> 🎯 **Takeaway:** formants = the hills of the spectral envelope. EQ can push the hills sideways. Your paper stops that.

☐ Part 2 done.

---

## Part 3: What other researchers built (4 min)

The report found **4 families** of existing work. Each solves *one piece*.

| Family | What it's good at | What it's missing for you |
|---|---|---|
| **1. AI speech cleaners** (DeepFilterNet, FullSubNet, DCCRN) | Fast, real-time noise removal | No formant protection; not tested on singing |
| **2. Formant trackers** (KARMA, TVQCP, Heat-Maps) | *Measuring* where the formants are, some with a confidence score | Only measure; they don't *protect* anything |
| **3. Re-synthesis AI** (vocoders, DDSP, HiFi-Glot) | Rebuilding a voice from controls | Rebuilding can change identity; not built for live cleaning |
| **4. AI-controlled effects** (learned EQ/compressor) | AI turns real knobs, so the result is explainable | No formant safety rules |

**Big lesson from the report:**
- Use AI as the **knob-turner**, not as the **voice-maker**.
- Keep a real DSP chain (EQ, de-esser, compressor) doing the actual sound changes.
- That way the processing is predictable, explainable and fast.

> 🎯 **Takeaway:** the pieces exist separately. Nobody has joined them with a safety rule.

☐ Part 3 done.

---

## Part 4: The gap: what nobody has done (2 min)

**The main gap, in one line:**
> No paper found gives a **math guarantee** that AI processing won't move a singer's formants beyond a set limit.

**The 4 smaller gaps:**
1. **No safety bound:** papers *measure* formant damage after processing; none *prevent* it.
2. **Confidence is wasted:** trackers know when they're unsure, but no system uses that to process more gently.
3. **No singing tests:** most systems are only tested on speech.
4. **Fuzzy "real-time" claims:** papers say "real-time" but rarely measure the full delay from input to output.

> 🎯 **Takeaway:** gap #1 is your paper. Gaps #2–4 are your supporting contributions.

☐ Part 4 done.

---

## Part 5: Your main idea ⭐ (5 min)

### Name: the **formant-safety projection**

**What it does, in plain words:**
1. The AI suggests an EQ curve.
2. NeuroChain finds the formant peaks (F1, F2, F3).
3. For each peak it asks: *"Would this EQ push the peak more than δ Hz?"* (δ = your limit, e.g. 20 Hz)
4. If yes → it **softens the EQ slope at that peak**, just enough.
5. The safe EQ is applied to the voice.

```
 AI suggests EQ ──► [ Safety check at F1, F2, F3 ] ──► Safe EQ ──► Voice out
                          │
                          └─ too steep at a formant? → flatten it a little
```

### The math (only 1 formula matters)

**How far a formant moves:**

$$\Delta F \approx -\frac{g'(F)}{l''(F) + g''(F)}$$

| Symbol | Plain meaning |
|---|---|
| ΔF | How far the formant moves (Hz) |
| g′(F) | How **steep** the EQ is at the formant |
| l″(F) | How **sharp** the formant hill is |
| g″(F) | How **curved** the EQ is at the formant |

**The safety rule:** keep the EQ steepness small compared with the hill's sharpness:

$$|g'(F)| \le \delta \cdot |l''(F) + g''(F)|$$

**Intuition:** a sharp, narrow formant is hard to push. A wide, soft formant is easy to push. So the rule allows more EQ near sharp formants and less near soft ones.

### When it can fail (be honest about these in the paper)

**Must handle (core risks):**
1. **Flat hill:** if the bottom of the formula is near zero, the estimate blows up. → Switch to safe mode.
2. **Wrong peak:** the tracker mistakes a harmonic for a formant. → Use the tracker's confidence (Part 6).
3. **Peaks merge or split:** two formants close together. → Needs a joint rule for neighbouring formants.

**Mention as limits:**
- It only covers EQ, not compressor or pitch-shifting effects.
- It protects the formant's *position*, not its *height* or *width*.

> 🎯 **Takeaway:** it's a **local** guarantee, not a perfect one. Say exactly that in the paper. Reviewers respect honest limits.

☐ Part 5 done.

---

## Part 6: 3 helper ideas (3 min)

These make the main idea work in the real world.

### Helper 1: Confidence weighting
- **Problem:** the formant tracker is sometimes unsure (noise, breathy singing, vibrato).
- **Fix:** when it's unsure, NeuroChain uses gentler processing.
- **Formula:** `output = confidence × AI_EQ + (1 − confidence) × safe_EQ`

### Helper 2: Artifact sentinel
- **Problem:** AI processing sometimes glitches (clicks, pumping, warbling).
- **Fix:** a small monitor watches the output. If it spots a glitch, it switches to a safe preset for a moment.

### Helper 3: Real latency measurement
- **Problem:** papers claim "real-time" without measuring the full delay.
- **Fix:** timestamp the audio at every stage (input → AI → DSP → output) and report the **worst** delay, not the average.

> 🎯 **Takeaway:** main idea + Helper 1 + Helper 2 = your paper. Helper 3 makes your latency claims believable.

☐ Part 6 done.

---

## Part 7: The paper plan (4 min)

### Title
*NeuroChain: Confidence-Aware Formant-Safe Neural DSP for Low-Latency Vocal Enhancement*

### Your one main claim (keep it narrow)
> NeuroChain improves vocal quality **while moving formants less** than an AI EQ without the safety layer, under a measured live-latency budget.

### Experiments: what to compare
| # | System | Why |
|---|---|---|
| 1 | Unprocessed voice | Reference |
| 2 | Classic DSP chain (no AI) | Shows what the AI adds |
| 3 | AI EQ, **no** safety layer | Shows the problem |
| 4 | AI EQ **+** safety projection | Your main idea |
| 5 | **Full NeuroChain** (+ confidence + sentinel) | Your complete system |

### What to measure
1. **Formant shift** for F1–F3: average **and** worst case
2. **Cleaning quality:** PESQ, SI-SDR, listening test
3. **Identity:** does it still sound like the same singer?
4. **Latency:** full input-to-output delay, worst case
5. **Glitches:** how often the sentinel triggers

### Test material
Sustained vowels · vowel glides · fast singing · vibrato · breathy voice · noisy recordings · "s" and "sh" heavy lines

> 🎯 **Takeaway:** 5 systems × 5 measures. Removing one component at a time (ablation) proves each part helps.

☐ Part 7 done.

---

## Part 8: 5 papers to read first (2 min)

All 5 were checked: they exist, and their titles match.

| # | Paper | Why read it | Link |
|---|---|---|---|
| 1 | **HiFi-Glot** (2024) | Closest prior work: differentiable formant filters | [arXiv 2409.14823](https://arxiv.org/abs/2409.14823) |
| 2 | **KARMA** (2011) | Formant tracking **with confidence**, needed for Helper 1 | [arXiv 1107.0076](https://arxiv.org/abs/1107.0076) |
| 3 | **Formant Heat-Maps** (2022) | Robust AI formant tracking | [arXiv 2206.11632](https://arxiv.org/abs/2206.11632) |
| 4 | **FullSubNet** (2021) | Real-time AI cleaner (a baseline for you) | [arXiv 2010.15508](https://arxiv.org/abs/2010.15508) |
| 5 | **dCoNNear** (2025) | Avoiding AI audio glitches, needed for Helper 2 | [arXiv 2501.04116](https://arxiv.org/abs/2501.04116) |

**Reading tip:** for each paper read only the **abstract + figure 1 + conclusion**, about 5 minutes each.

☐ Part 8 done.

---

## ⚠️ What is NOT proven yet

| Claim | Status |
|---|---|
| The safety rule works on real singing | ❌ Not tested; your prototype will test it |
| Nobody has done this before | 🟡 Not found in 42 searches; still check IEEE Xplore and Google Scholar |
| Under 10 ms is achievable | 🟡 Plausible; must be measured |
| The 5 papers above exist and match | ✅ Verified |

---

## ▶️ Your next action (2 minutes)

Open **[HiFi-Glot on arXiv](https://arxiv.org/abs/2409.14823)** and read just the abstract. It's the closest existing work to your idea.

Then tell Claude: **"build the prototype"**.
