//! Brent's cycle detection.
fn brent_cycle(link: &[usize], start: usize) -> (usize, usize) {
    let mut power = 1;
    let mut lam = 1;
    let mut tortoise = start;
    let mut hare = link[start];
    while tortoise != hare {
        if power == lam {
            tortoise = hare;
            power *= 2;
            lam = 0;
        }
        hare = link[hare];
        lam += 1;
    }
    tortoise = start;
    hare = start;
    for _ in 0..lam {
        hare = link[hare];
    }
    let mut mu = 0;
    while tortoise != hare {
        tortoise = link[tortoise];
        hare = link[hare];
        mu += 1;
    }
    (mu, lam)
}

fn main() {
    let link = [1usize, 2, 3, 4, 3];
    assert_eq!(brent_cycle(&link, 0), (3, 2));
    println!("brent cycle ok");
}
