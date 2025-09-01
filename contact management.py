contacts={}
while True :
  print("Contact management")
  print("(1)Add a contact")
  print("(2)View a contact")
  print("(3)Edit a contact")
  print("(4)Exit")
  answer=int(input("\nplease choose a number from 1 to 4"))
  if answer==1:
    id_contact=int(input("enter the contact ID"))
    contact_name=input("please type a name")
    while True:   
      contact_number=input("please type a phone number")
      if contact_number. isdigit():
        print("Great")
        break 
      else:
        print("it is not a number")
    print(f"\n\n{contact_name} is added successfully....\n\n")
    contacts[contact_name]={"tittle":contact_name}
    contacts[contact_number]={"phone number":contact_number}
    contacts[id_contact]={"the id":id_contact}
  elif answer==2:
   print(contacts)
  elif answer==3:
    varified_id=int(input("please enter his id"))
    if varified_id == contacts[id_contact]:
      new_name=input("enter a new name")
      new_number=input("enter a new phone number")
      contacts["number"]=new_number
      contacts["name"]=new_name
    else:
      print("please right the the id correctly")
    print("success")  
  elif answer==4:
    print("exiting.....")
    break  
  else:
    print("focus choose from 1 to 4")          
  
  