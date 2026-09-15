package main

import "fmt"

var faces = map[string]int{
	"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20,
}

func antonAndPolyhedrons(names []string) int {
	total := 0
	for _, name := range names {
		total += faces[name]
	}
	return total
}

func main() {
	if antonAndPolyhedrons([]string{"Icosahedron", "Cube", "Tetrahedron"}) != 30 {
		panic("polyhedrons failed")
	}
	fmt.Println("785A anton and polyhedrons ok")
}
