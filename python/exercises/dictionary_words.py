    #take word dictionary list. and then extract the n number of words from the list and then rearrange the words


import random
import sys

with open("/usr/share/dict/words", 'r') as f:
    corpus = f.read().splitlines()
f.close()

arr = corpus
def random_words():
    arr2 = []
    arr3 = arr
    #print arr3
    for i in range(5):
        rand_index = random.randint(0, len(arr3) - 1)
        arr2.append(arr3[rand_index])
        arr3.remove(arr3[rand_index])
    return arr2

if __name__ == '__main__':
    newSentence = random_words()
    print " ".join(newSentence)