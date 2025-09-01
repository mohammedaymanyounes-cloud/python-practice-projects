import string


def encrypt(message,shift):
  encrypt_message=""
  alphabet=string.ascii_lowercase
  for letter in message:
    if letter.lower()in alphabet:
      original_posisition=alphabet.index(letter.lower())
      new_position=(original_posisition-shift)%26
      encrypt_letter=alphabet[new_position]
      if letter.isupper():
        encrypt_letter=encrypt_letter.upper()
        
      encrypt_message+=encrypt_letter
    else:
      encrypt_message+=letter
  print(encrypt_message)
user_message=input("inter the message")
user_number=int(input("inter the shift number"))
encrypt(message=user_message,shift=user_number)