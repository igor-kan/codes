function sieve(n) {
  const is = new Uint8Array(n+1).fill(1); is[0]=is[1]=0;
  for (let i=2;i*i<=n;i++) if(is[i]) for(let j=i*i;j<=n;j+=i) is[j]=0;
  return [...is].flatMap((v,i)=>v?[i]:[]);
}
module.exports = { sieve };