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
# print(list3)

items = ["hi", 4, 8.99, "apple", ('t,b','n')]
list4 = [((items.index(v),v)) for v in items]
# print(list4)

num1 = [1,2,3,4,4,5,5]
num2 = [2,3,4,5]

list5 = [a for a in num1 if a in num2]
# print(list5)

sentence1 = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
words = sentence1.split()
list6 = [num for num in words if num.isdigit()==True]
# print(list6)

list7 = ['even' if num%2==0 else 'odd' for num in range(1,21)]
# print(list7)

num3 = [1,2,3,4,5,6,7,8,9]
num4 = [2,7,1,12]

list8 = [(x,x) for x in num3 if x in num4]
# print(list8)

list9 = [word for word in words if len(word)>=4]
# print(list9)

list10 = [number for number in range(1,1000) if True in [True for x in range(2,10) if number%x==0]]

print(list10)









