import random
from tkinter import N
from Words import words
import string



def word_guess(words): #the function to select a word
    word = random.choice(words) #randomly chooses somethingg from the list Words.py
    while '-' in word or ' ' in word: #cannot have space or - in hangman
        word = random.choice(words)

    return word.upper()

def hangman():
    answer = input("Would you like to start playing y/n ")
    while answer !=N:
        word = word_guess(words)
        word_letter = set(word) #letters in the word
        alphabet = set(string.ascii_uppercase)
        used_letters = set() # empty set for what the user guesses

        lives = 6

        #getting user input
        while len(word_letter) > 0:
            #''.join(['a' 'b' 'cd'] ) --> 'a b cd'
            print('You guessed the following letters:', ' '.join(used_letters) ) ##NOTE THE SPACEING!!!! Need a coma and a space inbetween the ' '.join()

            #what current word is (ie:w-rd)
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print ('Current word: ' , ' '.join(word_list) )


            user_letter = input('Guess a letter: ').upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter) #adds guessed letter to overall guessed set
                if user_letter in word_letter:
                    word_letter.remove(user_letter) #removes correctly guessed letter from word set
                    print('That letter was correct!')
                else:
                    lives = lives -1
                    print("That letter was incorrect!")
            elif user_letter in used_letters:
                print('You have already guessed that letter, try again.')
            else:
                print('Invalid Character. Try again.')
                
            if lives ==0:
                print(f'You LOSE! The word was {word}') 
                break 
        if len(word_letter) ==0:
                print(f'You WON! The word was {word}')
        answer = input("Would you like to play another round? y/n ")      
hangman()

