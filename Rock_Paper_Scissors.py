from random import randint
import random
from tkinter import N

def play():
    answer = input("would you like to start y/n? ").upper()
    while answer != N:
        computer= random.choice(['Rock', 'Paper', 'Scissors'])
        player = input("Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors: " )
        ##Rock > Scissors, Paper > Rock, Scissors > Paper
        if (player == 'r' and computer== 'Paper'):
            print("Computer chooses Paper. You lose.")
        elif (player == 'p' and computer== 'Scissors'):
            print("Computer chooses Scissors. You lose.")
        elif (player == 's' and computer == 'Rock'):
            print("Computer chooses Rock. You lose.")
        elif (player == computer):
            print("Tied.")
            
   
        else: print(f"Computer chooses {computer}. You win")
        answer = input("would you like to play again y/n? ")

        #need to add error handling for incorrect imputs 
play()






