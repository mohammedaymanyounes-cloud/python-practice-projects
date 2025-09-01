import random

words=["world","ugly","good","happy"]
random_word=random.choice(words)
chances=6
hangman= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
display=["_"]*len(random_word)
print(" ".join(display))
print(hangman[0])   
guessed_letters=[]
while "_"in display and chances>0:
  guess=input("please guess a letter").lower()
  if guess in guessed_letters:
    print("u already guessed that try again")
    print(f"u have {chances} lives")

    continue
  guessed_letters.append(guess)  
  if guess not in random_word:
     chances-=1
     print(hangman[6-chances])
  else:  
   for position in range(len(random_word)):
     if random_word[position]==guess:
      display[position]=guess
  print(" ".join(display))
  print(f"you have {chances}chances")
if chances==0:
  print("""
  +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
  =========''']
  """)
  print("you lost")
else:
  print("you win")
