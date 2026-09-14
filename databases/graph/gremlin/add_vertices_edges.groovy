// Mutating a graph: add vertices and edges.
def ada = g.addV('person').property('name', 'Ada').property('born', 1815).next()
def alan = g.addV('person').property('name', 'Alan').next()

g.addE('influenced').from(ada).to(alan).property('year', 1936).iterate()

g.V(ada).outE('influenced').inV().values('name').toList()
