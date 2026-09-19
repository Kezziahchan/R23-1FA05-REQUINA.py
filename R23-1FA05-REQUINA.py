import math

# Get the coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Get the coordinates of the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the differences between the coordinates
x_difference = x2 - x1
y_difference = y2 - y1

# Calculate the distance between the two points
distance = math.sqrt(
    math.pow(x_difference, 2) + math.pow(y_difference, 2)
)

# Display the result
print()
print(f"The distance between the two points is: {distance:.2f}")
