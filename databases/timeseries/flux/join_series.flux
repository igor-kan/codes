// Join two measurements on time.
cpu = from(bucket: "metrics")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> aggregateWindow(every: 1m, fn: mean)

mem = from(bucket: "metrics")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "mem")
  |> aggregateWindow(every: 1m, fn: mean)

join(tables: {cpu: cpu, mem: mem}, on: ["_time"])
