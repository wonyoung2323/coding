import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int endTime = 0;
        int idx = 0;
        int cnt = 0;
        
        PriorityQueue<int[]> q = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);
        while(true) {
            if(cnt == jobs.length) break;

            while(idx < jobs.length && jobs[idx][0] <= endTime) {
                q.add(jobs[idx++]);
            }
            if(q.isEmpty()) {
                endTime = jobs[idx][0];
            } else {
                int[] tmp = q.poll();
                answer += endTime - tmp[0] + tmp[1];
                endTime += tmp[1];  
                cnt++;
                System.out.println(cnt);
            }
        }
        
        return answer / jobs.length;
    }
}