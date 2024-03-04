def solution(want, number, discount):
    dictionary = {}
    for product, count in zip(want, number):
        dictionary[product] = count
    
    answer = 0
    for start in range(len(discount)): #최대 100,000
        now = discount[start:start+10]
        
        discount_products = {} #할인 품목 및 개수
        for product in now: #10번 반복.
            try:
                discount_products[product]+=1
            except:
                discount_products[product]=1
        
        valid = True
        for key in dictionary.keys(): #최대 10번 반복. -> 최대 1,000,000번. 완전탐색 가능
            try:
                if dictionary[key] != discount_products[key]: #원하는 제품을 모두 할인받을 수 없는 경우
                    valid=False
                    break
            except: #원하는 품목이 할인품목중에 없는 경우 error 발생처리.
                valid=False
                break
            
        if valid: # 원하는 제품을 모두 할인받을 수 있는 경우
            answer+=1
        
    
    return answer