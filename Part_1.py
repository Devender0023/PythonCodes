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

def new_list_check(my_list):
    return all(type(l) == list for l in my_list)

# print(new_list_check([[],[1],[2,3]]))

def remove_every_other(other_list):
    new_list = []
    for count,value in enumerate(other_list):
        if count%2 == 0:
            new_list.append(value)
    return new_list

def remove_every_other_(lst):
    return [val for i,val in enumerate(lst) if i % 2 == 0]

# print(remove_every_other_([5,1,2,4,1]))

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


# print(sum_pairs([4, 2, 10, 5, 1], 15))

def vowel_count(word):
    vowel_dict = {}
    for char in word:
        if char.lower() in ('a','e','i','o','u'):
            if char.lower() in vowel_dict.keys():
                vowel_dict[char.lower()]+=1
            else:
                vowel_dict[char.lower()] = 1

    return vowel_dict


# print(vowel_count('Python'))