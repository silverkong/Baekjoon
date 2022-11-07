def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)):
        if i == len(phone_book)-1:
            break
        prefix = phone_book[i]
        other_num = phone_book[i+1]
        if prefix in other_num and other_num.index(prefix) == 0:
            return False

    return True