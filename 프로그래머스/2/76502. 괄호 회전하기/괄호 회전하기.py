from collections import deque

def solution(s):
    answer=0
    queue=deque(s)
    
    for i in range(len(queue)):
        stack=[]
        
        for q in queue:
            if stack:
                if stack[-1]=='[' and q==']':
                    stack.pop()
                elif stack[-1]=='{' and q=='}':
                    stack.pop()
                elif stack[-1]=='(' and q==')':
                    stack.pop()
                else:
                    stack.append(q)
            else:
                stack.append(q)
        
        if len(stack)==0:
            answer+=1
        queue.append(queue.popleft())
    
    return answer
