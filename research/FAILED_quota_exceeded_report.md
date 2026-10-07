# Research topic: "NeuroChain: Real-Time Low-Latency Neural DSP for Formant-Preserving Vocal Enhancement"

Goal: Produce a literature review and research plan for a system that enhances singing/speech vocals in real time (live performance and plugin use) using neural networks, while preserving the singer's formants (vocal identity/timbre).

Please cover:
1. Background: classic DSP vocal processing (EQ, compression, de-essing, pitch correction), formants and why pitch shifting destroys them, and classic formant-preservation methods (LPC, cepstral envelope, PSOLA, WORLD vocoder).
2. Neural approaches: DDSP, neural vocoders (HiFi-GAN, Vocos, LPCNet), speech enhancement models (DeepFilterNet, RNNoise, Demucs), voice conversion (RVC, so-vits-svc), and differentiable DSP chains. For each: latency, model size, causal or not, and whether formants are kept.
3. Real-time constraints: latency budgets (<10 ms for live monitoring), causal/streaming architectures, buffer and block sizes, CPU vs GPU inference, quantization and pruning, and running inside a VST3/AU/CLAP plugin (ONNX Runtime, RTNeural, libtorch).
4. Evaluation: objective metrics (PESQ, STOI, SI-SDR, formant error F1-F3, spectral envelope distance, real-time factor, end-to-end latency) and subjective tests (MUSHRA, MOS).
5. Datasets for singing and speech (VCTK, NUS-48E, VocalSet, OpenSinger, M4Singer, DAPS) and their licenses.
6. Gap analysis: what current tools and papers fail to do at the same time (low latency + formant preservation + quality).
7. A proposed NeuroChain architecture: a chain of small neural modules (denoise -> pitch/formant analysis -> enhancement -> resynthesis) with a per-module latency budget.
8. A 3-month experiment plan with baselines, ablations and success criteria.

Output: structured report with headings, a comparison table of methods, and citations (arXiv links) for every claim. Flag anything uncertain.

Error calling Codex: Codex usage quota exceeded or rate limit triggered. Please try again later.

Error calling Codex: Codex usage quota exceeded or rate limit triggered. Please try again later.

Error calling Codex: Codex usage quota exceeded or rate limit triggered. Please try again later.

Error calling Codex: Codex usage quota exceeded or rate limit triggered. Please try again later.

Error calling Codex: Codex usage quota exceeded or rate limit triggered. Please try again later.

Error calling Codex: Codex usage quota exceeded or rate limit triggered. Please try again later.

Error calling Codex: Codex usage quota exceeded or rate limit triggered. Please try again later.