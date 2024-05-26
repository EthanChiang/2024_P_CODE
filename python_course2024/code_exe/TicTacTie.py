row1 =[" "," "," "]
row2 =[" "," "," "]  # 4,5,6 -> rwo2 0,1,2
#4,5,6 mod 3 = 1,2, 0
#1,2,0 -1 =0,1, -1
row3 =[" "," "," "]

counter =0

def display(row1,rwo2,row3):
    print(row1)
    print(row2)
    print(row3)

def user_choice():
    choice = input("please enter a number (1-9): ")
    # print(choice)
    # while not choice.isdigit() or int(choice) >9 or int(choice) <1:
    while not choice.isdigit() or (int(choice) not in range(1,10)):
            if not choice.isdigit():
                print("not valid")                            
            else:
                print("not within 1-9")
            choice = input("Enter1-9:") 
    return int(choice)

def getCurrentSymbol():
     global counter
     symbol_list = ["X","O"]
     counter +=1
     return symbol_list[counter%2]

def update_table(index):
     global counter
     if index in range(1,4):
          if row1[index -1] == " ":
             row1[index -1 ] = getCurrentSymbol()
             return True
          else:
             return False 
     elif index in range(4,7):
          if row2[index %3 -1 ] == " ": 
             row2[index %3 -1 ] = getCurrentSymbol()
             return True
          else:
             return False 
     else:
          if row3[index %3 -1 ] == " ":
             row3[index%3 -1] = getCurrentSymbol()
             return True
          else:
             return False            

def start_game():
   while True:
      display(row1,row2,row3)
      while True:
          choice = user_choice()
          if update_table(choice):
              break
          else:
              print("invalid input")    
    #   choice= user_choice()
    #   flag = update_table(choice)
    #   if not flag:
    #       print("invalid input")

      result = check_winning()
      if result == "player 1 wins":
          display(row1,row2,row3)
          print("player 1 wins")
          return
      elif result == "player 2 wins":     
          display(row1,row2,row3)
          print("player 2 wins")
          return


          

def check_winning():
    player1_wins = False
    player2_wins = False
    if(row1[0] ==row1[1] and row1[1] == row1[2] and (" " not in row1)):
         if(row1[0]=="X"):
             player2_wins = True
         else:
             player1_wins = True
    elif(row2[0] ==row2[1] and row2[1] == row2[2] and (" " not in row2)):
         if(row2[0]=="X"):
             player2_wins = True
         else:
             player1_wins = True
    elif(row3[0] ==row3[1] and row3[1] == row3[2] and (" " not in row3)):
         if(row3[0]=="X"):
             player2_wins = True
         else:
             player1_wins = True
    elif(row1[0] ==row2[0] and row2[0] == row3[0] and (" " != row1[0] and " " != row2[0] and " " != row3[0])):
         if(row1[0]=="X"):
             player2_wins = True
         else:
             player1_wins = True
    elif(row1[1] ==row2[1] and row2[1] == row3[1] and (" " != row1[1] and " " != row2[1] and " " != row3[1])):
         if(row1[1]=="X"):
             player2_wins = True
         else:
             player1_wins = True                                        
    elif(row1[2] ==row2[2] and row2[2] == row3[2] and (" " != row1[2] and " " != row2[2] and " " != row3[2])):
         if(row1[2]=="X"):
             player2_wins = True
         else:
             player1_wins = True                                        
         



    if player1_wins:
        return "player 1 wins"
    elif player2_wins:
        return "player 2 wins"
    else:
        return "draw"





# update_table(1)    
# display(row1,row2,row3)
# user_choice()
# getCurrentSymbol()







# choice = input("please enter a number (1-9): ")
# # print(int(choice)>9)
# print(choice.isdigit())

start_game()