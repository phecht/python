password = ""
SAVEDPASSWORD="python123"
while password != SAVEDPASSWORD:
    password = input("Enter password:")
    if password == SAVEDPASSWORD:
        print("Your logged in!")
    else:
        print("Wrong password, try again!")