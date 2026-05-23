class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let res = ""
        for(const str of strs){
            res += str.length + "#" + str
        }

        console.log(res)

        return res
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = []
        let i = 0
        while (i < str.length){
            let countStr = ""

            while (str[i] != "#"){
                countStr += str[i]
                i++
            }
            
            i++

            const count = Number(countStr)
            res.push(str.substring(i, i + count))

            i+=count

        }

        return res
    }
}
