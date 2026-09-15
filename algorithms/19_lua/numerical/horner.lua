-- Horner's method for polynomial evaluation.
local function horner(coefficients, x)
  local result = 0
  for i = #coefficients, 1, -1 do result = result * x + coefficients[i] end
  return result
end

local function horner_with_derivative(coefficients, x)
  local value, derivative = 0, 0
  for i = #coefficients, 1, -1 do
    derivative = derivative * x + value
    value = value * x + coefficients[i]
  end
  return value, derivative
end

local coefficients = { -1, 2, -6, 2 }
local value, derivative = horner_with_derivative(coefficients, 3)
assert(math.abs(value - 5) < 1e-9 and math.abs(derivative - 20) < 1e-9, "horner failed")
assert(math.abs(horner(coefficients, 3) - 5) < 1e-9, "horner evaluation failed")
print("[Lua Horner] polynomial and derivative verified")
