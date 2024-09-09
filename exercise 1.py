name = input("Enter your name: ")
print("Hello " + name)
r = float(input("Enter your radius: "))
import math
area = math.pi * (r **2)
print("Area = ", area)
l = float(input("Enter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))
perimeter = 2 *(l + w)
area = l * w
print("Perimeter = ", perimeter)
print("Area = ", area)
LOT_TO_GRAM = 13.3
POUND_TO_GRAM = 32
TALENT_TO_POUND = 20
GRAM_IN_KILOGRAM = 1000
talents = float(input("Entaer talemts: "))
pounds = float(input("Entaer pounds: "))
lots = float(input("Entaer lots: "))
total_lots = (talents * pounds * lots)
total_grams = total_lots * LOT_TO_GRAM
kilograms = int(total_grams / GRAM_IN_KILOGRAM)
grams = total_grams % GRAM_IN_KILOGRAM
print(f"The weight in modern units: {kilograms: } kilograms and {grams} grams.")
n = []
for num in range(0,9):
    num = str(num).zfill(3)
    print(num)
    n.append(num)
    n1 = []
    for num in range (1,6):
        num = str(num).zfill(4)
        print(num)
        ni.append(num)
        length = float(input("Enter the length of the zander in centimeters"))
        size_limit = 42
        if length >= size_limit:
            print("The zander meets the size limit. You can keep the fish.")
        else:
            diffrence = length - size_limit
            print(f"The zander is {diffrence: .1f} centimeters below the size limit. Please release it back into the lake.")
cabin_class = input("Enter the cabin class (LUX, A,B,C): ").upper()
if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
if cabin_class == "A":
    print("A: above the car deck, equipped with a window.")
if cabin_class == "B":
    print("B: windowless cabin above the car deck.")
if cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
    gender = input("Enter your biological gender (male/female): ").lower()
    hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))
    if gender == "female":
        if hemoglobin_value < 117:
            print("your hemoglobin is too low.")
            elif 117 <= hemoglobin_value <= 155:
            print("Your hemoglobin value is normal.")
        else:
            print("Your hemoglobin value is high.")
            elif gender == "male":
            if hemoglobin_value < 134:
                print("Your hemoglobin is low.")
                elif 134 <= hemoglobin_value <= 167:
                print("Your hemoglobin value is normal.")
            else:
                print("Your hemoglobin value is high.")
            else:
            print("Invalid gender entered.")
            year = int(input("Enter year: "))
            if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")





