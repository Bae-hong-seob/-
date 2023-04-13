def solution(hp):
    return sum([hp//5, (hp-(hp//5)*5)//3, hp-(hp//5)*5-((hp-(hp//5)*5)//3)*3])