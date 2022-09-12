s = list(input())

for i in range(len(s)):
    if(ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z')):
        s[i] = s[i].upper()
    else:
        s[i] = s[i].lower()

for i in range(len(s)):
    print(s[i], end='')