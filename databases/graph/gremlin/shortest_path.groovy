// Shortest path with repeat/until, BFS semantics.
g.V().has('name', 'Ada').
  repeat(out('knows').simplePath()).
    until(has('name', 'Grace')).
  path().
  by('name').
  limit(1)
