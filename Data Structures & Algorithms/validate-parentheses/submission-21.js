class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const check = {'}': '{', ']': '[', ')': '('}
        const stack = []
        for (const c of s){
            if (c in check){
                const open = stack.pop()
                if (open !== check[c]){
                    return false
                }
            }else {
                stack.push(c)
            }
        }

        return stack.length === 0
    }
}
