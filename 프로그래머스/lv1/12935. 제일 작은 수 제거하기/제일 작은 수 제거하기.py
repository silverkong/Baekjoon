def solution(arr):
    minIndex = arr.index(min(arr))
    del arr[minIndex]
    
    if len(arr) == 0:
        arr.append(-1)
        return arr
    else:
        return arr