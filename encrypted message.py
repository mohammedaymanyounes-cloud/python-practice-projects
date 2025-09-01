import string


def encrypt(message,shift):
  encripted_message=""
  alphabet=string.ascii_lowercase
  for letter in message:
    if letter.lower() in alphabet:
      original_position=alphabet.index(letter.lower())
      new_positionsition=(original_position+shift)%26
      encrypted_letter=alphabet[new_positionsition]
      if letter.isupper():
        encrypted_letter=encrypted_letter.upper()
      encripted_message+=encrypted_letter
    else:
      encripted_message+=letter
  print(encripted_message)    

user_message=input("inter the message")

shift_numberer=int(input("inter the shift number"))
encrypt(message=user_message,shift=shift_numberer)
