module SymplecticVerlet
export verlet_step

function verlet_step(q::Float64, p::Float64, grad_V_fn, dt::Float64, m::Float64=1.0)
    p_half = p - 0.5 * dt * grad_V_fn(q)
    q_next = q + dt * p_half / m
    p_next = p_half - 0.5 * dt * grad_V_fn(q_next)
    return q_next, p_next
end
end
