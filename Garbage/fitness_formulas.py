
# Formulas for use in other calculations
# Author: Keeltyc

import datetime

def gender_inquiry():
    ask = str.lower(raw_input("Enter your gender (M or F)"))
    if ask == "m" or ask == "f":
        gender = ask
        return gender
    else:
        print "That is not a valid option."

def body_fat():
    bodyfatknown = raw_input("Do you know your body fat percentage? (Y/N) ")
    if str.lower(bodyfatknown) == "y":
        body_fat = .01 * float(raw_input("Enter your body fat percentage: "))
        return body_fat
    elif str.lower(bodyfatknown) == "n":
        body_fat = 0
        return body_fat
    else:
        print "That is not a valid response."

def bmr(weight,height,age,gender,lean_mass):
    if gender == "f":
        if body_fat == 0:
            bmr = 655 + (9.6 * (weight * 0.453592)) + (1.8 * (2.54 * height)) - (4.7 * age)
            return bmr
        elif body_fat != 0:
            bmr = 370 + (9.8 * lean_mass)
            return bmr
    elif gender == "m":
        if body_fat == 0:
            bmr = 66 + (13.7 * weight * 0.453592) + (5 * height * 2.54) - (6.8 * age)
            return bmr
        elif body_fat != 0:
            bmr = 370 + (9.8 * lean_mass)
            return bmr