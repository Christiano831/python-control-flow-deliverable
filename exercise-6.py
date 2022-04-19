# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
month = input("Enter the month of the year (Jan - Dec): ")
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
day = int(input("Enter the day of the month: "))
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
# if month in ("Dec", "Jan", "Feb", "Mar"):
if month == "Dec" and day > 20:
    print(f"{month} {day} is in Winter")
elif month == "Jan":
    print(f"{month} {day} is in Winter")
elif month == "Feb":
    print(f"{month} {day} is in Winter")
elif month == "March" and day < 20:
    print(f"{month} {day} is in Winter")

#      Mar 20 - Jun 20: Spring
elif month == "March":
    print(f"{month} {day} is in Spring")
elif month == "Apr":
    print(f"{month} {day} is in Spring")
elif month == "May":
    print(f"{month} {day} is in Spring")
elif month == "Jun" and day < 21:
    print(f"{month} {day} is in Spring")
elif month == "Jun":

#      Jun 21 - Sep 21: Summer
    print(f"{month} {day} is in Summer")
elif month == "Jul":
    print(f"{month} {day} is in Summer")
elif month == "Aug":
    print(f"{month} {day} is in Summer")
elif month == "Sep" and day < 22:
    print(f"{month} {day} is in Summer")
elif month == "Sep":

#      Sep 22 - Dec 20: Fall
    print(f"{month} {day} is in Fall")
elif month == "Nov":
    print(f"{month} {day} is in Fall")
elif month == "Dec":
    print(f"{month} {day} is in Fall")
else:
    print(f"You didn't enter the proper format")
    
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.