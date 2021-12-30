def return_day(num = 1):
    days = {
        1:"Sunday",
        2:"Monday",
        3:"Tuesday",
        4:"Wednesday",
        5:"Thursday",
        6:"Friday",
        7:"Saturday"
    }
    day = days.get(num)
    if num < 1 or num > 7:
        return None
    return day

print(return_day(3))
print(return_day(9))

def last_element(nums):
    if len(nums) == 0:
        return None
    return nums[-1]

print(last_element([1, 2, 3]))
print(last_element([]))


def single_letter_count(word, char):
    if word:
        result = word.lower().count(char.lower())
        return result
    return 0


print(single_letter_count("Hello", "l"))
print(single_letter_count("Hello", "h"))
print(single_letter_count("Hello", "a"))



def multiple_letter_count(word):
    return {char:word.lower().count(char.lower()) for char in word}



print(multiple_letter_count("awesome"))
print(multiple_letter_count("Hello"))