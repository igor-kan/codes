// Updating and dropping properties/vertices.
g.V().has('name', 'Ada').property('lastActive', System.currentTimeMillis())

g.V().has('name', 'Ada').properties('obsolete').drop().iterate()
g.V().has('name', 'Temp').drop().iterate()
