class Solution {
    private int maxDungeons = 0; // 최대 던전 수
    
    public int solution(int k, int[][] dungeons) {
        boolean[] used= new boolean[dungeons.length];
        exploreDungeons(k,0,used,dungeons);
        return maxDungeons;
    }
    
    private void exploreDungeons(int k, int count, boolean[] used,int[][] dungeons) {
        // 최대 던전 수 갱신
        maxDungeons=Math.max(maxDungeons,count);
        
        // 모든 던전 순회
        for(int i=0; i<dungeons.length; i++) {
            if(!used[i] && k>=dungeons[i][0]) {
                used[i]=true;
                exploreDungeons(k-dungeons[i][1],count+1,used,dungeons);
                used[i]=false;
            }
        }
    }
}