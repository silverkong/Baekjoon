function solution(A, B) {
    var arr = [...A]
    for (var i = 0; i < arr.length; i++){
        if (A === B)
            return i;
        else{
            arr.unshift(arr.pop())
            if(arr.join('') === B)
                return i + 1;
        }
    }
    return -1;
}