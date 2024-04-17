from random import randint
def main():
    word1 = input()
    word2 = input()
    print('SI' if sort(list(word1)) == sort(list(word2)) else ranword(list(word1), [], 0))

def sort(word):
    for i in range(len(word)):
        for j in range(len(word)-1-i):
            if word[j] > word[j+1]:
                word[j], word[j+1] = word[j+1], word[j]
    return word

def ranword(word, random, count):
    while count <= len(word)-1:
        x = randint(0, len(word)-1)
        if not(x in random):
            random.append(x)
            count += 1
    
    new_word = generator(word.copy(), random)
    new_word, word = convert(new_word, ''), convert(word, '')
     
    return new_word if new_word != word else ranword(word, [], 0)

def convert(word, string):
    for i in word:
        string += i
    return string

def generator(word, random):
    for i in range(len(word)):
        word[i], word[random[i]] = word[random[i]], word[i]
    return word

main()