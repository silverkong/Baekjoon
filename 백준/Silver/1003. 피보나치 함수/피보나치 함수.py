T = int(input())
      
for _ in range(T):
    c_0 = [1, 0]
    c_1 = [0, 1]
    N = int(input())
    if N > 1:
        for i in range(N-1):
            c_0.append(c_1[-1])
            c_1.append(c_0[-2] + c_1[-1])
    print(c_0[N], c_1[N])