def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        filltered=''.join(i for i in skill_tree if i in skill)
        if skill.startswith(filltered):
            answer+=1

    return answer