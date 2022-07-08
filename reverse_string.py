def reverse_string(word):
    return word[::-1]
# print(reverse_string("dev"))

def list_check(my_list):
    count = 0
    # count_not_list = 0
    for ele in my_list:
        if type(ele) == list:
            count+=1

    if count == len(my_list):
        return True
    return False


# print(list_check([[],[1],[2,3]]))

