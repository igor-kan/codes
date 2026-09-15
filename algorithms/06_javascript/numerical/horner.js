function horner(coefficients, x) {
  let result = 0;
  for (let i = coefficients.length - 1; i >= 0; i -= 1) result = result * x + coefficients[i];
  return result;
}

function hornerWithDerivative(coefficients, x) {
  let value = 0;
  let derivative = 0;
  for (let i = coefficients.length - 1; i >= 0; i -= 1) {
    derivative = derivative * x + value;
    value = value * x + coefficients[i];
  }
  return { value, derivative };
}

module.exports = { horner, hornerWithDerivative };

if (require.main === module) {
  const coefficients = [-1, 2, -6, 2];
  const { value, derivative } = hornerWithDerivative(coefficients, 3);
  if (Math.abs(value - 5) > 1e-9 || Math.abs(derivative - 20) > 1e-9) throw new Error("horner failed");
  if (Math.abs(horner(coefficients, 3) - 5) > 1e-9) throw new Error("horner evaluation failed");
  console.log("[JavaScript Horner] polynomial and derivative verified");
}
