function solution(my_string) {
    var answer = '';
    var str_set = new Set([...my_string]);
    var str_arr = [...str_set];
    answer = str_arr.join("");
    
    
    return answer;
}