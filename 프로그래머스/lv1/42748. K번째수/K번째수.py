def solution(array, commands):
    answer = []
    
    for cmd in commands:
        setArray = array[cmd[0] - 1:cmd[1]]
        setArray.sort()
        answer.append(setArray[cmd[2] - 1])
        
    return answer