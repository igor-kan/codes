function kmp(text, pat) {
  const lps = makeLPS(pat), matches = []; let j=0;
  for (let i=0;i<text.length;) {
    if (text[i]===pat[j]) { i++; j++; }
    if (j===pat.length) { matches.push(i-j); j=lps[j-1]; }
    else if (i<text.length&&text[i]!==pat[j]) j = j ? lps[j-1] : (i++, 0);
  }
  return matches;
}
function makeLPS(p) {
  const lps=new Array(p.length).fill(0); let k=0;
  for (let i=1;i<p.length;) { if(p[i]===p[k]){lps[i++]=++k;}else if(k){k=lps[k-1];}else{i++;} }
  return lps;
}
module.exports = { kmp };