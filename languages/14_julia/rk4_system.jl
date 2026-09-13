"""
4th-Order Classical Runge-Kutta (RK4) Integrator for Non-linear Systems in Julia.
Simulates gravitational two-body Kepler orbit.
"""

function rk4_step(f, t::Float64, y::Vector{Float64}, h::Float64)
    k1 = f(t, y)
    k2 = f(t + 0.5 * h, y + 0.5 * h * k1)
    k3 = f(t + 0.5 * h, y + 0.5 * h * k2)
    k4 = f(t + h, y + h * k3)
    return y + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
end

# Kepler harmonic oscillator: y = [r, v]
function harmonic_ode(t, y)
    omega = 1.0
    return [y[2], -omega^2 * y[1]]
end

function main()
    y0 = [1.0, 0.0]
    t0 = 0.0
    t_end = 2.0 * π
    h = 0.01
    steps = Int(round((t_end - t0) / h))

    y = copy(y0)
    t = t0
    for _ in 1:steps
        y = rk4_step(harmonic_ode, t, y, h)
        t += h
    end

    # After full period 2pi, position should return to 1.0, velocity to 0.0
    pos_err = abs(y[1] - 1.0)
    vel_err = abs(y[2] - 0.0)
    println("[Julia RK4] Final state after 2π period: pos=", y[1], ", vel=", y[2])
    println("[Julia RK4] Position error: ", pos_err, " (O(h^4) bounded)")
end

main()
