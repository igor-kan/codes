def kmp(text, pat)
  lps = make_lps(pat); matches = []; j = 0
  text.chars.each_with_index do |c, i|
    j = lps[j-1] while j > 0 && c != pat[j]
    j += 1 if c == pat[j]
    if j == pat.length; matches << i-j+1; j = lps[j-1]; end
  end
  matches
end
def make_lps(p)
  lps = [0]*p.length; k = 0
  (1...p.length).each { |i|
    k = lps[k-1] while k>0 && p[i]!=p[k]
    k += 1 if p[i]==p[k]; lps[i]=k }
  lps
end