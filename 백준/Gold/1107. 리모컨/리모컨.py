import sys

# 현재 채널
now = 100
# 이동할 채널
N = input()
# 고장난 버튼의 개수
M = int(input())

# 채널 이동 횟수
move_ch = abs(100 - int(''.join(map(str, N))))

# 현재 채널과 같은지 확인
def ch100(N):
    if N == '100':
        print(0)
        sys.exit(0) # 여기서 코드 종료

# 고장난 버튼이 0개 일 때,
if M == 0:
    ch100(N)
    # 100과 인접하면 +, -로만 이동
    if move_ch < len(N):
        print(move_ch)
        sys.exit(0)
    else:
        print(len(N))
        sys.exit(0)

# 고장난 버튼 집합
btn = set(sys.stdin.readline().split())

# 만약 고장난 버튼이 10개라면 +, -로만 채널 이동
if M == 10:
    ch100(N)
    print(move_ch)
    sys.exit(0)

# 입력한 채널이 100이라면
ch100(N)

# 최소 채널
lowCh = -1
# 최대 채널
highCh = 500001
# 이동할 채널 정수화
ch = int(''.join(map(str, N)))

# 입력 채널 번호에 해당하는 버튼이 모두 정상일 때
if len(set(N) & btn) == 0:
    print(min(move_ch, len(N)))
    sys.exit(0)

# 이동할 채널보다 작은 번호에서 입력 횟수 구하기
temp = ch - 1
while temp > -1:
    if len(set(str(temp)) & btn) > 0:
        temp -= 1
    else:
        lowCh = len(str(temp)) + (ch - temp)
        break

# 이동할 채널보다 큰 번호에서 입력 횟수 구하기
temp = ch + 1
while temp < 1000000:
    if len(set(str(temp)) & btn) > 0:
        temp += 1
    else:
        highCh = len(str(temp)) + (temp - ch)
        break

# 작은 번호에서 경우를 찾지 못했다면(-1) 비교 대상에서 제외함
if lowCh == -1:
    print(min(move_ch, highCh))
else:
    print(min(move_ch, highCh, lowCh))