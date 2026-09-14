// Query a range from InfluxDB and filter.
from(bucket: "metrics")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu" and r._field == "usage_user")
  |> limit(n: 100)
