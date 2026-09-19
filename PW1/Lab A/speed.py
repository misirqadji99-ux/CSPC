import time
import numpy as np
from decay import simulate, simulate_loop

N0, rate = 200000, 0.05

# Измерение чистого Python (цикл)
start = time.perf_counter()
simulate_loop(N0, rate)
t_py = time.perf_counter() - start

# Измерение NumPy (векторизованный)
start = time.perf_counter()
simulate(N0, rate)
t_np = time.perf_counter() - start

speedup = t_py / t_np

print(f"Pure Python loop time: {t_py:.5f} s")
print(f"NumPy time:           {t_np:.5f} s")
print(f"NumPy is {speedup:.2f}x faster")