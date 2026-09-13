import java.util.*;
public class BFS {
    public static List<Integer> bfs(Map<Integer,List<Integer>> g, int src){
        Set<Integer> vis=new HashSet<>(); Queue<Integer> q=new LinkedList<>();
        List<Integer> order=new ArrayList<>(); q.add(src);
        while(!q.isEmpty()){int u=q.poll(); if(vis.add(u)){order.add(u); q.addAll(g.getOrDefault(u,List.of()));}}
        return order;
    }
}