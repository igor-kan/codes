# Database Query Languages

Query and schema examples for graph and NoSQL database families, plus
time-series and vector workloads. Each file is a focused, runnable snippet for
the relevant shell or driver.

## Layout

| Directory | Engine | Language | Files |
|:---|:---|:---|:---|
| `graph/cypher/` | Neo4j | Cypher | create, match, merge, paths, aggregation, constraints |
| `graph/gremlin/` | Apache TinkerPop | Gremlin (Groovy) | traversals, mutations, grouping, shortest path |
| `graph/sparql/` | RDF stores (Blazegraph, GraphDB, Jena) | SPARQL 1.1 | query, construct, aggregate, property paths, update |
| `graph/datalog/` | Souffle / DDlog | Datalog | transitive closure, reachability, recursion, negation |
| `document/mongodb/` | MongoDB | MQL / mongosh | inserts, queries, updates, aggregation, lookup, transactions, change streams |
| `wide_column/cassandra/` | Apache Cassandra | CQL | keyspaces, collections, time-series, secondary indexes, materialized views |
| `key_value/redis/` | Redis | RESP / Lua | strings, lists, hashes, sets, sorted sets, streams, transactions, pub/sub |
| `search/elasticsearch/` | Elasticsearch / OpenSearch | Query DSL (JSON) | mappings, settings, bulk, match/bool queries, aggregations |
| `timeseries/flux/` | InfluxDB | Flux | range, window, join, map/filter, writes |
| `timeseries/promql/` | Prometheus | PromQL | selectors, rates, aggregation, histograms, alerts |
| `vector/` | PostgreSQL + pgvector | SQL | setup, similarity search, HNSW/IVFFlat indexes, hybrid search |

The complementary relational examples live in `../algorithms/10_sql/`.

## Notes

- `search/elasticsearch/bulk_index.ndjson` is newline-delimited JSON (the bulk
  API format), not a single JSON document.
- Graph and NoSQL snippets are written for each engine's native shell; the
  MongoDB examples are validated as JavaScript and the Elasticsearch examples
  as JSON.
