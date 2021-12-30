# import sys
# list_comp = sys.getsizeof([x*10 for x in range(1000)])
# gen_exp = sys.getsizeof(x*10 for x in range(1000))


# print(list_comp)
# print(gen_exp)

# def is_all_strings(collection):
#     return all(type(item) == str for item in collection)


# print(is_all_strings([2, 'a', 'b', 'c']))


# songs = [
# 	{"title": "happy birthday", "playcount": 1},
# 	{"title": "survive", "playcount": 6},
# 	{"title": "YMCA", "playcount": 99},
# 	{"title": "Toxic", "playcount": 31}
# ]

# print(sorted(songs, key = lambda user : user["playcount"], reverse = True))


def sum_even_values(*args):
    return sum(arg for arg in args if arg%2==0)


print(sum_even_values(1,2,3,4,5,6))





