import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int N = commands.length;
        int[] answer = new int[N];
        
        for(int i = 0; i < N; i++) {
            int s = commands[i][0];
            int e = commands[i][1];
            int k = commands[i][2];
            
            int[] new_arr = Arrays.copyOfRange(array, s - 1, e);
            Arrays.sort(new_arr);
            answer[i] = new_arr[k - 1];
        }
        return answer;
    }
}