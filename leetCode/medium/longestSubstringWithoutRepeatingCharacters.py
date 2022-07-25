


def lengthOfLongestSubstring(str):

    count = 1
    max = 1
    
    for startPoint in str:
        for compare in range(1, len(str)):
            
            if startPoint != str[compare]:
                count = count + 1
            else:
                if count > max:
                    max = count
                count = 0
                break
    
    return max



print(lengthOfLongestSubstring("pwwkew"))