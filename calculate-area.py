# Write a Python program which accepts multiple integer for calculating area of some geometrical shapes like Circle, Square, rectangle etc.

Program code :
  
radius = int(input("Enter radius: "))
side_square = int(input("Enter side value of square: "))
side1_rec, side2_rec = int(input("Enter first side value of reactangle: ")), int(input("Enter second side value of reactangle: "))

print("")
print("Radius of circle is: "+str(radius), end = "\n")
print("Side of square is: "+str(side_square), end = "\n")
print("Both sides of rectangle are: "+str(side1_rec)+" and "+ str(side2_rec),end = "\n")

print("Area of circle is == 3.141 * radius * radius -> 3.141*(radius**2) \n ===>", (radius**2)*3.141, end = "\n")
print("Area of square is == side * side -> side_square**2\n ===> ", side_square**2, end = "\n")
print("Area of rectangle is == length * breadth -> side1_rec * side2_rec \n ===> ", side1_rec*side2_rec)


Output of the above code is:
  
Enter radius: 7
Enter side value of square: 12
Enter first side value of reactangle: 10
Enter second side value of reactangle: 16
Given integers for multiple options for calculating areas are below: 
Radius of circle is: 7
Side of square is: 12
Both sides of rectangle are: 10 and 16

Area of circle is == 3.141 * radius * radius -> 3.141*(radius**2) 
 ===> 153.909
Area of square is == side * side -> side_square**2
 ===>  144
Area of rectangle is == length * breadth -> side1_rec * side2_rec 
 ===>  160
