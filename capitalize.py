def compact(collection):
    return [val for val in collection if val]
    # [val for val in collection if bool(val) == True]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))



def partition(collection, fn):
    truthy_list= []
    falsy_list = []
    for num in collection:
        if fn(num):
            truthy_list.append(num)
        else:
            falsy_list.append(num)
    return [truthy_list, falsy_list]

#print(partition([1,2,3,4], callback))



