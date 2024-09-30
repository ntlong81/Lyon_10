text = '''To you to you understand to you ChatGPT.'''
#normalize
text_nor = text.lower()
for char in {'.','*',',','-',}:
    text_nor = text_nor.replace(char, ' ')
#count
words = text_nor.split()
fre_words ={}
for word in words:
    if word in fre_words:
        fre_words[word] += 1
    else: 
        fre_words[word] = 1
print(fre_words)