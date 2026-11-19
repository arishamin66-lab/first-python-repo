while True:
    user_input = input("Enter any positive number: ")
    try:
        a = int(user_input)
        break
    except ValueError:
        print("Your input is not a number. Please try again.")

if a < 0:
    print("Your input is negative")
elif a == 0 or a % 2 == 0:
    print("Your input is even")
else:
    print("Your input is odd")