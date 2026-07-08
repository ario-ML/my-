import random 
from collections import Counter 

random_words = '''greenland uk usa iraq japan france germany iran poland'''
random_words = random_words.split(' ')

word = random.choice(random_words)
if __name__ == "__main__" : 
    for i in word :
        print('_',end=" ")
    print()

playing = True 


