-- 1D Kalman Filter in Lua (Numerical Recipes 3rd Ed. Chapter 15)

local KalmanFilter = {}
KalmanFilter.__index = KalmanFilter

function KalmanFilter.new(x, p, q, r)
    return setmetatable({x = x, p = p, q = q, r = r}, KalmanFilter)
end

function KalmanFilter:predict()
    self.p = self.p + self.q
end

function KalmanFilter:update(z)
    local k = self.p / (self.p + self.r)
    self.x = self.x + k * (z - self.x)
    self.p = (1.0 - k) * self.p
    return self.x
end

local kf = KalmanFilter.new(0.0, 1.0, 0.01, 0.1)
for _, z in ipairs({0.9, 1.1, 0.95, 1.05}) do
    kf:predict()
    kf:update(z)
end
assert(math.abs(kf.x - 1.0) < 0.2)
print("Lua Kalman Filter verified.")
