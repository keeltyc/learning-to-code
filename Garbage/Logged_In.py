
from Test_Login_Page import *
from time import sleep

Logged_In = False

def change_password(new_password):
    new_password = raw_input("Enter a new password: ")
    new_password = str.upper(new_password)
    if new_password == login_list[login]:
        print "That's the same as your existing password! Try again."
        sleep(0.5)
    elif len(new_password) > 12:
        print "That password is too long. Try again."
        sleep(0.5)
    elif len(new_password < 5):
        print "That password is too short. Try again."
        sleep(0.5)
    else:
        logins_list[login] = new_password

def logging_in():
    counter = 0
    if counter < 3:
            print "Welcome! Please choose an option:"
            print "L = Log In"
            print "C = Create Account"
            print "Q = Quit"
            print ""
            username = raw_input("?: ")
            username = str.upper(username)
    return login_screen()
    if Logged_In == True:
        print "Hello! What would you like to do?"
        print "C = Change my password"
        print "B = See some boobs"
        print "Q = Quit"
        print ""
        sleep(0.5)
        choice = raw_input("?: ")

        if choice == "C":
            change_password()

logging_in()