module StaggeredGrid
export pressure_poisson_rhs

function pressure_poisson_rhs(u_star::Matrix{Float64}, v_star::Matrix{Float64}, dx::Float64, dt::Float64)
    du_dx = (u_star[2:end, :] - u_star[1:end-1, :]) ./ dx
    return du_dx ./ dt
end
end
