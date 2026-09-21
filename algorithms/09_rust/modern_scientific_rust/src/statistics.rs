//! Basic Descriptive Statistics and Pearson Correlation.

pub fn mean(data: &[f64]) -> f64 {
    data.iter().sum::<f64>() / (data.len() as f64)
}

pub fn variance(data: &[f64]) -> f64 {
    let m = mean(data);
    data.iter().map(|x| (x - m).powi(2)).sum::<f64>() / ((data.len() - 1) as f64)
}

pub fn std_dev(data: &[f64]) -> f64 {
    variance(data).sqrt()
}

pub fn pearson_correlation(x: &[f64], y: &[f64]) -> f64 {
    assert_eq!(x.len(), y.len());
    let mx = mean(x);
    let my = mean(y);
    let mut cov = 0.0;
    let mut var_x = 0.0;
    let mut var_y = 0.0;

    for (xi, yi) in x.iter().zip(y.iter()) {
        let dx = xi - mx;
        let dy = yi - my;
        cov += dx * dy;
        var_x += dx * dx;
        var_y += dy * dy;
    }

    cov / (var_x.sqrt() * var_y.sqrt())
}
