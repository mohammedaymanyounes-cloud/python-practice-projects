import time
  
def check(email):  
  if "@"in email and "."in email:
    return True
  else:
    return False
def add_user(name,email):
  if check(email):
    print(f"user:{name} with email: {email} was added successfully added")
  else:
    print(f"user:{name} with email {email} isn`t validated")
  




user_name=input("what is your name")
user_email=input("Enter your address")
print("checking your user name please wait")
time.sleep(2)
print("validating your email address")
time.sleep(3)
add_user(user_name,user_email)
