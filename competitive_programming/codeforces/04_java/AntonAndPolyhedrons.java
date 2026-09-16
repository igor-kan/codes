import java.util.*;

// Codeforces 785A - Anton and Polyhedrons.
public class AntonAndPolyhedrons {
    static int antonAndPolyhedrons(String[] names) {
        Map<String, Integer> faces = new HashMap<>();
        faces.put("Tetrahedron", 4);
        faces.put("Cube", 6);
        faces.put("Octahedron", 8);
        faces.put("Dodecahedron", 12);
        faces.put("Icosahedron", 20);
        int total = 0;
        for (String name : names) total += faces.get(name);
        return total;
    }

    public static void main(String[] args) {
        assert antonAndPolyhedrons(new String[] {"Icosahedron", "Cube", "Tetrahedron"}) == 30;
        System.out.println("785A anton and polyhedrons ok");
    }
}
