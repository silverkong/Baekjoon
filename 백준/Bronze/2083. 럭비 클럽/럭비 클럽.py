r = []
while True:
    m = input().split(' ')
    if m[0] == '#':
        break
    if int(m[1]) > 17 or int(m[2]) >= 80:
        str = m[0] + ' Senior'
        r.append(str)
    else:
        str = m[0] + ' Junior'
        r.append(str)
for i in range(len(r)):
    print(r[i])