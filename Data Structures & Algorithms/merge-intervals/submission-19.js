class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals) {
        const res = []

        intervals.sort((a,b) => a[0] - b[0])

        for (let i = 0; i < intervals.length; i++){
            const [s2,e2] = intervals[i]
            if (res.length >= 1){
                const [s1,e1] = res[res.length-1]
                if (s2 <= e1){
                    res[res.length - 1] = [Math.min(s1,s2), Math.max(e1,e2)]
                    continue
                }
            }
            res.push([s2,e2])
        }

        return res


    }
}
