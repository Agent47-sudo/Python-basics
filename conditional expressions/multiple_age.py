a = int(input("Enter your age: "))
#if statement number 1
if a%2 == 0:
    print("Your age is even.")
else:
    print("Your age is odd.")
# if statement number 2
if a >= 18:
    print("You are eligible to vote.\nPlease proceed to the voting booth.\nThank you for participating in the democratic process!")
elif a < 0:
    print("Invalid age entered. Please enter a valid age.")
elif a == 0:
    print("Please enter a valid age\n don't mess with me.")
else:
    print("You are not eligible to vote.\nPlease wait until you reach the age of 18.\nThank you for your interest in civic engagement!")