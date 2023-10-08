def solution(numbers):
    
    numbers = list(map(str,numbers))
    numbers = sorted(numbers, key=lambda number : number*3, reverse=True)

    return ''.join(numbers) if numbers[0] != '0' else "0"