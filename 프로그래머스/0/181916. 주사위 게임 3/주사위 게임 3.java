import java.util.*;
class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] arr={a,b,c,d};
        Arrays.sort(arr);
        
        // 경우 1:네 숫자 모두 같음
        if (arr[0]==arr[3]) {
            return 1111*arr[0];
        }
        //경우 2: 세 숫자 같음
        else if (arr[0] == arr[2]) {
            return (10 * arr[0] + arr[3]) * (10 * arr[0] + arr[3]);
        }
        else if (arr[1] == arr[3]) {
            return (10 * arr[3] + arr[0]) * (10 * arr[3] + arr[0]);
        }
        //경우 3: 2개 2개 같음
        else if(arr[0]==arr[1] && arr[2]==arr[3]) {
            return ((arr[0]+arr[2])*Math.abs(arr[0]-arr[2]));
        }
        //경우 4: 두 숫자 같고 나머지 모두 다름
        else if (arr[0]==arr[1]) {
            return(arr[2]*arr[3]);
        }
        else if (arr[1]==arr[2]) {
            return(arr[0]*arr[3]);
        }
        else if (arr[2]==arr[3]) {
            return(arr[0]*arr[1]);
        }
        //경우 5: 모두 서로 다른 경우
        else {
            return(arr[0]);
        }
    }
}