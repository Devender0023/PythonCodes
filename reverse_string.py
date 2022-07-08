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

def remove_every_other(other_list):
    new_list = []
    for count,value in enumerate(other_list):
        if count%2 == 0:
            new_list.append(value)


    return new_list

# print(remove_every_other([5,1,2,4,1]))

def sum_pairs(nums, num):
    new_nums = []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == num:
                new_nums.append(nums[i])
                new_nums.append(nums[j])
        if len(new_nums) == 2:
            break
    return new_nums




print(sum_pairs([4, 2, 10, 5, 1], 15))