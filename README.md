# CSPC — PW1 Lab A
# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:

conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- A radioactive decay simulation in Python and vectorised NumPy, with unit tests and speed benchmark.

**Speed comparison (loop vs NumPy):**
- loop : 4.87788 s
- numpy : 0.00016 s
- speed-up: 29796x faster

**Tests:** all passing? yes

**Conclusion:**
- NumPy vectorization drastically improves performance compared to standard Python loops when processing large arrays (200,000 atoms), achieving a massive speed-up. Setting up Conda environments and unit tests ensures full reproducibility and code reliability across different systems.

## Pw1 — Lab B

The observed decay data followed an exponential decay curve. Comparing the scatter of observed values with the analytical law `N(t) = N0 * exp(-LAMBDA * t)` in `figure.png`, the two shapes clearly match, confirming the data obeys the expected decay law. The Snakemake pipeline automates figure generation: it reads `decay_observed.csv`, runs `plot.py`, and produces `figure.png`, rerunning only when inputs change.


## PW2 — Lab A

The measured mean acceleration was about −8.6 m/s², close to the expected −g ≈ −9.81 m/s², confirming the object was in free fall. The acceleration is noisy because it comes from differentiating the position twice; each derivative amplifies the noise in the data, and the standard deviation (≈ 28.7) is much larger than the mean (≈ −8.6). Integrating the noisy acceleration back up to velocity and then to position recovered the original trajectory with a maximum difference of about 0.78 m — integration suppresses noise, the exact opposite of differentiation.