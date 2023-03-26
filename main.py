import math

# Prompt user for number of days to simulate
days = input("Enter the number of days to simulate: ")

# Check that input is an integer
while not days.isdigit():
    days = input("Please enter an integer: ")

# Convert input to integer
days = int(days)

# Initialize starting amount
amount = 0.01

# Simulate doubling of penny for each day
for i in range(1, days + 1):
    # Update amount for current day
    amount *= 2
    # Print amount for current day
    if amount >= 1:
        # Print amount in dollars if it is 1 dollar or more
        if math.isclose(amount, 1.0):
            print(f"On day {i}, you have 1 dollar")
        else:
            print(f"On day {i}, you have ${amount:.2f}")
    else:
        # Print amount in cents if it is less than 1 dollar
        if math.isclose(amount, 0.01):
            print(f"On day {i}, you have 1 cent")
        else:
            print(f"On day {i}, you have {int(amount*100)} cents")
