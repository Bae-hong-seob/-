def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x : str(x)*3, reverse=True)
    
    return "0" if numbers[0]=="0" else ''.join(numbers)