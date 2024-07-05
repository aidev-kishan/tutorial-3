import math
import sys
want = input("Be a King or Queen type yes : - ").lower()
if want == "yes":
    genders = input("Are you Load or lady : - load for type 'K' or lady for 'Q'").lower()
    name = input("What is your name? :- ").lower()
else:
    sys.exit()
def add_a_king(name, genders):
    if want == "yes":
        if genders == "k":
            print(f"King {name}!" )
        else:
            print(f"Queen {name}")
add_a_king(name, genders)

number = input("enter the number want to Square: - ")
number = float(number)
def calculate_square(number):
    square = number*number
    print(f"Square {square})!")
calculate_square(number)

print("features, version -1 ")
number_cubes = input("Enter the number you want to cube : -")
number_cubes = float(number_cubes)
def cube(numbers):
    cube = number_cubes*number_cubes*number_cubes
    print(cube)
cube(number_cubes)

print("The feature is complate and ready to go ")
print("gungun")