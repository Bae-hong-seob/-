def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        a,b = phone_book[i], phone_book[i+1]
        if len(a)>len(b):
            continue
        if b[:len(a)] == a:
            return False
        
    return True