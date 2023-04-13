def solution(my_string):
    remove_list = ['a','e','i','o','u']
    for i in remove_list:
        my_string = my_string.replace(i,'')
    return my_string