import java.util.*;
import java.io.*;

class Solution {
    static class Word{
        String words;
        int idx;
        public Word(String words, int idx) {
            this.words = words;
            this.idx = idx;
        }
    }
    
    public boolean compare(String a, String b, int n) {
        int notSame = 0;
        for(int i = 0; i < n; i++) {
            if(a.charAt(i) != b.charAt(i)) {
                notSame += 1;
            }
        }
        if(notSame == 1) return true;
        else return false;
    }
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        ArrayList<String> wordsArray = new ArrayList<>(Arrays.asList(words));
        int n = begin.length();
        Queue<Word> q = new ArrayDeque();
        boolean visited[] = new boolean[words.length];
        if(!wordsArray.contains(target)) return 0;
        
        q.add(new Word(begin, 0));
        while(!q.isEmpty()) {
            Word now = q.poll();
            if(now.words.equals(target)) {
                answer = now.idx;
            }
            for(int i = 0; i < words.length; i++) {
                if(visited[i]) continue;
                if(compare(now.words, words[i], n)) {
                    q.add(new Word(words[i], now.idx + 1));
                    visited[i] = true;
                }
            }
        }
        
        return answer;
    }
}