def topKFrequent(words,k):
    res = []    
    counter = {}
    arr = []

    for word in words:
        counter[word] = counter.get(word,0)+1
    
    for key, val in counter.items():
        res.append([val,key])

    res.sort(reverse=True)

    for i in range(k):
        arr.append(res[i][1])

    arr.sort()

    return arr

print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"],4))