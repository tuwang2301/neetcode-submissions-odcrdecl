class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = {}
        for(const n of nums){
            freq[n] = (freq[n] || 0) + 1
        }

        const res = Object.keys(freq).sort((a,b) => freq[b] - freq[a])

        return res.slice(0,k)

    }
}
