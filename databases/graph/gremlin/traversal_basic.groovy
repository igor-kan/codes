// Basic Gremlin traversal steps.
g.V().hasLabel('person').
  has('name', 'Ada').
  out('knows').
  values('name').
  limit(10)

g.V().hasLabel('person').order().by('name', asc).valueMap(true)
