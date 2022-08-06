

def remove(s):
    counts = {}
    result = []
    answer = ""


    for letter in s:
        if letter not in counts:
            result += letter
        counts[letter] = counts.get(letter, 0) + 1
    
    result.sort()
    for i in result:
        answer += i
    
    return answer

print(remove("cbacdcbc"))