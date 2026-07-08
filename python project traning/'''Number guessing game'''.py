'''Number guessing game'''
import random

guess =  0 
while True : 
    guess += 1
    num = random.randint(1,10)
    player_guess = int(input())
    if num == player_guess :
        print("winner")
        print(guess) 
        break
    if num > player_guess :
        print ("upper")
    elif num < player_guess : 
        print ("lower")
    