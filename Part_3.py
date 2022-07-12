def two_list_dictionary(lst1, lst2):
    if len(lst1) > len(lst2):
        to_add = len(lst1) - len(lst2)
        for i in range(to_add):
            lst2.append(None)
        return dict(zip(lst1, lst2))
    return dict(zip(lst1, lst2))



# print(two_list_dictionary(['x', 'y', 'z'], [1,2]))


def range_in_list(lst, start=0, end=0):
    def add(start, end):
        sum = 0
        for i in range(start, end):
            sum += lst[i]
        return sum
    if end == 0 or end > len(lst):
        return add(start, len(lst))
    return add(start, end+1)


print(range_in_list([], 0, 1))