"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

t, y = np.loadtxt("freefall.csv", delimiter=",", skiprows=1, unpack=True)

v = np.gradient(y, t)
a = np.gradient(v, t)
print("mean acceleration =", a.mean())
print("std acceleration =", a.std())


v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]
max_diff = np.max(np.abs(y_rec - y))
print("max position difference =", max_diff)

fig, axes = plt.subplots(3, 1, sharex=True)

axes[0].plot(t, y)
axes[0].set_ylabel("position (m)")

axes[1].plot(t, v)
axes[1].set_ylabel("velocity (m/s)")

axes[2].plot(t, a)
axes[2].axhline(-9.81, color="red", linestyle="--")
axes[2].set_ylabel("acceleration (m/s²)")
axes[2].set_xlabel("time (s)")

plt.savefig("motion.png")
plt.show()