class Solution {
    public int solution(String number) {
        int answer = 0;
        int sum=0;
        
        // 각 자리 숫자의 합 계산
        for (char c : number.toCharArray()) {
            sum += c - '0'; // 문자 '0'~'9'를 숫자로 변환 (아스키코드)
        }
        
        answer=sum%9;
        
        return answer;
    }
}