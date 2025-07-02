import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int[] com:commands) {
            int i=com[0];
            int j=com[1];
            int k=com[2];
            
            ArrayList<Integer> subList=new ArrayList<>();
            for (int idx=i-1; idx<j; idx++){
                subList.add(array[idx]);
            }
            
            Collections.sort(subList);
            answer.add(subList.get(k-1));
            
        }
        
        int[] res=new int[answer.size()];
        for (int i=0; i<answer.size(); i++) {
            res[i]=answer.get(i);
        }
        return res;
    }
}