import os
import time
import random
image=("""PLAY: 21
 ___   ___   ___
|K  | |7  | |4  |
| ♠ | | ♦ | | ♦ |
|__K| |__7| |__4|
""") 

def show():
  print("choose a game to start....")
  print('''
  1-frogy
  2-twenty one
  3-snake
  ''')
def clear():
  os.system("cls" if os.name=='nt' else 'clear')
def add():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  card=random.choice(cards)
  return card
def calculate(cards):
  if sum(cards)==21 and len(cards )==2:
    return 0
  if 11 in cards  and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
def compare(user_score,computer_score):
  results={
    'draw':'draw🤦‍♂️\n\n',
    'user_over':'you went over 21 sorry... you lost😢',
    'computer_over':'computer went over 21 you won😍😍',
    'user_21':'you won with a black jack👏👏🎁',
    'computer_21':'computer had a black jack sorry you lost😒😒',
    'computer_win':'computer won🤦‍♀️',
    "user_win":'you won😆😆',
  }
  if user_score==computer_score:
    return results['draw']
  elif user_score>21:
    return results['user_over']
  elif computer_score>21:
    return results['computer_over']
  elif user_score==0:
    return results['user_21']
  elif computer_score==0:
    return results['computer_21']
  elif user_score>computer_score:
    return results['user_win']
  else:
    return results['computer_win']
def game():
  user_cards=[add() for _ in range(2)]
  computer_cards=[add() for _ in range(2)]
  game_continue=True
  while game_continue:
    user_score=calculate(user_cards)
    computer_score=calculate(computer_cards)
    print(f"your cards are {user_cards} current score is {sum(user_cards)}")
    print(f"computer`s first is card is {computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score>21 or computer_score>21:
      game_continue=False
    else:
      need=input('get another card (y or n)').lower()
      if need=='y':
        user_cards.append(add())
      else:
        game_continue=False
  while computer_score !=0 and computer_score<17:
    computer_cards.append(add())
    computer_score=calculate(computer_cards)
  print(f'your final hand : {user_cards} and your score is {user_score}')
  print(f"computer`s final hand: {computer_cards} and his score is {computer_score} ")
  print(compare(user_score,computer_score))

while input('choose a game to start.....\n\n1-frogy \n2-snake \n3-twenty one\n').lower()=="twenty one":
  
  game()  

