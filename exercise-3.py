# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
dog_human_age = int(input("Input a dog's age in human years: "))
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
if dog_human_age < 3:
    dog_age = dog_human_age * 10
#      - Any remaining years count as 7 years each
else:
    dog_age = (dog_human_age - 2) * 7
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
print(f"The dog's age in dog years is {dog_age}")

# Hint:  Use the int() function to convert the string returned from input() into an integer