function longestCommonPrefix (strs){
    commonPrefix = ""
    for (let i = 0; i < strs[0].length; i++) {
        for (let j = 0; j < strs.length; j++) {
            if (strs[i][j] === strs[0][i]){
                commonPrefix += strs[0][i]
            }
        }
        
    }

    return commonPrefix

}

console.log(longestCommonPrefix(["flower","flow","flight"]))