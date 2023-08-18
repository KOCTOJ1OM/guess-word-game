import random


lines = open('finalwords.txt').read().splitlines()
def chose_word():
    myline =random.choice(lines)
    return myline

secret = chose_word()


count = len(secret)

correct = list(secret)

final = []
lifes = 5
print('word: ', '*'*count, 'length:', count)

def chose(lifes):
    print(f' attemps: {lifes}\\5')
    if lifes != 0:
        word = input('you`r word is: ')
        if len(word) > len(secret):
            print(f'you cant write word that longer then {len(secret)} symbols')
            word = input("try again: ")
        elif len(word) < 3:
            print(f'you cant write word that shorter then 3 symbols')
            word = input("try again: ")
        elif word == '':
            print(f'you cant write word that shorter then 3 symbols')
            word = input("try again: ")
        else:
            if ' ' in word:
                word = word.replace(' ', '')
                pass
            else:
                pass

    word = word.casefold()

    list_of_exist = []
    #create list of exist words
    for a in lines:
        if word[0] in a[0]:
            list_of_exist.append(a)
        else:
            pass
    #chek input for existance of word
    if word in list_of_exist:
        pass
    else:
        print('this word is not in list')
        chose(lifes)

    return word


def check(word, lifes):
    try:
        Lword = list(word)

        ugadanie = []

        counter = 0

        for a in Lword:
            if Lword[counter] in secret:
                ugadanie.append(Lword[counter])
                counter = counter + 1
            else:
                counter = counter + 1
                pass

        if len(final) < len(secret):
            for a in correct:
                final.append('*')

        import numpy as np
        for x in ugadanie:
            idx = np.argwhere(np.array(correct) == x).flatten()
            for a in idx:
                final[a] = x

        final2 = ''.join(final)
        lifes = lifes - 1

        if word == secret:
            print('congrats! its your wictory, word: ', secret)
        elif final2 != secret:
            print('nope.   ', 'word: ', final2)
            check(word=chose(lifes), lifes=lifes)
        elif final2 == secret:
            print('congrats! its your wictory, word: ', secret)
        else:
            print('you lose.. secret word is:', secret)
    except:
        print('you lose.. Secret word is: ', secret)


check(word=chose(lifes=lifes), lifes=lifes)