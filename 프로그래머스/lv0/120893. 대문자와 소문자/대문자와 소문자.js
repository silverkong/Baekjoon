function solution(my_string) {
    var answer = '';
    var str = [...my_string];
    var lower = /^[a-z]+$/
    
    for (var s of str){
        if (lower.test(s)){
            answer += s.toUpperCase();
        }else{
            answer += s.toLowerCase();
        }
    }
    return answer;
}