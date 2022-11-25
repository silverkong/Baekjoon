function solution(my_string) {
    var answer = 0;
    var str_arr = my_string.split(" ");
    var op = '';
    
    for (var str of str_arr){
        if (isNaN(str) == false){
            if (answer == 0)
                answer = Number(str)
            else{
                if (op == '+')
                    answer += Number(str);
                else
                    answer -= Number(str);
            }
        }else
            op = str;
    }
    
    return answer;
}