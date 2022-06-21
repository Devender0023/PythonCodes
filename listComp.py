list = [x for x in range(1,1000) if x%7==0]
# print(list)

list1 = [x for x in range(1,1000) if '3' in str(x)]
# print(list1)

string = 'Given a list of numbers, remove floats (numbers with decimals)'
list2 = [x for x in string if x==' ']
# print(len(list2))


sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
chars = ['a','e','i','o','u', ' ']
list3 = [char for char in sentence if char not in chars]
print(list3)
