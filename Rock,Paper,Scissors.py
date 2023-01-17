import random

choices = ["r" , "p" , "s"]

choice_meaning ={
    "r" : "Rock",
    "s" : "Scissors",
    "p" : "Paper",
}

user_score = 0
ai_score = 0

# *final_number = 5

i = 0

# for i in range(5):
while i < 5:    
# *while True
     user_choice = input("Select from Rock,Paper,Scissors (r, p, s): ")

     ai_choice = random.choice(choices)  #hoshmasnoyee 

     if user_choice in choices:
          print(f"Your choice is {choice_meaning[user_choice]}. AI choice is {choice_meaning[ai_choice]}.")
     # for won : r > s  -  p > r  -  s > p 
          if user_choice == ai_choice:
               print('Tie')
          elif user_choice == "r" and ai_choice == "s":
               print("user have earned a point.")
               user_score += 1
          elif user_choice == "p" and ai_choice == "r":
               print("user have earned a point.") 
               user_score += 1   
          elif user_choice == "s" and ai_choice == "p":
               print("user have earned a point.")
               user_score += 1
          else:
               print("AI have earned a point.")
               ai_score += 1
     else:
          print("Invalid input")
          i -= 1
     
     print(f"user score: {user_score} / AI score: {ai_score}") 
     
     # *if user_score == final_number or ai_score == final_number 
          #  *break   
     print("\n", "_"*15, "\n")
     
     i += 1
     
if user_score > ai_score:
     print(f"user you are winner by {user_score} score,but AI you are loser by {ai_score}.")
elif user_score < ai_score:
     print(f"AI you are winner by {ai_score} score,but user you are loser by {user_score} score.")
else:
     print(f"user you have equalized with AI. AI score = {ai_score}, user score = {user_score} ")

# *if user_score == final_number:
     # *print(f"user you are winner by {user_score} score,but AI you are loser by {ai_score}.")
# *elif user_score < ai_score:
     # *print(f"AI you are winner by {ai_score} score,but user you are loser by {user_score} score.")        