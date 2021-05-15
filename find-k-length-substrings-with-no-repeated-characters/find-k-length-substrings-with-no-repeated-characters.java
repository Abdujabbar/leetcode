class Solution {
    public int numKLenSubstrNoRepeats(String str, int k) {
        Map<Character, Integer> counter = new HashMap<>();
        int ans = 0;

        for (int i = 0; i < str.length(); i++) {
            counter.put(str.charAt(i), counter.getOrDefault(str.charAt(i), 0) + 1);
            
            if (i >= k) {
                counter.put(str.charAt(i - k), counter.get(str.charAt(i - k)) - 1);
                if(counter.get(str.charAt(i - k)) == 0){
                    counter.remove(str.charAt(i - k));
                }

            }

            if (counter.size() == k) {
                ans++;
            }

        }

        return ans;
    }
}