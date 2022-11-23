T = int(input())

for _ in range(T):
    N = int(input())
    clothes = [input().split() for _ in range(N)]

    answer = 1
    clothesDic = {}
    
    # 옷 리스트 딕셔너리에 담기
    for cloth in clothes:
        if cloth[1] not in clothesDic.keys():
            clothesDic[cloth[1]] = 1
        else:
            clothesDic[cloth[1]] += 1
    
    # 입거나 안 입거나의 조건
    for key, value in clothesDic.items():
        answer *= (value + 1)
    
    # 둘 다 안 입는다는 조건도 포함되어 있으므로 -1을 해준다
    answer -= 1
    print(answer)