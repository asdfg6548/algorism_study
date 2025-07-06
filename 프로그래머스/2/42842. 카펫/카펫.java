class Solution {
    public int[] solution(int brown, int yellow) {
        // 전체 격자 수 = brown + yellow
        int total = brown + yellow;
        
        // yellow의 약수 쌍 (w, h) 탐색
        for (int h = 1; h <= Math.sqrt(yellow); h++) {
            if (yellow % h == 0) {
                int w = yellow / h; // w * h = yellow
                // 갈색 격자 수 확인: 2w + 2h + 4 == brown
                if (2 * w + 2 * h + 4 == brown) {
                    // 가로 >= 세로, 전체 가로 = w + 2, 세로 = h + 2
                    return new int[]{w + 2, h + 2};
                }
            }
        }
        
        // 제한사항 상 답이 항상 존재
        return new int[]{};
    }
}