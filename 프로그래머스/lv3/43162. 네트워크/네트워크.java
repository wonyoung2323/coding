import java.util.*;
import java.io.*;

class Solution {
    public void dfs(int now, int[][] computers, int n) {
        for(int i = 0; i < n; i++) {
            if(computers[now][i] == 1) {
                computers[now][i] = 0;
                computers[i][now] = 0;
                dfs(i, computers, n);
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        for(int i = 0; i < n; i++) {
            if (computers[i][i] == 1) {
                computers[i][i] = 0;
                answer += 1;
                dfs(i, computers, n);
            }
        }
        
        return answer;
    }
}