import random
rock="🤛"
paper="🤚"
scissors="✌️"

print("welcome to 🆁🅾🅲🅺 🅿🅰🅿🅴🆁 🆂🅲🅸🆂🆂🅾🆁🆂 🅶🅰🅼🅴")
answer=input("do you know the rules of this game enter help to know it").lower()
if answer=="help":
 print("""
        1)rock breaks scissors
        2)paper covers up the rock
        3)scissors cut the paper
        """)
choice=input("choose Rock or Paper or Scissors").lower()
if choice not in ["rock","paper","scissors"]:
 print("please choose rock or paper or scissors")
computer_choice=random.choice(["rock","paper","scissors"])
if choice=="rock":
  print(f"you chose {rock}")
elif choice=="paper":
  print(f"you chose {paper}")
else:
  print(f"you chose {scissors}")
if computer_choice=="rock":
  print(f"AI {rock}")
elif computer_choice=="paper":
  print(f"AI {paper}")
else:
  print(f"AI {scissors}")







if computer_choice==choice:
  print("draw")
elif choice=="paper"and computer_choice=="rock"or choice=="rock"and computer_choice=="scissors"or choice=="scissors"and computer_choice=="paper":
 print(f"{choice} beats {computer_choice}")
 print("you win")
else:
 print(f"{computer_choice} beats {choice}")
 print("you lost")
