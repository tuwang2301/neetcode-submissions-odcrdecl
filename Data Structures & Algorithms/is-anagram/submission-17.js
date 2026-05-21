class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const check1 = new Array(26).fill(0)
        const check2 = new Array(26).fill(0)

        for (const c of s){
            check1[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
        }

        for (const c of t){
            check2[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
        }

        for (let i = 0; i < check1.length; i++){
            if (check1[i] !== check2[i]){
                return false
            }
        }
        return true
    }
}
