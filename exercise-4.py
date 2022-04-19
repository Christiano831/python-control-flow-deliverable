# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
print("Enter the lengths of three side of a triangle: ")
#      a: 
first = input("First angle: ")
#      b:
second = input("Second angle: ")
#      c:
third = input("Third angle: ")
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
if first == second and first == third:
    print(f"A triangle with sides of {first}, {second}, & {third} is an equalateral triangle")
#      scalene - all three sides are unequal in length
elif first != second and first != third and second != third:
    print(f"A triangle with sides of {first}, {second}, & {third} is a scalene triangle")
#      isosceles - two sides are the same length
else:
    print(f"A triangle with sides of {first}, {second}, & {third} is an isosceles triangle")
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
