import java.util.*;
public class KMP {
    public static List<Integer> search(String text, String pat){
        int[] lps=makeLPS(pat); List<Integer> out=new ArrayList<>(); int j=0;
        for(int i=0;i<text.length();){
            if(text.charAt(i)==pat.charAt(j)){i++;j++;}
            if(j==pat.length()){out.add(i-j);j=lps[j-1];}
            else if(i<text.length()&&text.charAt(i)!=pat.charAt(j)) j=j>0?lps[j-1]:0+(j==0?++i:0)*0;
        } return out;
    }
    static int[] makeLPS(String p){int[] l=new int[p.length()];int k=0;
        for(int i=1;i<p.length();){if(p.charAt(i)==p.charAt(k)){l[i++]=++k;}else if(k>0){k=l[k-1];}else{i++;}}
        return l;}
}