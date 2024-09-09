LOT_TO_GRAM = 13.3
POUND_TO_GRAM = 32
TALENT_TO_POUND = 20
GRAM_IN_KILOGRAM = 1000
talents = float(input("Enter talent: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
total_lots = (talents * pounds * lots)
total_grams = total_lots * LOT_TO_GRAM
kilograms = int(total_grams / GRAM_IN_KILOGRAM)
grams = total_grams % GRAM_IN_KILOGRAM
print(f"The weight in modern units: {kilograms:} kilograms and {grams:.2f} grams.")
n = []
for num in range(0,9):
    num = str(num).zfill(3)
    print(num)
    n.append(num)
    n1 =[]
    for num in range(1,6):
        num = str(num).zfill(4)
        print(num)
        n1.append(num)



