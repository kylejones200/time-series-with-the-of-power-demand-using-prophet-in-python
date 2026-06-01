#!/usr/bin/env python3
"""Python vs Rust kernel benchmark."""

from __future__ import annotations

import time
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from compute_kernel import fourier_seasonality  # noqa: E402

def main() -> None:
    t = np.ascontiguousarray(np.arange(5000, dtype=float))
    period, n_harmonics = 24.0, 3
    t0 = time.perf_counter()
    for _ in range(200):
        fourier_seasonality(t, period, n_harmonics)
    py_s = time.perf_counter() - t0
    try:
        import time_series_with_the_of_power_demand_using_prophet_in_python_rs as rs
    except ImportError:
        print("Build: maturin develop --release -m rust/py/Cargo.toml")
        print(f"Python {py_s:.3f}s")
        return
    rs_s = rs.bench_kernel_py(t, period, n_harmonics, 5000)
    print(f"Python {py_s:.3f}s Rust {rs_s:.3f}s speedup {py_s / max(rs_s, 1e-9):.1f}x")
    np.testing.assert_allclose(
        fourier_seasonality(t, period, n_harmonics),
        np.asarray(rs.fourier_seasonality_py(t, period, n_harmonics)),
        rtol=1e-10,
    )
    print("Correctness: OK")

if __name__ == "__main__":
    main()
