function beautifulYear(year) {
  let current = year;
  while (true) {
    current += 1;
    if (new Set(String(current)).size === 4) return current;
  }
}

if (require.main === module) {
  if (beautifulYear(1987) !== 2013 || beautifulYear(2013) !== 2014) throw new Error("beautiful year failed");
  console.log("271A beautiful year ok");
}
