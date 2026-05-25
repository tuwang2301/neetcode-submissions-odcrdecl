class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals) {
        const res = []

        const sorted = intervals.sort((a,b) => a[0] - b[0])
        console.log(sorted)
        for (let i = 0; i < intervals.length; i++){
            const [s1,e1] = intervals[i]
            let check = false
            for (let j = 0; j < res.length; j++){
                const [s2,e2] = res[j]
                console.log(s1,e1, s2,e2)
                if ((s1 <= s2 && s2 <= e1) ||
                    (s2 <= s1 && s1 <= e2)){
                    check = true
                    res[j] = [Math.min(s1,s2), Math.max(e1, e2)]
                }
            }

            if (!check){
                res.push([s1,e1])
            }
        }

        return res


    }
}
