def solution(s):
    answer = []
    s = s.split(" ")

    for word in s:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
            
        #공백 처리
        else:
            answer.append(word)

    return " ".join(answer)