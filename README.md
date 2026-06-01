# Time Series with the of power demand using Prophet in Python

Published: 2023-12-13
Medium: [https://medium.com/@kyle-t-jones/time-series-with-the-of-power-demand-using-prophet-in-python-1680eb2d17d1](https://medium.com/@kyle-t-jones/time-series-with-the-of-power-demand-using-prophet-in-python-1680eb2d17d1)

## Business context

This project uses hourly energy demand data from ERCOT in Texas to predict future demand.

This project uses hourly energy demand data from ERCOT in Texas to predict future demand.

This chart is messy because it is hourly figures. We could smooth this out using resampling. For now, I am going to leave it.



## Rust performance port

Side-by-side **Python vs Rust** implementation of the numeric hot loop — Fourier seasonality features. Reference PyO3 benchmark: **see `benchmark_rust.py`** on a release build (local machine; run `benchmark_rust.py` to reproduce).

| Path | Role |
|------|------|
| `src/compute_kernel.py` | Python/numpy reference kernel |
| `rust/core/` | Pure Rust library |
| `rust/py/` | PyO3 bindings |
| `rust/bench/` | Standalone CLI benchmark |
| `benchmark_rust.py` | Python vs Rust timing + correctness check |

```bash
# Rust-only CLI benchmark
cd rust && cargo run --release -p time_series_with_the_of_power_demand_using_prophet_in_python_bench

# Python vs Rust (PyO3)
pip install maturin numpy
maturin develop --release -m rust/py/Cargo.toml
python benchmark_rust.py
```

Python ML training, solvers, and orchestration stay in Python; Rust targets the numeric hot loops. Stochastic generators validate output shapes; deterministic kernels match at tight floating-point tolerance.


## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).