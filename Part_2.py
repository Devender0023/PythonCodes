def titleize(sentence):
    words = sentence.split()
    words = [word.replace(word[0], word[0].upper()) for word in words]
    return ' '.join(words)

print(titleize("oNLy cAPITALIZe fIRSt"))