# Space-Based Architecture

Achieve elastic scale by removing the central database bottleneck: process in
memory over a distributed **tuple space**, with asynchronous data writers to
persistence.

## Components

- Processing units (stateless or in-memory replicated).
- Virtualized middleware: messaging grid, data grid, processing grid, deployment
  manager.
- Asynchronous data writers.

Good for extreme, spiky concurrency (ticketing, online auctions). Complexity and
data consistency are the price.

Related: In-Memory Data Grid, Event-Driven.
