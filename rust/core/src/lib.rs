//! Fourier seasonality features for hourly demand.

pub fn fourier_seasonality(t: &[f64], period: f64, n_harmonics: usize) -> Vec<f64> {
    let n = t.len();
    let n_feats = n_harmonics * 2;
    let mut out = vec![0.0; n * n_feats];
    for (i, &ti) in t.iter().enumerate() {
        for h in 0..n_harmonics {
            let k = (h + 1) as f64;
            let angle = 2.0 * std::f64::consts::PI * k * ti / period;
            out[i * n_feats + 2 * h] = angle.sin();
            out[i * n_feats + 2 * h + 1] = angle.cos();
        }
    }
    out
}
