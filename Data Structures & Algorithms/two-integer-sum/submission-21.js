class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map()
        for (let i = 0; i < nums.length; i++){
            const check = target - nums[i]
            if (map.has(check)){
                return [map.get(check), i]
            }
            map.set(nums[i], i)
        }
        return []
    }
}
