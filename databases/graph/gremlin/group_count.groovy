// Grouping and aggregation.
g.V().hasLabel('person').
  groupCount().by('country')

g.V().hasLabel('order').
  group().
    by('status').
    by(values('amount').sum())
