import num2word
from word2number import w2n

def add(query):
    if '+' in query:
        list = query.split('+')
    if 'plus' in query:
        list = query.split('plus')

    print(list[0], list[1])   

    try:
        list[0] = num2word(list[0]) 
        list[1] = num2word(list[1]) 
        a = w2n.word_to_num(list[0])
        b = w2n.word_to_num(list[1])
    except:
        a = int(list[0])
        b = int(list[1])
          
    return a + b

def subtract(query):
    if '-' in query:
        list = query.split('-')
    if 'minus' in query:
        list = query.split('minus')

    print(list[0], list[1])   

    try:
        list[0] = num2word(list[0]) 
        list[1] = num2word(list[1]) 
        a = w2n.word_to_num(list[0])
        b = w2n.word_to_num(list[1])
    except:
        a = int(list[0])
        b = int(list[1])
          
    return a - b