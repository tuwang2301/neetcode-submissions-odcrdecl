class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        const stack = []
        const res = new Array(temperatures.length).fill(0)
        for (let i = 0; i < temperatures.length; i++){
            while (stack.length > 0 && temperatures[i] > stack[stack.length - 1][1]){
                const [index, temp] = stack.pop()
                res[index] = i - index
            }

            stack.push([i, temperatures[i]])
        }

        return res
    }
}
