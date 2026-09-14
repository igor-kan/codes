// Filtering, ordering and ranges.
g.V().hasLabel('person').
  where(has('age', gte(30))).
  order().by('age', desc).
  range(0, 10).
  project('name', 'age').
    by('name').
    by('age')
