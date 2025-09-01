import random
import string
print("     let's make a strong password" )
password=[]
numbers=[]
srings=[]
punctuations=[]
length=int(input("how long password do you want?"))
length1=int(input("how many letters do you want?"))
length2=int(input("how many numbers do you want?"))
length3=int(input("how many punctuations do you want?"))
if length1+length2+length3==length:
  strings=random.choices(string.ascii_letters,k=length1)
  password.extend(strings)
  numbers=random.choices(string.digits,k=length2)
  password.extend(numbers)
  punctuations=random.choices(string.punctuation,k=length3)
  password.extend(punctuations)
  random.shuffle(password)
  the_real_password="".join(password)
  print(f"your password is {the_real_password}")
else:
  print("go back and check your password length")
  
  