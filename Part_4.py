def sum_up_diagonals(outer_list):
    sum = 0
    for index, inner_list in enumerate(outer_list):
        sum += inner_list[index]
        sum += inner_list[-(index+1)]
    # for index, inner_list in enumerate(outer_list):
    #     sum += inner_list[-(index+1)]
    return sum

# print(sum_up_diagonals([
#   [ 1, 2, 3 ],
#   [ 4, 5, 6 ],
#   [ 7, 8, 9 ]
# # ]))

def min_max_key(d):
    lst = [num for num in d.keys()]
    lst.sort()
    return [lst[0], lst[-1]]


# print(min_max_key({2:'a', 7:'b', 1:'c',10:'d',4:'e'}))

def find_greater_numbers(lst):
    count = 0
    for idx in range(1,len(lst)):
        for i in range(0, idx):
            if lst[idx] > lst[i]:
                count+=1
    return count


print(find_greater_numbers([]))