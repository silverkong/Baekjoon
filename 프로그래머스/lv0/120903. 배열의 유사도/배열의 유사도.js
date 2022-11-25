function solution(s1, s2) {
    var result = s1.filter(x => s2.includes(x));
    var answer = result.length;
    
    return answer;
}