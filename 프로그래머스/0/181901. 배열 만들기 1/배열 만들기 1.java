import java.util.*;
class Solution {
    public int[] solution(int n, int k) {
        ArrayList<Integer> list= new ArrayList<>();
        for (int i=1; i<n+1; i++) {
            if (i%k==0){
                list.add(i);
            }
        }
        
        int len=list.size();
        int[] answer=new int[len];
        for (int i=0; i<len; i++) {
            answer[i]=list.get(i);
        }
        
        return answer;
    }
}