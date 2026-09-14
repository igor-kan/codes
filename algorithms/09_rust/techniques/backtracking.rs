//! Backtracking: subsets and permutations in Rust.

pub fn subsets(nums: &[i64]) -> Vec<Vec<i64>> {
    let mut res = Vec::new();
    let mut cur = Vec::new();
    fn dfs(nums: &[i64], start: usize, cur: &mut Vec<i64>, res: &mut Vec<Vec<i64>>) {
        res.push(cur.clone());
        for i in start..nums.len() {
            cur.push(nums[i]);
            dfs(nums, i + 1, cur, res);
            cur.pop();
        }
    }
    dfs(nums, 0, &mut cur, &mut res);
    res
}

pub fn permutations(nums: &[i64]) -> Vec<Vec<i64>> {
    let mut res = Vec::new();
    let mut cur = Vec::new();
    let mut used = vec![false; nums.len()];
    fn dfs(nums: &[i64], cur: &mut Vec<i64>, used: &mut Vec<bool>, res: &mut Vec<Vec<i64>>) {
        if cur.len() == nums.len() {
            res.push(cur.clone());
            return;
        }
        for i in 0..nums.len() {
            if used[i] {
                continue;
            }
            used[i] = true;
            cur.push(nums[i]);
            dfs(nums, cur, used, res);
            cur.pop();
            used[i] = false;
        }
    }
    dfs(nums, &mut cur, &mut used, &mut res);
    res
}

fn main() {
    assert_eq!(subsets(&[1, 2, 3]).len(), 8);
    assert_eq!(permutations(&[1, 2, 3]).len(), 6);
    println!("[Rust Backtracking] Subsets (8) + permutations (6) verified.");
}
