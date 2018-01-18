import re

while True:
    password = (input("Please enter your password: "))
    if len(password) < 8:
        print("Ensure your password is atleast 8 characters!")
    elif re.search('[0-9]',password) is None:
        print("Please ensure your password has atleast 1 number")
    elif re.search('[A-Z]',password) is None:
        print("Make sure your password has a capital letter in it")
    elif re.search('[a-z]',password)is None:
        print("Make sure your password has a lower case letter in it")
    elif re.search('[!@#$%^&*()_+=-]',password) is None:
        print("Please include one special character!")
    else:
        print("Congrats, your password has been set")
        break
