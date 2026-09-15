function activitySelection(activities) {
  const sorted = [...activities].sort((a, b) => a.finish - b.finish);
  const chosen = [];
  let last = -Infinity;
  for (const activity of sorted) {
    if (activity.start >= last) {
      chosen.push(activity);
      last = activity.finish;
    }
  }
  return chosen;
}

module.exports = { activitySelection };

if (require.main === module) {
  const acts = [
    { start: 1, finish: 4 }, { start: 3, finish: 5 }, { start: 0, finish: 6 },
    { start: 5, finish: 7 }, { start: 3, finish: 9 }, { start: 5, finish: 9 },
    { start: 6, finish: 10 }, { start: 8, finish: 11 }, { start: 8, finish: 12 },
    { start: 2, finish: 14 }, { start: 12, finish: 16 },
  ];
  const chosen = activitySelection(acts);
  if (chosen.length !== 4) throw new Error("activity selection failed");
  console.log("[JavaScript Activity Selection] maximum set verified");
}
