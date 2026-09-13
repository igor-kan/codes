import java.util.*;
public class Dijkstra {
    public static Map<Integer,Long> dijkstra(Map<Integer,List<int[]>> g, int src){
        Map<Integer,Long> dist=new HashMap<>(); dist.put(src,0L);
        PriorityQueue<long[]> pq=new PriorityQueue<>(Comparator.comparingLong(a->a[0]));
        pq.offer(new long[]{0,src});
        while(!pq.isEmpty()){long[] cur=pq.poll(); int u=(int)cur[1]; long d=cur[0];
            if(d>dist.getOrDefault(u,Long.MAX_VALUE)) continue;
            for(int[] e:g.getOrDefault(u,List.of())){long nd=d+e[1];
                if(nd<dist.getOrDefault(e[0],Long.MAX_VALUE)){dist.put(e[0],nd); pq.offer(new long[]{nd,e[0]});}}}
        return dist;
    }
}