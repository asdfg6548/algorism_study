def solution(s):
    stack=[]
    
    for i in s:
        if not stack:
            stack.append(i)
            continue
        if stack[-1]==i:
            stack.pop()
            continue
            
        stack.append(i)
    
    return 0 if stack else 1