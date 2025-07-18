#A programme that calculates the perimeter and area of a rectangle

'''
area of rectangle = l x b
perimeter of rectangle = 2(l + b)
'''

def calculate_area(len, width):
    return len * width

def calculate_perimeter(len, width):
    return 2 * (len + width)

'''
for area in calculate_area:
    if area == 0:
        print()
'''

while True:

    len = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = calculate_area(len, width)
    print(f"Area of the rectangle: {area}")

    perimeter = calculate_perimeter(len, width)
    print(f"Perimeter of the rectangle: {perimeter}")

    choice = input("Do you want to calculate another rectangle? (yes/no):").strip().lower()
    if choice != 'yes':
        print("Goodbye!")
        break

#except ValueError:
#    print("Invalid input! Enter valid numbers for lenght and width.\n") 
