//! 4th-Order Runge-Kutta ODE Integrator.

pub fn rk4_step<F>(t: f64, y: &[f64], dt: f64, f: &F) -> Vec<f64>
where
    F: Fn(f64, &[f64]) -> Vec<f64>,
{
    let n = y.len();
    let k1 = f(t, y);

    let mut y_temp = vec![0.0; n];
    for i in 0..n {
        y_temp[i] = y[i] + 0.5 * dt * k1[i];
    }
    let k2 = f(t + 0.5 * dt, &y_temp);

    for i in 0..n {
        y_temp[i] = y[i] + 0.5 * dt * k2[i];
    }
    let k3 = f(t + 0.5 * dt, &y_temp);

    for i in 0..n {
        y_temp[i] = y[i] + dt * k3[i];
    }
    let k4 = f(t + dt, &y_temp);

    let mut y_next = vec![0.0; n];
    for i in 0..n {
        y_next[i] = y[i] + (dt / 6.0) * (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i]);
    }
    y_next
}

pub fn rk4_integrate<F>(t0: f64, tf: f64, y0: &[f64], n_steps: usize, f: F) -> (Vec<f64>, Vec<Vec<f64>>)
where
    F: Fn(f64, &[f64]) -> Vec<f64>,
{
    let dt = (tf - t0) / (n_steps as f64);
    let mut t_vals = Vec::with_capacity(n_steps + 1);
    let mut y_vals = Vec::with_capacity(n_steps + 1);

    let mut t = t0;
    let mut y = y0.to_vec();

    t_vals.push(t);
    y_vals.push(y.clone());

    for _ in 0..n_steps {
        y = rk4_step(t, &y, dt, &f);
        t += dt;
        t_vals.push(t);
        y_vals.push(y.clone());
    }

    (t_vals, y_vals)
}
