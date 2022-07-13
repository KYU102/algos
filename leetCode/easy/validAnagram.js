function isAnagram(s, t) {
    let sortedT = t.split("").sort().join()
    let sortedS = s.split("").sort().join()

    if (sortedS === sortedT){
        return true
    }
    else {
        return false
    }
};

console.log(isAnagram("abc", "abcd"))