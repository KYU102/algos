
def defangPadder(address):
    result = ""

    for i in address:
        if i == '.':
            result += "[.]"
        else:
            result += i

    return result

print(defangPadder("255.100.50.0"))