import os
library_catalog={}
def clear():
  os.system("cls" if os.name =="nt"else "clear")
def add_book():
  while True:
    clear()
    isbn=input("enter the isbn ")
    title=input("enter the title ")
    author=input("enter the author`s name")
    library_catalog[isbn]={
      "title":title,
      "author":author,"available":True
    }
    print(
      f"book: {title} by {author} with isbn {isbn} is added successfully")
    choice=input("do you want to add another book? (y or n)")
    if choice.lower()!="y":
      break
def check_out():
  while True:
    clear()
    isbn=input("inter the isbn")
    if isbn in library_catalog:
      
      if library_catalog[isbn]['available']:
        library_catalog[isbn]['available']=False
        print(
        f"book:{library_catalog[isbn]['title']} is checked out successfully")
      else:
        print("sorry... it is already taken")
    else:
      print("sorry... this book not found in our catalog")
    choice=input("do you want to check out another book? (y or n)")
    if choice.lower()!='y':
      break
def check_in():
  while True:
    clear()
    isbn=input("enter the isbn")
    if isbn in library_catalog:
      if not library_catalog[isbn]['available']:
        library_catalog[isbn]['available']=True
        print(
         f"book: {library_catalog[isbn]['title']} checked in successfully")
      else:
        print("this book is already here")
    else:
      print("this book not found")
    choice=input("do you want to check in another book? (y or n)")  
    if choice.lower()!='y':
      break
def book_list():
  while True:
    clear()
    for isbn in library_catalog:
      book_info=library_catalog[isbn]
      print(
        f"book: {book_info['title']},author:{book_info['author']},available: {book_info['available']}")
    choice=input("do you want to go to tho main manu(y or n)")
    if choice.lower=="y":
      break

while True:
  print("\n library catalog")
  print("(1)add book")
  print("(2)check out")
  print("(3)check in")
  print("(4)book list")
  print("(5)exit")
  choice=int(input("choose from 1 to 5"))
  if choice==1:
    add_book()
  elif choice==2:
    check_out()
  elif choice==3:
    check_in()
  elif choice==4:
    book_list()
  elif choice==5:
    print("exiting....")
    break
  else:
    print("your answer is not here .")
    
      

