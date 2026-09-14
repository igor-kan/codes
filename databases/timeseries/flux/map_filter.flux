// Transform rows with map and filter.
from(bucket: "metrics")
  |> range(start: -2h)
  |> filter(fn: (r) => r._measurement == "temperature")
  |> map(fn: (r) => ({ r with _value: r._value * 9.0 / 5.0 + 32.0, unit: "F" }))
  |> filter(fn: (r) => r._value > 32.0)
