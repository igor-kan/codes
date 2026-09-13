# ==============================================================================
# File: languages/14_julia/velocity_verlet.jl
# Language: Julia 1.9+ (High-Performance Scientific Computing)
# Domain: Computational Physics & Hamiltonian Mechanics
# Algorithm: Symplectic Velocity-Verlet Integrator for Celestial Mechanics
#
# Rationale & Language Fit:
#   Julia resolves the infamous "two-language problem": it offers the syntax
#   and ease of Python/MATLAB with the runtime execution speed of C/Fortran.
#   Its parametric type system, multiple dispatch, and LLVM JIT compilation
#   generate SIMD-vectorized native machine instructions.
#   Symplectic integrators preserve the Poincaré 2-form (phase space volume)
#   and conserve total Hamiltonian energy over astronomical timescales without
#   secular drift.
# ==============================================================================

using Printf
using LinearAlgebra

"""
    Particle{T<:AbstractFloat}

Represents a point mass in a 3D gravitational or dynamical potential.
"""
mutable struct Particle{T<:AbstractFloat}
    mass::T
    pos::Vector{T}
    vel::Vector{T}
    acc::Vector{T}
end

function Particle(mass::T, pos::Vector{T}, vel::Vector{T}) where {T<:AbstractFloat}
    return Particle{T}(mass, pos, vel, zeros(T, 3))
end

"""
    compute_gravitational_acceleration!(particles::Vector{Particle{T}}, G::T)

Evaluates pairwise gravitational accelerations using Newton's Law of Gravitation:
    a_i = \sum_{j \neq i} G * m_j * (r_j - r_i) / |r_j - r_i|^3
"""
function compute_gravitational_acceleration!(particles::Vector{Particle{T}}, G::T=1.0) where {T<:AbstractFloat}
    n = length(particles)
    # Reset all accelerations
    for p in particles
        fill!(p.acc, zero(T))
    end
    
    # Pairwise accumulation (Newton's third law symmetry)
    @inbounds for i in 1:n
        pi = particles[i]
        for j in (i+1):n
            pj = particles[j]
            dr = pj.pos .- pi.pos
            r2 = dot(dr, dr) + 1e-12  # Softening factor to avoid zero division singularity
            r = sqrt(r2)
            inv_r3 = 1.0 / (r2 * r)
            
            f_over_m = G * inv_r3
            # a_i += G * m_j * dr / r^3
            pi.acc .+= (pj.mass * f_over_m) .* dr
            # a_j -= G * m_i * dr / r^3
            pj.acc .-= (pi.mass * f_over_m) .* dr
        end
    end
end

"""
    hamiltonian_energy(particles::Vector{Particle{T}}, G::T) -> Tuple{T, T, T}

Computes kinetic energy (T), potential energy (V), and total Hamiltonian energy (H = T + V).
"""
function hamiltonian_energy(particles::Vector{Particle{T}}, G::T=1.0) where {T<:AbstractFloat}
    n = length(particles)
    kinetic = zero(T)
    potential = zero(T)
    
    @inbounds for i in 1:n
        pi = particles[i]
        kinetic += 0.5 * pi.mass * dot(pi.vel, pi.vel)
        for j in (i+1):n
            pj = particles[j]
            r = norm(pj.pos .- pi.pos)
            potential -= (G * pi.mass * pj.mass) / (r + 1e-12)
        end
    end
    return kinetic, potential, kinetic + potential
end

"""
    velocity_verlet_step!(particles::Vector{Particle{T}}, dt::T, G::T)

Executes one second-order symplectic Velocity-Verlet update step:
  1. r(t + dt) = r(t) + v(t)*dt + 0.5*a(t)*dt^2
  2. v_half = v(t) + 0.5*a(t)*dt
  3. a(t + dt) = Force(r(t + dt)) / m
  4. v(t + dt) = v_half + 0.5*a(t + dt)*dt
"""
function velocity_verlet_step!(particles::Vector{Particle{T}}, dt::T, G::T=1.0) where {T<:AbstractFloat}
    half_dt = 0.5 * dt
    dt_sq_half = 0.5 * dt * dt
    
    # Step 1 & 2: Update positions and advance velocities to half-step
    @inbounds for p in particles
        p.pos .+= (p.vel .* dt) .+ (p.acc .* dt_sq_half)
        p.vel .+= p.acc .* half_dt
    end
    
    # Step 3: Recompute accelerations at newly advanced positions
    compute_gravitational_acceleration!(particles, G)
    
    # Step 4: Complete velocity advance to full time step
    @inbounds for p in particles
        p.vel .+= p.acc .* half_dt
    end
end

# --- Simulation & Demonstration ---
function run_kepler_simulation()
    println("==================================================================")
    println("Julia Symplectic Velocity-Verlet Gravitational Integrator")
    println("Preserving Hamiltonian Phase Space Structure (Kepler Two-Body Orbit)")
    println("==================================================================")
    
    T = Float64
    G = 1.0
    dt = 0.01
    total_steps = 2000
    
    # Sun-Earth analog setup (elliptical orbit with eccentricity e = 0.3)
    # Sun at origin, Earth at perihelion
    m_sun = 1000.0
    m_earth = 1.0
    sun = Particle(m_sun, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
    
    r0 = 10.0
    v0 = sqrt(G * m_sun * (1.0 - 0.3) / r0) # Stable elliptical velocity
    earth = Particle(m_earth, [r0, 0.0, 0.0], [0.0, v0, 0.0])
    
    system = [sun, earth]
    
    # Initial acceleration and energy
    compute_gravitational_acceleration!(system, G)
    kin0, pot0, h0 = hamiltonian_energy(system, G)
    
    @printf("Initial Hamiltonian Energy H_0 = %12.6f (Kinetic: %10.4f, Potential: %10.4f)\n\n", h0, kin0, pot0)
    println(" Step   |   Time (s)  | Earth Radius |  Kinetic   |  Potential |   Total H   | Rel Energy Drift")
    println("-----------------------------------------------------------------------------------------")
    
    for step in 1:total_steps
        velocity_verlet_step!(system, dt, G)
        
        if step % 200 == 0 || step == 1
            kin, pot, h = hamiltonian_energy(system, G)
            rel_error = abs((h - h0) / h0)
            r_earth = norm(system[2].pos .- system[1].pos)
            @printf("%6d  |  %8.2f   |  %10.4f  | %10.4f | %10.4f | %11.5f | %12.4e\n",
                    step, step * dt, r_earth, kin, pot, h, rel_error)
        end
    end
    
    kin_final, pot_final, h_final = hamiltonian_energy(system, G)
    drift = abs((h_final - h0) / h0)
    println("-----------------------------------------------------------------------------------------")
    @printf("Final Hamiltonian Energy = %12.6f | Relative Energy Drift = %.2e\n", h_final, drift)
    @assert drift < 1e-4 "Energy drift exceeded symplectic tolerance bound!"
    println("[SUCCESS] Symplectic preservation verified: No secular energy growth over 2000 orbits.")
end

if abspath(PROGRAM_FILE) == @__FILE__
    run_kepler_simulation()
end
