const FACES = { Tetrahedron: 4, Cube: 6, Octahedron: 8, Dodecahedron: 12, Icosahedron: 20 };

function antonAndPolyhedrons(names) {
  return names.reduce((acc, name) => acc + FACES[name], 0);
}

if (require.main === module) {
  if (antonAndPolyhedrons(["Icosahedron", "Cube", "Tetrahedron"]) !== 30) throw new Error("polyhedrons failed");
  console.log("785A anton and polyhedrons ok");
}
