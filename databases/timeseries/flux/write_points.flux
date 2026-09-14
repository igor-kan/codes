// Write points to a bucket.
import "influxdata/influxdb/schema"

data = [
  {_time: now(), _measurement: "sensor", sensor_id: "a", _field: "temp", _value: 21.5},
  {_time: now(), _measurement: "sensor", sensor_id: "b", _field: "temp", _value: 19.8},
]

data
  |> schema.fieldsAsCols()
  |> to(bucket: "sensors", org: "example")
