N = 5
coins = [3,2,1,1,9]

coins.sort()

check_number = 1
for coin in coins:
    if check_number < coin:
        break
    else:
        check_number+=coin
        
print(check_number)