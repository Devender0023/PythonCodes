# from collections import deque

def valid_parentheses(String):
    count = 0
    i = 0
    while i < len(String):
        if String[i] == '(':
            count+=1
        if String[i] == ')':
            count -= 1
        if (count < 0):
            return False
        i+=1
    return count == 0


# print(valid_parentheses("())("))

def reverse_vowels(String):
    sentence = list(String)
    vowels = ('a','e','i','o','u')
    vow_list = [[index, char] for index,char in enumerate(sentence) if char.lower() in vowels]

    print(vow_list)
    for index in range(len(vow_list)):
        sentence[vow_list[index][0]] = sentence[vow_list[index-1][0]]

    return ' '.join(sentence)
    # return String
    # vow = []
    # curr = []
    # for index, char in enumerate(String):
    #     if char.lower() in ('a','e','i','o','u'):
    #         vow.append(char)
    #         curr.append(index)
    # replaced = []
    # replaced.extend(curr)
    # replaced.append(replaced.pop(0))
    # print(curr)
    # print(replaced)
    # new_string = ""
    # counter = 0
    # for i in range(len(curr)):
    #     new_string = new_string+String[counter:curr[i]]+vow[i-1]
    #     print(new_string)
    #     counter = curr[i]+1
    # residual = len(String) - len(new_string)
    # new_string += String[-residual:]
    # return new_string



# print(reverse_vowels("Reverse Vowels In A String"))


def three_odd_numbers(lst):
    # print(len(lst))
    for idx in range(len(lst)-2):
        sum = (lst[idx]+lst[idx+1]+lst[idx+2])
        # print(sum)
        if sum % 2 != 0:
            return True

    return False


print(three_odd_numbers([1,2,3,3,2]))