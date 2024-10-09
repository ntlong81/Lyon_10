print("our module is imported")
def text_normalize(text, lower = True):
    if lower:
        text_nor = text.lower()
    else:
        text_nor = text 
    special_letters =set('.,?*()-')
    for letter in special_letters:
        text_nor = text_nor.replace(letter,' ')
    return text_nor

def text_count(text, nor = True):
    if nor:
        text_nor = text_normalize(text)
    else:
        text_nor = text
    words = text_nor.split()
    fre_word ={}
    for word in words:
        if word in fre_word:
            fre_word[word] += 1
        else: 
            fre_word[word] = 1
    return fre_word

def get_topk(fre_word, k =5):
    return sorted(list(fre_word.items()),key= lambda x: x[1],reverse=True)[:k]
