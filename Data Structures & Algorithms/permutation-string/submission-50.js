class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if (s1.length > s2.length){
            return false
        }

        const permutation = new Array(26).fill(0)
        const check = new Array(26).fill(0)

        for (let i = 0; i < s1.length; i++){
            permutation[s1.charCodeAt(i) - 97]++
            check[s2.charCodeAt(i) - 97]++
        }

        function match(arr1, arr2){
            for (let i = 0; i < arr1.length; i++){
                if (arr1[i] !== arr2[i]){
                    return false
                }
            }
            return true
        }

        if (match(permutation, check)){
            return true
        }

        for (let l = 0; l < s2.length - s1.length; l++){
            check[s2.charCodeAt(l) - 97]--
            check[s2.charCodeAt(l+s1.length) - 97]++

            if (match(permutation, check)){
                return true
            }
        }

        return false
        
    }
}
