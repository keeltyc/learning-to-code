"""
Just playing around, creating a login page, I think.abs

Author: Keeltyc
"""

from time import sleep

logins_list = {"KEELTYC":"@DINOSAUR"}


def login_test(username,password):

    Logged_In = False
    Active = True
    counter = 0
    while Logged_In == False and Active == True:
        if counter < 3:
            print "Welcome! Please choose an option:"
            print "L = Log In"
            print "C = Create Account"
            print "Q = Quit"
            print ""
            user_choice = raw_input("?: ")
            user_choice = str.upper(user_choice)     
            if user_choice == "L":
                login = raw_input("Enter your username: ")
                login = str.upper(login)
                if login in logins_list:
                    sleep(0.5)
                    password = raw_input("Enter your password: ")
                    password = str.upper(password)
                    sleep(0.5)
                    if password == logins_list[login]:
                        print "Welcome, " + login + "! You are now logged in."
                        Logged_In = True
                        Active = False
                        sleep(1)
                    else:
                        print "Sorry, that login is incorrect. You have " + str(2 - counter) + " more tries."
                        counter +=1
                        continue
                else:
                    print "That user does not exist. You have " + str(2 - counter) + " more tries."
                    counter +=1
                    sleep(1)
                    continue   
            if user_choice == "C":
                print "You are creating a new account."
                print " "
                new_username = raw_input("Enter new username: ")
                new_username = str.upper(new_username)
                if new_username in logins_list:
                    print ""
                    print "Sorry, that username is taken."
                    sleep(0.5)
                    continue
                elif len(new_username) > 12:
                    print "That username is too long. Try again."
                    sleep(0.5)
                    continue
                elif len(new_username < 5):
                    print "That username is too short. Try again."
                    sleep(0.5)
                    continue
                else:
                    new_password = raw_input("Enter a new password: ")
                    if len(new_password) > 12:
                        print "That password is too long. Try again."
                        sleep(0.5)
                        continue
                    elif len(new_password < 5):
                        print "That password is too short. Try again."
                        sleep(0.5)
                        continue
                    else:
                        logins_list[new_username] = new_password
                        continue
            if user_choice == "Q":
                sleep (0.5)
                print ""
                print "Quitting. Goodbye!"
                Active = False
        else:
            sleep(1)
            print ""
            print "You have run out of tries. Fuck off, hacker!"
            print ""
            sleep(1)
            break
    else:
        Logged_In = True
        