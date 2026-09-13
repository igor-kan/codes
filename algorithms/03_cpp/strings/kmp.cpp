#include <string>
#include <vector>
std::vector<int> kmp(const std::string& text, const std::string& pat){
    int m=pat.size(); std::vector<int> lps(m,0),out;
    for(int i=1,k=0;i<m;){ if(pat[i]==pat[k])lps[i++]=++k; else if(k)k=lps[k-1]; else i++; }
    for(int i=0,j=0;i<(int)text.size();){
        if(text[i]==pat[j]){i++;j++;}
        if(j==m){out.push_back(i-j);j=lps[j-1];}
        else if(i<(int)text.size()&&text[i]!=pat[j]) j=j?lps[j-1]:0,i+=!j;
    } return out;
}