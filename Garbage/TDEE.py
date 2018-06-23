
# Attempting a basic TDEE calculator
# Author: Keeltyc

from fitness_formulas import * 

gender = gender_inquiry()

age = (raw_input("What is your current age? "))

height = raw_input("What is your height in inches? ")

weight = float(raw_input("What is your current weight in pounds? "))

body_fat = body_fat()

lean_mass = weight * (1 - body_fat)

bmr = bmr(weight,height,age,gender,lean_mass)

print """
On a scale from 1 to 10,
how active would you say you are,
where 1 is completely sedentary
(like a desk job with no exercise)
and 10 is totally active (like a
full-time job in manual labor?)

"""

activity = raw_input("Enter your rating: ")

activity_factor = 1+ (float(activity) * 0.12)

tdee = float(bmr) * float(activity_factor)

bmr = int(bmr)
tdee = int(tdee)

print "    *** "
print "gender = " + gender
print "age = " + age + " years"
print "weight = " + str(weight) + " lbs"
print "lean mass = " + str(lean_mass) + " lbs"
print "height = " + str(height) + " inches"
print "bmr = " + str(bmr) + " calories per day"
print "activity rating = " + str(activity) + " out of 10"
print "    *** "
print "Total Daily Calories burned = " + str(tdee)
print "    *** "


ask = str.lower(raw_input("Would you like to Gain, Lose, or Maintain weight? "))

if ask == "lose":
    total_goal = float(raw_input("What is your goal weight? "))
    loss_goal = weight - total_goal
    weekly_goal = raw_input("How many pounds would you like to lose per week? ")
    daily_calories = tdee - ((float(weekly_goal) * 3500) / 7)
    if daily_calories < 1200:
        daily_difference = tdee - 1200
    elif daily_calories >= 1200:
        daily_difference = tdee - daily_calories

    daily_loss = daily_difference / 3500
    weekly_loss = (daily_difference * 7) / 3500

    weeks_to_goal = loss_goal / weekly_loss

    # Answer if a person wants to lose an unsafe amount of weight
    if float(weekly_goal) > 2.5:
        print "It is unsafe to lose more than 2.5 pounds per week."
        weekly_calorie_goal = float(3500 * float(2.5))
        if daily_calories >= 1200:
            print "To lose " + str(loss_goal) + " pounds in " + str(float(loss_goal) / float(weekly_goal)) + " weeks, you must consume " + str(weekly_calorie_goal) + " fewer calories per week."
            print "  "
            print "That means a maximum of " + str(tdee - (weekly_calorie_goal / 7)) + " calories per day."
        elif daily_calories < 1200:
            print "   "
            print "For basic nutritional needs, it is not safe to eat fewer than 1,200 calories per day."
            print "To safely lose " + str(loss_goal) + " pounds while consuming the minimum number of calories per day for basic nutrition,"
            print "will take you " + str(weeks_to_goal) + " weeks."
            print "   "
            print "By eating only 1,200 calories per day, you will lose " + str(weekly_loss) + " pounds per week."
    # Answer if a person's weight loss goal is reasonable
    elif float(weekly_goal) <= 2.5:
        weekly_calorie_goal = float(3500 * float(weekly_goal))
        if daily_calories >= 1200:
            print "To lose " + str(loss_goal) + " pounds in " + str(float(loss_goal) / float(weekly_goal)) + " weeks, you must consume " + str(weekly_calorie_goal) + " fewer calories per week."
            print "  "
            print "That means a maximum of " + str(tdee - (weekly_calorie_goal / 7)) + " calories per day."
        elif daily_calories < 1200:
            print "   "
            print "For basic nutritional needs, it is not safe to eat fewer than 1,200 calories per day."
            print "To safely lose " + str(loss_goal) + " pounds while consuming the minimum number of calories per day for basic nutrition,"
            print "will take you " + str(weeks_to_goal) + " weeks."
            print "   "
            print "By eating only 1,200 calories per day, you will lose " + str(weekly_loss) + " pounds per week."
elif ask == "gain":
    total_goal = float(raw_input("What is your goal weight?"))
    gain_goal = total_goal - weight
    weeks_needed = total_goal / 2.5
    print "You can safely gain " + str(gain_goal) + " pounds in " + str(gain_goal / 2.5) + " weeks."
    print "   "
    print "To do so, you must eat " + str(2.5*3500) + " more calories per week than you burn."
    print "   "
    print "That means consuming a minimum of " + str(tdee + (8750/7)) + " calories per day."
elif ask == "maintain":
    print "To maintain your current weight, try to consume around " + str(tdee) + " calories per day, or " + str(tdee * 7) + " calories per week."
    gain_or_lose = int(tdee)
else:
    print "That is not a valid response."
