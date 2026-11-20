VALID_UNITS = {"C", "F", "K"}

while True:
    unit_input = input("Enter the unit you wanna convert from. Type (C), (F) or (K): ").strip().upper()
    if unit_input not in VALID_UNITS:
        print("You wrote invalid source input. Please enter C, F, or K.")
        continue

    raw_temp = input("Enter the value you wanna convert: ").strip()
    try:
        temp_input = float(raw_temp)
    except ValueError:
        print("You wrote invalid value. Please enter a number.")
        continue

    user_input = input("Enter the unit you wanna convert to. Type (C), (F) or (K): ").strip().upper()
    if user_input not in VALID_UNITS:
        print("You wrote invalid target input. Please enter C, F, or K.")
        continue

    # Check against physical minimum (absolute zero)
    if (unit_input == "C" and temp_input < -273.15) or \
       (unit_input == "F" and temp_input < -459.67) or \
       (unit_input == "K" and temp_input < 0):
        print("Temperature cannot be below absolute zero. Try again.")
        continue

    break  # All inputs are valid

if unit_input == user_input:
    result = temp_input
elif unit_input == "C":
    result = (temp_input * 9 / 5) + 32 if user_input == "F" else temp_input + 273.15
elif unit_input == "F":
    result = (temp_input - 32) * 5 / 9 if user_input == "C" else (temp_input - 32) * 5 / 9 + 273.15
elif unit_input == "K":
    result = temp_input - 273.15 if user_input == "C" else (temp_input - 273.15) * 9 / 5 + 32

print(f"Result: {round(result, 2)} {user_input}")