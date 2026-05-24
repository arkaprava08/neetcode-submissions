class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(k, Collections.reverseOrder());
        ArrayList<Integer> out = new ArrayList<>();



        for (int i=0; i<nums.length-k+1; i++) {
            if(i==0) {
                for(int j=0; j<k; j++) {
                    maxHeap.add(nums[j]);
                }
            } else {
                maxHeap.remove(nums[i-1]);
                maxHeap.add(nums[i+k-1]);
            }
            out.add(maxHeap.peek());
        }

        return out.stream().mapToInt(i -> i).toArray(); 
    }
}
