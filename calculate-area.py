# Write a Python program which accepts multiple integer for calculating area of some geometrical shapes like Circle, Square, rectangle etc.

Program code :
  
radius = int(input())
side_square = int(input())
side1_rec, side2_rec = int(input()), int(input())
print("Given integers for multiple options for calculating areas are below: ")
print("Radius of circle is: "+str(radius), end = "\n")
print("Side of square is: "+str(side_square), end = "\n")
print("Both sides of rectangle are: "+str(side1_rec)+" and "+ str(side2_rec))

print("Area of circle is == 3.141 * radius * radius -> 3.141*(radius**2) \n ===>", (radius**2)*3.141, end = "\n")
print("Area of square is == side * side -> side_square**2\n ===> ", side_square**2, end = "\n")
print("Area of rectangle is == length * breadth -> side1_rec * side2_rec \n ===> ", side1_rec*side2_rec)
