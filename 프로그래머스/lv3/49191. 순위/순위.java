import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        List<List<Integer>> win = new ArrayList();
        List<List<Integer>> lose = new ArrayList();
        
        for(int i = 0; i < n + 1; i++) {
            win.add(new ArrayList());
            lose.add(new ArrayList());
        }
        
        for(int[] result: results) {
            int a = result[0];
            int b = result[1];
            win.get(a).add(b);
            lose.get(b).add(a);
        }
        
        for(int i = 1; i < n + 1; i++) {
            boolean visited[] = new boolean[n + 1];
            int count = 0;
            Queue<Integer> q = new ArrayDeque();
            q.add(i);
            visited[0] = visited[i] = true;
            
            while(!q.isEmpty()){
                int now = q.poll();
                for(int nodes = 0; nodes < win.get(now).size(); nodes++) {
                    if(visited[win.get(now).get(nodes)]) continue;
                    visited[win.get(now).get(nodes)] = true;
                    count += 1;
                    q.add(win.get(now).get(nodes));
                }
            }
            
            q.add(i);
            while(!q.isEmpty()){
                int now = q.poll();
                for(int nodes = 0; nodes < lose.get(now).size(); nodes++) {
                    if(visited[lose.get(now).get(nodes)]) continue;
                    visited[lose.get(now).get(nodes)] = true;
                    count += 1;
                    q.add(lose.get(now).get(nodes));
                }
            }
            
            if(count == n - 1) answer += 1;
        }
        
        return answer;
    }
}