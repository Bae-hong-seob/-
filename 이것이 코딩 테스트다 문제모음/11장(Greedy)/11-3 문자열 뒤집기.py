#N = '0001100'
N = input()

make_0_count = N.split('0')
make_0 = 0 
for count in make_0_count:
    if count != '':
                make_0+=1
print(make_0)
                        
make_1_count = N.split('1')
make_1 = 0 
for count in make_1_count:
    if count != '':
                make_1+=1
print(make_1)

print(make_0_count, make_1_count)
print(min(make_0, make_1))