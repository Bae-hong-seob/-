N = 5
fear_list = [2, 3, 1, 2, 2]

fear_list = sorted(fear_list)
group = 0

while(fear_list):
            print(fear_list)
            how_many = fear_list[-1]
            
            # group 결성 가능
            if how_many <= len(fear_list):
                        for _ in range(how_many):
                                    fear_list.pop()
                        group+=1
            # group 인원수 부족.
            else:
                        continue
print(group)            