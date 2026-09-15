fn beautiful_matrix(grid: &[[i32; 5]; 5]) -> i32 {
    for row in 0..5 {
        for column in 0..5 {
            if grid[row][column] == 1 {
                return (row as i32 - 2).abs() + (column as i32 - 2).abs();
            }
        }
    }
    -1
}

fn main() {
    let grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ];
    assert_eq!(beautiful_matrix(&grid), 3);
    println!("263A beautiful matrix ok");
}
