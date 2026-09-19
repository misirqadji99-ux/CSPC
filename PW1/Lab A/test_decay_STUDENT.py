"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_simulate_negative_rate():
    with pytest.raises(ValueError):
        simulate(100, -0.1)


def test_simulate_average():
    n0, rate = 1000, 0.05
    dt, steps = 0.05, 200
    t = steps * dt  # t = 10
    expected = n0 * np.exp(-rate * t)
    
    seeds = range(50)
    results = [simulate(n0, rate, seed=s)[-1] for s in seeds]
    avg_result = np.mean(results)
    
    assert avg_result == pytest.approx(expected, rel=1e-1)