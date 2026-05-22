class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const check = {'}': '{', ']': '[', ')': '('}
        const set = new Set(Object.keys(check))
        const stack = []
        for (const c of s){
            if (set.has(c) && stack){
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
