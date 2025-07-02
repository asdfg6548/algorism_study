class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length];
        
        for (int i=0; i<arr.length; i++) {
            int num1=arr[i];
            if (num1 >=50 && num1%2==0 ){
                answer[i]=num1/2;
            }
            else if (num1 <50 && num1%2==1) {
                answer[i]=num1*2;
            }
            else{
                answer[i]=arr[i];
            }
        }
        
        return answer;
    }
}