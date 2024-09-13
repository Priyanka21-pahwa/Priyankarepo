import random
num_dice = int(input("How many dice do you want to roll? "))
total_sum = 0
for _ in range(num_dice):
    roll = random.randint(1,6)
    total_sum += roll
print(f"The sum of the numbers rolled is: {total_sum}")


numbers = []
while True:
    user_input = input("Enter a number (or press Enter to finish): ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")
numbers.sort(reverse=True)
top_five_numbers = numbers[:5]
print("The five greatest numbers in descending order are:", top_five_numbers)

