import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> res=new ArrayList<>();
        int len=answers.length;
        
        int cnt1=0;
        int cnt2=0;
        int cnt3=0;
        
        int arr1[]={1,2,3,4,5};
        int arr2[]={2,1,2,3,2,4,2,5};
        int arr3[]={3,3,1,1,2,2,4,4,5,5};
        
        for (int i=0; i<len; i++) {
            if (answers[i]==arr1[i%5]) {
                cnt1+=1;
            }
            if (answers[i]==arr2[i%8]) {
                cnt2+=1;
            }
            if (answers[i]==arr3[i%10]) {
                cnt3+=1;
            }
            
        }
        
        int max=Math.max(cnt1,Math.max(cnt2,cnt3));
        
        if (max==cnt1) {
            res.add(1);
        }
        
        if (max==cnt2) {
            res.add(2);
        }
        
        if (max==cnt3) {
            res.add(3);
        }
        
        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}