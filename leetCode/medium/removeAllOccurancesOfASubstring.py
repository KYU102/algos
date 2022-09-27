from os import remove


def removeOccurances(s,part):
        i = 0
        change = False

        while i < len(s)-len(part)+1:
            if s[i:i+len(part)] == part:
                s = s[:i] + s[i+len(part):]
                change = True
            else:
                i+=1
            
            if change:
                i = 0
                change = False
        return s

print(removeOccurances("daabcbaabcbc",'abc'))