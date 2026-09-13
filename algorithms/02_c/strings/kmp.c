#include <stdio.h>
#include <string.h>
void compute_lps(const char *p, int m, int *lps){
    int k=0; lps[0]=0;
    for(int i=1;i<m;){
        if(p[i]==p[k]) lps[i++]=++k;
        else if(k) k=lps[k-1];
        else lps[i++]=0;
    }
}
void kmp(const char *text, const char *pat){
    int n=strlen(text), m=strlen(pat), lps[m];
    compute_lps(pat,m,lps);
    int i=0,j=0;
    while(i<n){
        if(text[i]==pat[j]){i++;j++;}
        if(j==m){printf("Found at %d\n",i-j);j=lps[j-1];}
        else if(i<n&&text[i]!=pat[j]) j=j?lps[j-1]:0,i+=!j;
    }
}
