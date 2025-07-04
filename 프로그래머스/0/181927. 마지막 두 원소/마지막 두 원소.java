class Solution {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        // 새로운 배열 생성 (길이 n+1)
        int[] answer = new int[n + 1];
        
        // num_list를 answer로 복사
        System.arraycopy(num_list, 0, answer, 0, n);
        
        // 마지막 두 요소 비교
        if (num_list[n - 1] > num_list[n - 2]) {
            answer[n] = num_list[n - 1] - num_list[n - 2];
        } else {
            answer[n] = 2 * num_list[n - 1];
        }
        
        return answer;
    }
}