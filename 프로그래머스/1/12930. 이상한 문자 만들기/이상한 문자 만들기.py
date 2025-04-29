def solution(s):
    # 단어 단위로 처리
    words = s.split(' ')
    result = []
    
    for word in words:
        new_word = ''
        for i, char in enumerate(word):
            # 짝수 인덱스: 대문자, 홀수 인덱스: 소문자
            new_word += char.upper() if i % 2 == 0 else char.lower()
        result.append(new_word)
    
    # 단어들을 공백으로 연결
    return ' '.join(result)