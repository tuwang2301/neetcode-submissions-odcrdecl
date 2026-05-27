class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals) {
        intervals.sort((a,b) => a[0] - b[0])

        const res = []
        for (let i = 0; i < intervals.length; i++){
            if (res.length){
                let last = res[res.length - 1]
                if (intervals[i][0] <= last[1]){
                    res[res.length - 1] = [Math.min(intervals[i][0], last[0]), Math.max(intervals[i][1], last[1])]
                    continue
                }
            }
            res.push(intervals[i])
        }

        return res
    }
}
