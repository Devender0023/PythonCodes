# from collections import deque
from functools import wraps

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


# print(three_odd_numbers([1,2,3,3,2]))


def mode(lst):
    total = {key:lst.count(key) for key in lst}
    keys = list(total.keys())
    vals = list(total.values())
    num = max(total.values())
    return (keys[vals.index(num)])


# print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))


def letter_counter(string):
    def inner(char):
        return string.lower().count(char)
    return inner

# counter = letter_counter('Amazing')
# print(counter('a'))
# print(counter('m'))
#
# counter2 = letter_counter('This Is Really Fun!')
# print(counter2('i'))
# print(counter2('t'))


def once(fn):
    fn.is_called = False

    def inner(*args):
        if not(fn.is_called):
            fn.is_called=True
            return fn(*args)
    return inner




# oneAddition = once(add)
# print(oneAddition(2,2))
# print(oneAddition(2,2))

def next_prime():
    count=2
    all_primes = set()
    while True:
        for prime in all_primes:
            if count%prime==0:
                break
        else:
            all_primes.add(count)
            yield count
        count+=1



primes = next_prime()
print([next(primes) for i in range(25)])





