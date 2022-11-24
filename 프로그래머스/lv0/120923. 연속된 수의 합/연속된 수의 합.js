function solution(num, total) {
    var answer = [];
    var minNum = Math.ceil(total / num) - Math.floor(num / 2);
    
    for (i = minNum; i < minNum + num; i++){
        answer.push(i);
    }
    
    return answer;
}