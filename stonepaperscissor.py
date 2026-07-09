#this program is generated to play stone,,paper,,scissor!
import os
os.system ("cls")
print("HELLO GUYZ! SHAKE YOUR HANDS. AFTER SHAKING , Enter data:)")
user1 = input("user1 ENTER YOUR SHAPE: ").lower()
user2 = input("user2 ENTER YOUR SHAPE: ").lower()
if(user1 == "stone" and user2 == "scissor"):
    print("CONGRATS user1 WINS! ")
elif(user1 == "scissor" and user2 == "stone"):
    print("CONGRATS user2 WINS!")
elif(user1 == "paper" and user2 == "stone"):
    print("CONGRATS user1 WINS! ")
elif(user1 == "stone" and user2 == "paper"):
    print("CONGRATS user2 WINS!")
elif(user1 == "paper" and user2 == "scissor"):
    print("CONGRATS user2 WINS!")
elif(user1 == "scissor" and user2 == "paper"):
    print("CONGRATS user1 WINS! ")
elif(user1 == "stone" and user2 == "stone" or user1 == "scissor" and user2 == "scissor" or HADIQA == "paper" and HIBBA == "paper"):
    print("BOTH SHAPES ARE SAME! Please try again.")
else:
    print("INVALID SYNTAX!")
