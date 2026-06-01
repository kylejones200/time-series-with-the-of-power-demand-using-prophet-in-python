use time_series_with_the_of_power_demand_using_prophet_in_python_core::fourier_seasonality;
use numpy::{PyArray1, PyReadonlyArray1, IntoPyArray};
use pyo3::prelude::*;

#[pyfunction]
fn fourier_seasonality_py<'py>(
    py: Python<'py>,
    t: PyReadonlyArray1<f64>,
    period: f64,
    n_harmonics: usize,
) -> PyResult<Bound<'py, PyArray1<f64>>> {
    Ok(fourier_seasonality(t.as_slice()?, period, n_harmonics).into_pyarray(py))
}

#[pyfunction]
#[pyo3(signature = (t, period, n_harmonics, iterations=5_000))]
fn bench_kernel_py(
    t: PyReadonlyArray1<f64>,
    period: f64,
    n_harmonics: usize,
    iterations: usize,
) -> PyResult<f64> {
    let tb = t.as_slice()?.to_vec();
    let start = std::time::Instant::now();
    for _ in 0..iterations {
        let _ = fourier_seasonality(&tb, period, n_harmonics);
    }
    Ok(start.elapsed().as_secs_f64())
}

#[pymodule]
fn time_series_with_the_of_power_demand_using_prophet_in_python_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fourier_seasonality_py, m)?)?;
    m.add_function(wrap_pyfunction!(bench_kernel_py, m)?)?;
    Ok(())
}
