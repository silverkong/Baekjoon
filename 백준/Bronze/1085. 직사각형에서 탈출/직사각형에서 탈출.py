x, y, w, h = map(int, input().split())
if x < w-x:
    rx = x
else:
    rx = w-x
if y < h-y:
    ry = y
else:
    ry = h-y
if rx < ry:
    print(rx)
else:
    print(ry)
