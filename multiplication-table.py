n_input = input("Enter the base number: ")
rang_input = input("Enter the range limit (press Enter for 10): ")


try:
    n = int(n_input)
except ValueError:
    print("Invalid base number. Please enter a whole number.")
    exit()


if rang_input.strip() == "":
    rang = 10
else:
    try:
        rang = int(rang_input)
    except ValueError:
        print("Invalid range. Please enter a whole number.")
        exit()


if rang < 1:
    print("Range limit must be 1 or greater.")
elif rang > 10000:
    print("Range limit is too large (max is 10,000).")
else:
    
    max_width = len(str(n * rang))

    for i in range(1, rang + 1):
        result = n * i
        print(f"{n} x {i:2} = {result:>{max_width}}")