function solution(s) {
    var answer = '';
    var str_arr = [...s].sort();
    var count = getCount(str_arr);
    
    for (var [key, value] of Object.entries(count)){
        if (`${value}` == '1'){
            answer += key;
        }
    }
    
    return answer;
}

function getCount(array) {
    return array.reduce((pv, cv) => {
        pv[cv] = (pv[cv] || 0) + 1;
        return pv;
    }, {});
}