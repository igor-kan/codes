# Batch vs Stream Processing (DDIA Ch. 10-11)

## Batch

- Process bounded input; MapReduce, Spark, Flink batch.
- MapReduce: map, shuffle, reduce; fault tolerance via recomputation.
- Join strategies: broadcast, partitioned, sort-merge.
- Materialization pipelines (dbt, Airflow) for analytics.

## Stream

- Process unbounded events continuously.
- **Sources:** logs (Kafka), CDC, message queues, sensor feeds.
- **Time:** event time vs processing time; watermarks; late events.
- **Exactly-once:** checkpointing + idempotent sinks; Kafka transactions.
- **Windowing:** tumbling, hopping, sliding, session.
- **State:** keyed state, joins, and materialized views (Kafka Streams, Flink).

## Lambda vs Kappa

- **Lambda:** batch + speed layers; two codebases, consistent results.
- **Kappa:** single streaming pipeline reprocessed from the log.
