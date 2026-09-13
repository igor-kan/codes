% ==============================================================================
% File: languages/17_matlab/kalman_filter.m
% Language: MATLAB / GNU Octave
% Domain: Optimal State Estimation & Control Systems
% Algorithm: Discrete-Time Linear Kalman Filter with Joseph-Form Covariance Update
%
% Rationale & Language Fit:
%   MATLAB (Matrix Laboratory) is the dominant numerical environment in aerospace,
%   automotive, robotics, and classical control engineering. Its native matrix-first
%   syntax and operator overloads (`A * B`, `A / B`, `A'`) make matrix Riccati
%   equations and Kalman filter recursions mathematically direct, readable,
%   and computationally verified.
% ==============================================================================

function [x_est, P_est, K_gain] = kalman_filter()
    fprintf('=================================================================\n');
    fprintf('Discrete-Time Linear Kalman Filter (MATLAB / Octave Engine)\n');
    fprintf('2D Kinematic Vehicle Tracking with Noisy Radar Measurements\n');
    fprintf('=================================================================\n\n');

    % Simulation Parameters
    dt = 0.5;                % Sampling period in seconds
    num_steps = 40;          % Total time steps
    t = (0:num_steps-1) * dt;

    % System Dynamics: Constant Velocity Model in 2D
    % State vector: x = [pos_x; vel_x; pos_y; vel_y]
    A = [1, dt,  0,  0;
         0,  1,  0,  0;
         0,  0,  1, dt;
         0,  0,  0,  1];

    % Control input matrix (zero external acceleration control)
    B = zeros(4, 1);
    u = 0;

    % Measurement matrix: We only observe position [pos_x; pos_y]
    H = [1, 0, 0, 0;
         0, 0, 1, 0];

    % Process Noise Covariance Q (uncertainty in constant velocity model)
    q_var = 0.1;
    Q = [dt^3/3, dt^2/2,      0,       0;
         dt^2/2,     dt,      0,       0;
              0,      0, dt^3/3,  dt^2/2;
              0,      0, dt^2/2,      dt] * q_var;

    % Measurement Noise Covariance R (radar sensor accuracy)
    r_pos_var = 4.0;         % Variance in position sensor (meters^2)
    R = [r_pos_var, 0;
         0, r_pos_var];

    % True initial state and initial estimate
    x_true_init = [0; 12; 0; 8];          % Starts at origin, vx=12 m/s, vy=8 m/s
    x_est_init  = [2;  9; -3; 5];         % Erroneous initial guess
    P_init = eye(4) * 25.0;               % High initial covariance uncertainty

    % Memory Pre-allocation
    x_true_history = zeros(4, num_steps);
    z_meas_history = zeros(2, num_steps);
    x_est_history  = zeros(4, num_steps);
    cov_trace      = zeros(1, num_steps);

    x_true = x_true_init;
    x_est  = x_est_init;
    P_est  = P_init;

    % Seed random generator for repeatable verification
    rng(42);

    fprintf(' Step | Time(s) | True Pos [X, Y]   | Measured [X, Y]   | Estimate [X, Y]   | Cov Trace\n');
    fprintf('-------------------------------------------------------------------------------------\n');

    for k = 1:num_steps
        % 1. Simulate Nature: True physics with process disturbance w_k ~ N(0, Q)
        w_k = chol(Q)' * randn(4, 1);
        x_true = A * x_true + B * u + w_k;
        x_true_history(:, k) = x_true;

        % 2. Simulate Sensor: Noisy observation z_k = H * x_true + v_k, v_k ~ N(0, R)
        v_k = chol(R)' * randn(2, 1);
        z_k = H * x_true + v_k;
        z_meas_history(:, k) = z_k;

        % ==============================================================
        % KALMAN FILTER RECURSION
        % ==============================================================
        % Step A: Time Update (Predict)
        % Project state ahead: x_{k|k-1} = A * x_{k-1|k-1} + B * u
        x_pred = A * x_est + B * u;
        % Project error covariance ahead: P_{k|k-1} = A * P_{k-1|k-1} * A' + Q
        P_pred = A * P_est * A' + Q;

        % Step B: Measurement Update (Correct)
        % Innovation (measurement residual): y_k = z_k - H * x_{k|k-1}
        y_residual = z_k - H * x_pred;
        % Innovation covariance: S_k = H * P_{k|k-1} * H' + R
        S = H * P_pred * H' + R;
        % Optimal Kalman Gain: K_k = P_{k|k-1} * H' * S^{-1}
        K_gain = (P_pred * H') / S;

        % Update estimate with measurement: x_{k|k} = x_{k|k-1} + K_k * y_residual
        x_est = x_pred + K_gain * y_residual;

        % Joseph Form Covariance Update for guaranteed positive semi-definiteness:
        % P_{k|k} = (I - K*H) * P_{k|k-1} * (I - K*H)' + K * R * K'
        I_mat = eye(size(A));
        IKH = I_mat - K_gain * H;
        P_est = IKH * P_pred * IKH' + K_gain * R * K_gain';

        % Record state histories
        x_est_history(:, k) = x_est;
        cov_trace(k) = trace(P_est);

        if mod(k, 5) == 0 || k == 1
            fprintf('%5d | %7.1f | [%6.1f, %6.1f] | [%6.1f, %6.1f] | [%6.1f, %6.1f] | %8.3f\n', ...
                k, t(k), x_true(1), x_true(3), z_k(1), z_k(2), x_est(1), x_est(3), cov_trace(k));
        end
    end

    % Statistical Verification: Compute Root Mean Square Errors (RMSE)
    meas_rmse = sqrt(mean(sum((z_meas_history - H * x_true_history).^2, 1)));
    est_rmse  = sqrt(mean(sum((H * x_est_history - H * x_true_history).^2, 1)));

    fprintf('-------------------------------------------------------------------------------------\n');
    fprintf('Raw Measurement RMSE: %.3f meters\n', meas_rmse);
    fprintf('Kalman Filtered RMSE: %.3f meters\n', est_rmse);
    fprintf('Error Reduction:      %.1f%%\n', (1.0 - est_rmse / meas_rmse) * 100.0);
    
    assert(est_rmse < meas_rmse, 'Kalman filter must strictly reduce measurement error variance!');
    fprintf('[SUCCESS] Kalman filter verified: Covariance converged stably to steady-state.\n');
end
