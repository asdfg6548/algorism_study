import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int len=sizes.length;
        int answer = 0;
        
        // 명함을 돌릴 수 있으므로 큰 값을 가로에 작은 값을 세로에
        ArrayList<Integer> garo = new ArrayList<>();
        ArrayList<Integer> sero = new ArrayList<>();
        
        for (int i=0; i<len; i++) {
            if (sizes[i][0]>=sizes[i][1]){
                garo.add(sizes[i][0]);
                sero.add(sizes[i][1]);
            }
            else{
                garo.add(sizes[i][1]);
                sero.add(sizes[i][0]);
            }
        }
        answer=Collections.max(garo)* Collections.max(sero);
        return answer;
    }
}