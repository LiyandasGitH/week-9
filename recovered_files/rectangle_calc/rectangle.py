import calculate

len = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate.area(len, width)
perimeter = calculate.perimeter(len, width)
    
print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")
