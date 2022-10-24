import sys

N, M = map(int, sys.stdin.readline().split())
pokemon = {}
pokemon_index = {}

for i in range(N):
    name = sys.stdin.readline().strip()
    pokemon[i] = name
    pokemon_index[name] = i

for _ in range(M):
    temp = sys.stdin.readline().strip()
    if temp.isdigit():
        print(pokemon[int(temp)-1])
    else:
        print(pokemon_index[temp]+1)