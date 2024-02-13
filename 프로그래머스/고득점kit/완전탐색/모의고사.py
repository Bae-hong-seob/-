def solution(answers):
    one = [1,2,3,4,5] * (len(answers)//5) + [1,2,3,4,5][:len(answers)%5]
    two = [2,1,2,3,2,4,2,5] * (len(answers)//8) + [2,1,2,3,2,4,2,5][:len(answers)%8]
    three = [3,3,1,1,2,2,4,4,5,5] * (len(answers)//10) + [3,3,1,1,2,2,4,4,5,5][:len(answers)%10]
        
    correct_one = sum([1 for predict, answer in zip(one, answers) if predict==answer])
    correct_two = sum([1 for predict, answer in zip(two, answers) if predict==answer])
    correct_three = sum([1 for predict, answer in zip(three, answers) if predict==answer])
    
    correct = [correct_one, correct_two, correct_three]
    max_correct = max(correct)
    answer = []
    for index, value in enumerate(correct):
        if max_correct == value:
            answer.append(index+1)
    return answer