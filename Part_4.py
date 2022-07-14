def sum_up_diagonals(outer_list):
    sum = 0
    for index, inner_list in enumerate(outer_list):
        sum += inner_list[index]
        sum += inner_list[-(index+1)]
    # for index, inner_list in enumerate(outer_list):
    #     sum += inner_list[-(index+1)]
    return sum

print(sum_up_diagonals([
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]))

def min_max_key