def area(shape):
    area = 0
    if shape == "triangle":
        base = input("Enter the length of the base: ")
        height = input("Enter the length of the height: ")
        area = (int(base)*int(height))/2
    elif shape == "square":
        side = input("Enter the length of the side: ")
        area = int(side)**2
    elif shape == "rectangle":
        height = input("Enter the length of the height: ")
        width = input("Enter the length of the width: ")
        area = int(height)*int(width)
    elif shape == "circle":
        radius = input("Enter the radius: ")
        area = 3.14*(int(radius)**2)
    print("The area is " + str(area))


def perimeter(shape):
    perimeter = 0
    if shape == "triangle":
        string = input("Enter the lengths of the three sides (spaces in between): ")
        a,b,c = string.split(" ")
        perimeter = int(a) + int(b) + int(c)
    elif shape == "square":
        side = input("Enter the length of the side: ")
        perimeter = int(side)*4
    elif shape == "rectangle":
        height = input("Enter the length of the height: ")
        width = input("Enter the length of the width: ")
        perimeter = 2*int(height) + 2*int(width)
    elif shape == "circle":
        radius = input("Enter the radius: ")
        perimeter = 2*3.14*int(radius)
    print("The perimeter is " + str(perimeter))


def choice(shape):
    choice = input("Do you want the area (a) or perimeter (p) of the %s? " % (shape))
    if choice == "area" or choice == "a":
        area(shape)
    elif choice == "perimeter" or choice == "p":
        perimeter(shape)
    else:
        print('error')


shapes = ["triangle","square","rectangle","circle"]
user_shape = input("Enter a shape: ")
if user_shape != shapes:
    user_shape = input("Error. Enter triangle, square, rectangle, or circle: ")


choice(user_shape)

