#include <cstdint>
uint64_t gcd(uint64_t a, uint64_t b){ return b?gcd(b,a%b):a; }
uint64_t lcm(uint64_t a, uint64_t b){ return a/gcd(a,b)*b; }
uint64_t powmod(uint64_t b, uint64_t e, uint64_t m){
    uint64_t r=1; for(b%=m;e;e>>=1){if(e&1)r=r*b%m;b=b*b%m;} return r;
}