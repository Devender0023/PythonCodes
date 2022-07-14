def two_list_dictionary(lst1, lst2):
    if len(lst1) > len(lst2):
        to_add = len(lst1) - len(lst2)
        for i in range(to_add):
            lst2.append(None)
        return dict(zip(lst1, lst2))
    return dict(zip(lst1, lst2))



# print(two_list_dictionary(['x', 'y', 'z'], [1,2]))


def range_in_list(lst, start=0, end=0):
    if end == 0 or end > len(lst):
        return sum(lst[start:len(lst)])
    return sum(lst[start:end+1])


# print(range_in_list([], 0, 1))


def same_frequency(num1, num2):

    # def make_dict(nums):
    #     my_dict = {}
    #     for num in str(nums):
    #         if num not in my_dict.keys():
    #             my_dict[num] = 1
    #         else:
    #             my_dict[num] += 1
    #     return my_dict

    dict1 = {letter:str(num1).count(letter) for letter in str(num1)}
    dict2 = {letter:str(num2).count(letter) for letter in str(num2)}
    count = 0
    for key, value in dict1.items():
        if key in dict2.keys() and dict1[key] == dict2[key]:
            count+=1
    if count == len(dict1):
        return True
    return False


# print(same_frequency(1212, 2211))

def nth(lst, index):
    if index < 0:
        return lst[len(lst)+index]
    return lst[index]


# print(nth(['a','b','c','d'],3))


def find_the_duplicate(lst):
    new_list = []
    for ele in lst:
        if ele not in new_list:
            new_list.append(ele)
        else:
            return ele


print(find_the_duplicate([2,1,3,4]))




