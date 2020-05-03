import re
from time import time
start = time()
def duplicate_encode(word):
    word = word.lower()
    word = word.replace("(",",")
    word = word.replace(")",'<')
    
    for i in word:
        if i != 1 and i != 0:
            search = re.findall(i,word)
            if len(search) > 1:
                word = re.sub(i,'1',word)
            else:
                word = re.sub(i,'0',word)
        print('Palabra: ' + str(word))

    word = re.sub('1',')',word)
    word = re.sub('0','(',word)
    return word

print(start - time())