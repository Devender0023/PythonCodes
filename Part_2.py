def titleize(sentence):
    words = sentence.split()
    words = [word.replace(word[0], word[0].upper()) for word in words]
    return ' '.join(words)

# print(titleize("oNLy cAPITALIZe fIRSt"))

def find_factors(number):
    factors = [num for num in range(1,number+1) if number%num==0]
    return factors

# print(find_factors(412146))

def includes(collection, element, index=0):
    if type(collection) in (str, list):
        new_coll = collection[index:len(collection)]
        if element in new_coll:
            return True
        return False
    else:
        if element in collection.values():
            return True
        return False


# print(includes('abcd','b',1))

def repeat(my_str, num):
    return my_str*num

# print(repeat('abc', 0))

def truncate(sentence, num):
    if num < 3:
        return "Truncation must be at least 3 characters."
    else:
        if num-3 > len(sentence):
            return f'{sentence[:num-3]}'
        return f'{sentence[:num-3]}...'


print(truncate("Problem solving is the best!", 10))