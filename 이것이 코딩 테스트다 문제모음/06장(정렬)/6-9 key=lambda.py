array = [('바나나', 2), ('사과', 5), ('당근', 3)]
print('before : ', array)

def setting(data):
    return data[1]

result = sorted(array, key = setting)
print('after : ', result)