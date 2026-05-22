class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        let check = false
        const permutation = new Set(s1)

        for (let i = 0; i < s2.length; i++){
            if (permutation.has(s2[i])){
                const sub = s2.substring(i, i + s1.length)
                const check1 = new Array(26).fill(0)
                const check2 = new Array(26).fill(0)

                for (const s of s1){
                    check1[s.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
                }

                for (const s of sub){
                    check2[s.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
                }

                check = true
                for (let i = 0; i < check1.length; i++){
                    if (check1[i] != check2[i]){
                        check = false
                        break
                    }
                }

                if (check){
                    return true
                }
            }
        }
        return check
    }
}
