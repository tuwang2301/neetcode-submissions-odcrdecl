class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const set = new Set(nums)
        let res = 0

        for(const n of nums){
            if(!set.has(n-1)){
                let count = 0
                while (set.has(n+count)){
                    count += 1
                }
                res = Math.max(res, count)
            }
        }
        return res
    }
}
