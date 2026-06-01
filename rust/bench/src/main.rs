use time_series_with_the_of_power_demand_using_prophet_in_python_core::fourier_seasonality;

fn main() {
    let t: Vec<f64> = (0..5000).map(|i| i as f64).collect();
    for _ in 0..5000 {
        let _ = fourier_seasonality(&t, 24.0, 3);
    }
}
