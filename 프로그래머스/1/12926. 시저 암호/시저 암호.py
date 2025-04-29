def solution(s, n):
    result = ''
    for char in s:
        if char == ' ':
            result += char
        elif char.isupper():
            result += chr((ord(char) - 65 + n) % 26 + 65)
        else:
            result += chr((ord(char) - 97 + n) % 26 + 97)
    return result