function theatreSquare(n, m, a) {
  return Math.ceil(n / a) * Math.ceil(m / a);
}

if (require.main === module) {
  if (theatreSquare(6, 6, 4) !== 4 || theatreSquare(1, 1, 1) !== 1) throw new Error("theatre square failed");
  console.log("1A theatre square ok");
}
