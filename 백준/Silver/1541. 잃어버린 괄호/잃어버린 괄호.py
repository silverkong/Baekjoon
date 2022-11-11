import sys

# 계산할 식 입력 받기 : - 기준으로 나누어야 최소값
calList = sys.stdin.readline().rstrip().split('-')
# 결과 값 선언
result = 0

# 계산
for c in calList[0].split('+'):
    result += int(c)

for c in calList[1:]:
    for i in c.split('+'):
        result -= int(i)
 
print(result)