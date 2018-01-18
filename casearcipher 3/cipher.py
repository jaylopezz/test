while True:
  userName=input("What is your name?")
  if not (userName.isalpha()):
    print('You can only put letters.')
  else:
    print("Hello" +" " + userName+ "!")
    break

def alert():
    while True:
        userAlert=input('Input your message: ')
        if not(userAlert.isalpha()):
            print('You must only put letters.')
        else:
            print('Your message is "' + str(userAlert) + '".')
            return userAlert
            break

def key():
    while True:
        userKey=input('How would you like to shift the letters? 3-25: ')
        if not(userKey.isnumeric()):
            print('Only insert numbers!!')
        elif(int(userKey)<3 or int(userKey)>25):
            print('Error! Only shift letters from 3-25.')
        else:
            return userKey
            break

def encrypt():
  cipher=''
  for character in userAlert:
    if character == ' ':
      cipher += character

    else:
      integerValue = ord(character)
      integerValue -=  97
      integerValue += int(userKey)
      integerValue %= 26
      integerValue += 97
      cipher += chr(integerValue)
  print(cipher)


def decrypt():
  cipher=''
  for character in userAlert:
    if character == ' ':
      cipher += character

    else:
      integerValue = ord(character)
      integerValue -=  97
      integerValue -= int(userKey)
      integerValue %= 26
      integerValue += 97
      cipher += chr(integerValue)
  print(cipher)






userAnswer=''


userAnswer=input('Do you want to encrypt or decrypt your message? Enter e to encrypt, d to decrypt: ')
if userAnswer == 'e':
  userAlert = alert()
  userKey = key()
  encrypt()

elif userAnswer == 'd':
  userAlert = alert()
  userKey = key()
  cipher=''
  decrypt()
