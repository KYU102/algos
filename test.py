from string import ascii_lowercase


def test(message, rotation = 4):
    rotated = ascii_lowercase[rotation:] + ascii_lowercase[:rotation]
    cipher = {o: n for o, n in zip(ascii_lowercase,rotated)}

    encoded = []
    for char in message.lower():
        if char in cipher:
            encoded.append(cipher[char])
        else:
            encoded.append(char)

    return''.join(encoded)

print(test('SUPER'))