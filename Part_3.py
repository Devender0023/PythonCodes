def two_list_dictionary(lst1, lst2):
    if len(lst1) > len(lst2):
        to_add = len(lst1) - len(lst2)
        for i in range(to_add):
            lst2.append(None)
        return dict(zip(lst1, lst2))
    return dict(zip(lst1, lst2))



print(two_list_dictionary(['x', 'y', 'z'], [1,2]))