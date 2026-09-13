const gcd = (a,b) => b===0 ? a : gcd(b, a%b);
const lcm = (a,b) => a/gcd(a,b)*b;
module.exports = { gcd, lcm };