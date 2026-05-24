class Solution {
    public int lastStoneWeight(int[] stones) {
        if(stones.length == 1)
            return stones[0];

        PriorityQueue<Integer> queue = new PriorityQueue<Integer>(Collections.reverseOrder());
        
        for(int i=0; i<stones.length; i++) {
            queue.add(stones[i]);
        }

        while(queue.size() > 1) {
            int val = (queue.remove()-queue.remove());
            val = (val<0) ? val*-1 : val;
            queue.add(val);
        }

        return queue.remove();
    }
}
