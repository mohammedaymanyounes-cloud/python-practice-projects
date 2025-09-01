import time
import os


def clear():
  os.system('cls' if os.name == 'nt' else 'clear')


class member:

  def __init__(self, first_name, last_name, id, status='inactive'):
    self.first_name = first_name
    self.last_name = last_name
    self.id = id
    self.status = status

  def show(self):
    print(f"first name: {self.first_name}")
    print(f"last name: {self.last_name}")
    print(f"membership id: {self.id} ")
    print(f"status: {self.status}")
    print('-' * 20)


def create():
  first_name = input("Enter first name")
  last_name = input("Enter last name")
  id = input("Enter id membership")
  status = input(
      "Enter status (active or inactive) or you can click Enter to skip")
  if not status:
    status = 'inactive'
  return member(first_name, last_name, id, status)

#انشأ ليست لنضع فيها الاعضاء
members =[]


def search(members):
  print("search by \n")
  print("1-membership id")
  print("2-first name")
  print("3-membership status")

  search_choice = int(input("Enter your choice"))

  members_found = []

  if search_choice == 1:
    search_id = input("Enter the id to search")
    for x in members:
      if x.id == search_id:
        members_found.append(x)
        break
  elif search_choice == 2:
    first_name = input("Enter his first name")
    for x in members:
      if x.first_name.lower() == first_name:
        members_found.append(x)
  elif search_choice == 3:
    search_status = input("Enter his status (active or inactive)")
    for x in members:
      if x.status == search_status:
        members_found.append(x)
  if members_found:
    clear()
    print("members found")
    for x in members_found:
      x.show()
  else:
    print("member not found")
    time.sleep(2)


while True:
  clear()
  print("Wellcome to Gym membership management\n")
  print("1-Add member")
  print("2-display members")
  print("3-search for a member")
  print("4-Exit\n")

  choice = input("what do you want to do")

  if choice == '1':
    members.append(create())
    print("member added successfully")
    print(members)
  elif choice =='2':
    clear()
    if members:
      print("displaying members")
      for x in members:
        x.show()
    else:
      print("it`s empty")
      time.sleep(2)
  elif choice == '3':
    if members:
      search(members)
    else:
      print("no members to search")
      time.sleep(2)

  elif choice =='4' :
    print("Exiting...")
    break

  else:
    print("please choose from our options")
    print("choose from 1 to 4")
