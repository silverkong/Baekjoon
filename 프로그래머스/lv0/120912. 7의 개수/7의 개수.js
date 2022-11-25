function solution(array) {
    var answer = 0;
    
    for (var num of array){
        var arr = [...String(num)];
        for (var n of arr){
            if (n == '7')
                answer++;
        }
    }
    
    return answer;
}