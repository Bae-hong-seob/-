def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(reverse=True)
    numbers.sort(key=lambda x : x*3, reverse=True)
    
    return "0" if numbers[0]=="0" else ''.join(numbers)