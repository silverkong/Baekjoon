def solution(s):
    answer = 0
    sList = list(s)
    
    for _ in range(len(s)):
        temp = []
        for i in range(len(sList)):
            if temp:
                if sList[i] == ')' and temp.pop() == '(':
                    continue
                elif sList[i] == '}' and temp.pop() == '{':
                    continue
                elif sList[i] == ']' and temp.pop() == '[':
                    continue
                else:
                    temp.append(sList[i])
            else:
                temp.append(sList[i])
        if len(temp) == 0:
            answer += 1
        sList.append(sList.pop(0))
        
    return answer