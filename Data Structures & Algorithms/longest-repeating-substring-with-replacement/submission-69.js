class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const map = new Map()
        let l = 0
        let longest = 0

        for (let r = 0; r < s.length; r++){
            map.set(s[r], (map.get(s[r]) || 0) + 1)
            console.log(map)
            while (true){
                const max_freq = Math.max(...map.values()) 
                const check = max_freq >= (r-l+1) - k
                if (check){
                    break
                }else {
                    map.set(s[l], (map.get(s[l]) || 0) - 1)
                    l++
                }
            }

            longest = Math.max(longest, r-l+1)

        }
        return longest
    }
}
