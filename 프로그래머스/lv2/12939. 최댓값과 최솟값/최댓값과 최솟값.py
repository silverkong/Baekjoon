def solution(s):
    answer = ''
    numList = list(map(int, s.split()))
    answer += str(min(numList)) + ' '
    answer += str(max(numList))
    return answer