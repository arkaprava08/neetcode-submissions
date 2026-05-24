class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(k, Collections.reverseOrder());
        ArrayList<Integer> out = new ArrayList<>();




        for(int i=0; i<k; i++) {
            maxHeap.add(nums[i]);
        }
        out.add(maxHeap.peek());

        int j=k-1;
        for (int i=1; i<nums.length-k+1; i++) {
            maxHeap.remove(nums[i-1]);
            maxHeap.add(nums[i+k-1]);
            out.add(maxHeap.peek());
        }

        return out.stream().mapToInt(i -> i).toArray(); 
    }
}
