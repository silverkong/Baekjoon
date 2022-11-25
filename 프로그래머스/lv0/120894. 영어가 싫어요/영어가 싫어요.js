function solution(numbers) {
    var answer = 0;
    var num = { zero: 0, one: 1, two: 2, three: 3, four: 4,
                five: 5, six: 6, seven: 7, eight: 8, nine: 9 }
    
    while (isNaN(numbers)){
        for (var key in num){
            if (numbers.includes(key)){
                numbers = numbers.replace(key, num[key].toString());
            }
        }
    }
    
    answer = Number(numbers);
    
    return answer;
}