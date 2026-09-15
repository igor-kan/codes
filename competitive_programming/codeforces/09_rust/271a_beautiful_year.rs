use std::collections::HashSet;

fn beautiful_year(year: i32) -> i32 {
    let mut current = year;
    loop {
        current += 1;
        let digits: HashSet<char> = current.to_string().chars().collect();
        if digits.len() == 4 {
            return current;
        }
    }
}

fn main() {
    assert_eq!(beautiful_year(1987), 2013);
    assert_eq!(beautiful_year(2013), 2014);
    println!("271A beautiful year ok");
}
