import java.util.*;
class Solution {
    public long solution(int a, int b) {
        long answer=0;
        // a ⊕ b: 문자열로 붙여서 숫자로 변환
        String concat = String.valueOf(a) + String.valueOf(b);
        long concatValue = Long.parseLong(concat);
        
        // 2 * a * b
        long productValue = 2L * a * b;
        
        
        if (concatValue>=productValue) {
            answer=concatValue;
        }
        else {
            answer=productValue;
        }
        
        return answer;
    }
}