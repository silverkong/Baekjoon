function solution(quiz) {
    var answer = [];
    var quiz_arr = [];
    
    for (var q of quiz)
        quiz_arr.push(q.split(" "));
    
    for (var arr of quiz_arr){
        var temp = 0;
        var result = 0;
        var op = '';
        for (var a of arr){
            if (a == '+' || a == '-' || a == '=')
                op = a;
            else if (isNaN(a) == false){
                if (op == '')
                    var temp = Number(a);
                else if (op == '='){
                    if (result == Number(a))
                        answer.push("O");
                    else
                        answer.push("X");
                }else{
                    if (op == '-')
                        result = temp - Number(a);
                    else
                        result = temp + Number(a);
                }
            }
        }
    }
    
    return answer;
}