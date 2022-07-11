def titleize(sentence):
    words = sentence.split()
    words = [word.replace(word[0], word[0].upper()) for word in words]
    return ' '.join(words)

# print(titleize("oNLy cAPITALIZe fIRSt"))

def find_factors(number):
    factors = [num for num in range(1,number+1) if number%num==0]
    return factors

print(find_factors(412146))