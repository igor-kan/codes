#include <stdio.h>
#include <string.h>
void sieve(int n){
    char is_prime[n+1]; memset(is_prime,1,sizeof(is_prime));
    is_prime[0]=is_prime[1]=0;
    for(int i=2;(long long)i*i<=n;i++)
        if(is_prime[i]) for(int j=i*i;j<=n;j+=i) is_prime[j]=0;
    for(int i=2;i<=n;i++) if(is_prime[i]) printf("%d ",i);
}
