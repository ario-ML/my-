'''Word guessing game'''
import random 
worlds = ["red " , "blue" , "green " , "black" , "pink" , "gold", "silver" , "perpel"]

print ("welcome to guess color ")
turn = 0
while True : 
    turn += 1 
    world =random.choice(worlds)
    guess = input("guess your color")
    if world == guess : 
        print("winner")
        break 
    if world != guess :
        print("wrong ")
    if turn == 3 :
        print ("loser")
        break