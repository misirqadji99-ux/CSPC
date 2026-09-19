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
