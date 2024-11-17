def solution(n, words):
    answer = [0,0]
    word_list=[words[0]]   
    
    for i in range(1,len(words)):
        if word_list[-1][-1]==words[i][0] and words[i] not in word_list:
            word_list.append(words[i])
        else:
            answer[0]=(i%n)+1
            answer[1]=(i//n)+ 1
            break

    return answer