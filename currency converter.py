import os
import time

dollar=("""
            ______________
    __,.,---'''''              '''''---..._
 ,-'             .....:::''::.:            '`-.
'           ...:::.....       '
            ''':::'''''       .               ,
|'-.._           ''''':::..::':          __,,-
 '-.._''`---.....______________.....---''__,,-
      ''`---.....______________.....--
""")
exchange_rate={
  "":dollar,
  "USD":1.0,
  "EUR":.85,
  "EGB":30.9,
  "RMB":6.5,  
}
def clear():
  os.system("cls" if os.name==("nt") else "clear")
def show():
  print("welcome to 'currency converter':\n")
  for currency in exchange_rate:
    print(f"{currency}: {exchange_rate[currency]}")
def currency_converter():
  clear()
  show()
  convert_from=input("\nChoose a currency to convert from:").upper()
  while True:
    amount=float(input("Enter the amount"))
    if (input(f"you want to convert {amount}{convert_from} comfirm (y or n)"))=='y':
      break
  clear()
  show()
  convert_to=input("choose a currency to convert to").upper()
  print("analyzing your request....please wait")
  time.sleep(2)
  print(f"checking for {convert_to}`s best rates available....please wait")
  time.sleep(1)
  print(f"getting discount price for {convert_from} ....please wait")
  clear()
  if convert_from not in exchange_rate or convert_to not in exchange_rate:
    print("invalid currency. conversion caceled")
    time.sleep(2)
    currency_converter()
  new_rate=exchange_rate[convert_to]/exchange_rate[convert_from]
  converted_amount=amount*new_rate
  clear()
  print(f"preparing the deal from {convert_from} to {convert_to}")
  time.sleep(2)
  print(
    f"xchange rate: 1{convert_from}={new_rate} {convert_to}\n\n ")
  time.sleep(2)
  print(
    f"{amount} {convert_from} is equal to{round(converted_amount,2)} {convert_to}")
  time.sleep(1)
  if (input("do you accept this transaction (y or n"))=='y':
    print("transaction successful")
  else:
    print("transaction canceled")
  if input("do you want to make another conversion (y or n)")=='y':
    currency_converter()
  else:
    print("thanks for using currency converter")
currency_converter()    
 