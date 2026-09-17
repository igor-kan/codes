# 1D Kalman Filter in Julia (Numerical Recipes 3rd Ed. Chapter 15)

mutable struct KalmanFilter1D
    x::Float64
    p::Float64
    q::Float64
    r::Float64
end

function predict!(kf::KalmanFilter1D)
    kf.p += kf.q
end

function update!(kf::KalmanFilter1D, z::Float64)
    k = kf.p / (kf.p + kf.r)
    kf.x += k * (z - kf.x)
    kf.p = (1.0 - k) * kf.p
    return kf.x
end

kf = KalmanFilter1D(0.0, 1.0, 0.01, 0.1)
for z in [0.9, 1.1, 0.95, 1.05]
    predict!(kf)
    update!(kf, z)
end
@assert abs(kf.x - 1.0) < 0.2
println("Julia Kalman Filter verified.")
