fn anton_and_polyhedrons(names: &[&str]) -> i32 {
    names.iter().map(|name| match *name {
        "Tetrahedron" => 4,
        "Cube" => 6,
        "Octahedron" => 8,
        "Dodecahedron" => 12,
        "Icosahedron" => 20,
        _ => 0,
    }).sum()
}

fn main() {
    assert_eq!(anton_and_polyhedrons(&["Icosahedron", "Cube", "Tetrahedron"]), 30);
    println!("785A anton and polyhedrons ok");
}
