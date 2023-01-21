# def solution(absolutes, signs):
#     return sum([absolutes[i] if signs[i] == True else absolutes[i]*-1 for i in range(len(signs)) ])

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))