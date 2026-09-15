// Catalan numbers by the recurrence.
const catalan = new Array(11).fill(0);
catalan[0] = 1;
for (let i = 1; i <= 10; i += 1) {
  let sum = 0;
  for (let j = 0; j < i; j += 1) sum += catalan[j] * catalan[i - 1 - j];
  catalan[i] = sum;
}
if (catalan[5] !== 42 || catalan[10] !== 16796) throw new Error("wrong Catalan numbers");
console.log(`catalan(10)=${catalan[10]}`);
