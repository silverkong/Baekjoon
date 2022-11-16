def solution(phone_number):
    answer = ''
    back_number = phone_number[-4:]
    slice_number = phone_number[0:-4]
    
    for num in slice_number:
        answer += '*'
    
    return answer + back_number