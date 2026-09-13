public class MathUtils {
    public static long gcd(long a, long b){ return b==0?a:gcd(b,a%b); }
    public static long lcm(long a, long b){ return a/gcd(a,b)*b; }
    public static long powMod(long base, long exp, long mod){
        long r=1; base%=mod;
        for(;exp>0;exp>>=1){if((exp&1)==1)r=r*base%mod; base=base*base%mod;} return r;
    }
}