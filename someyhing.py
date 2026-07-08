import random 
print("guess_number_game")

random_num = random.randint(1,10)
guess = 0


player_1 = str(input("player_1 : "))
player_2= input("player_2 : ")
random_starter = random.choice([player_1,player_2])
print(f"{random_starter} turn ")
currect_player =random_starter
while True :
    if guess == 4 : 
           
       print("chans is gone")
       break
    
    
    guess += 1
    player_guess = int(input(f"{currect_player} guess a number:"))
    
    if guess == 4 : 
           
       print("chans is gone")
       break

    if player_guess == random_num :
        print(f"winner is {currect_player}")
        print(f"number is :{random_num}")
        print("end")
        
        break
    elif player_guess <random_num  :
        print("upper")
        print(f"chance:{guess}")
    elif player_guess > random_num : 
        print("lower")
        print(f"chance:{guess}")
   
    currect_player = random_starter
    if currect_player == player_1 :
        currect_player = player_2
    elif currect_player == player_2 : 
            currect_player = player_1
       
            
      









