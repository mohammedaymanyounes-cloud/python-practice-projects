books=[]
book=input("enter a name of a book you own\n").lower()
books.append(book)
if book:
  book1=input("enter the name of another book or press (Enter)to skip")
  if book1:
    books.append(book1)
    print("   ")
    print("    ")
    print(f"you have {books}")
  else:
    input("enter")
    print("   ")
    print("    ")
    print(f"you have{books}")
    
else:
  print("you forgot to enter the name of your book")
  print(" ")
book2=input("enter the name of a book you wish to have in the future")
book3=input("if you want to add another book go on or press (Enter) to ski[")
wish=[]
wish.append(book2)
wish.append(book3)
if book3:
  books.append(book3)
  print(f"now you have {books}")
  print(" ")
  print("  ")
  print(f"your wishlist includes {wish}")
else:
  print(f"you have {books}")
  print("  ")
  print("   ")
  print(f"your wishlist includes {wish}")
  input("enter")
book4=input("enter the name of a book from your wishlist that you have quired or press(Enter)")
if book4:
 if book4 in wish:
  wish.remove(book4)
  print(f"your wishlist includes{wish}")
 else:
   print("it does not exist")
else:
 input("Enter")
print("  ")
print("  ")
donate=input("enter the name of a book that you will donate or press(Enter)")
if donate in books:
  books.remove(donate)
  print(f"you have after this donation {books}")
else:
  input("Enter")