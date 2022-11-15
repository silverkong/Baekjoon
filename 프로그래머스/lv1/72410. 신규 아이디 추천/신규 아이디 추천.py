import re
def solution(new_id):
    answer = ''
    
    # 1단계 : 소문자로 변경
    new_id = new_id.lower()
    
    # 2단계 : 소문자, 숫자, -, _, .가 아니라면 제거
    rules = re.compile('[0-9a-z_.\-]+')
    new_id = rules.findall(new_id)
    new_id = ''.join(new_id)
            
    # 3단계 : 마침표가 2번 이상 연속된다면 하나로 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # 4단계 : 마침표가 처음이나 끝에 위치한다면 제거
    new_id = new_id.strip('.')
        
    # 5단계 : 빈 문자열이라면, "a"대입
    if new_id == '':
        new_id += 'a'
        
    # 6단계 : 16자 이상이면 16자부터 모두 제거, 제거한 후 '.'이 위치한다면 '.' 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
            
    # 7단계 : 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 붙이기
    while len(new_id) <= 2:
        new_id += new_id[-1]
    
    return new_id