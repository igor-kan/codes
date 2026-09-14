function subsets(nums) {
  const res = [];
  const cur = [];
  function dfs(i) {
    if (i === nums.length) { res.push([...cur]); return; }
    cur.push(nums[i]);
    dfs(i + 1);
    cur.pop();
    dfs(i + 1);
  }
  dfs(0);
  return res;
}

function permutations(nums) {
  const res = [];
  const used = new Array(nums.length).fill(false);
  const cur = [];
  function dfs() {
    if (cur.length === nums.length) { res.push([...cur]); return; }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      cur.push(nums[i]);
      dfs();
      cur.pop();
      used[i] = false;
    }
  }
  dfs();
  return res;
}

module.exports = { subsets, permutations };

if (require.main === module) {
  if (subsets([1, 2, 3]).length !== 8) throw new Error("subsets count failed");
  if (permutations([1, 2, 3]).length !== 6) throw new Error("permutations count failed");
  console.log("[JavaScript Backtracking] subsets & permutations verified");
}
