""""
1) keep looping until stopped
2) 3D surface areas (cube, sphere, pyramid)
3) multiple entries at once
4) return the biggest to smallest term
"""

def perimeter(shape, list, index):
    perimeter = 0
    if shape == "triangle":
        a = list[index + 1]
        b = list[index + 2]
        c = list[index + 3]
        perimeter = int(a) + int(b) + int(c)
    elif shape == "square":
        side = list[index + 1]
        perimeter = int(side)*4
    elif shape == "rectangle":
        height = list[index + 1]
        width = list[index + 2]
        perimeter = 2*int(height) + 2*int(width)
    elif shape == "circle":
        radius = list[index + 1]
        perimeter = 2*3.14*int(radius)
    return perimeter


def area(shape, list, index):
    area = 0
    if shape == "triangle":
        base = list[index + 1]
        height = list[index + 2]
        area = (int(base)*int(height))/2
    elif shape == "square":
        side = list[index + 1]
        area = int(side)**2
    elif shape == "rectangle":
        height = list[index + 1]
        width = list[index + 2]
        area = int(height)*int(width)
    elif shape == "circle":
        radius = list[index + 1]
        area = 3.14*(int(radius)**2)
    return area


def surface_area(shape, list, index):
    sa = 0
    if shape == "cube":
        edge = list[index + 1]
        sa = 6 * (int(edge)**2)
    elif shape == "sphere":
        radius = list[index + 1]
        sa = 4 * 3.14 * (int(radius)**2)
    elif shape == "cone":
        radius = list[index + 1]
        height = list[index + 2]
        sa = 3.14 * int(radius) * (int(radius) * ((int(height)**2 + int(radius)**2)**.5))
    return sa


shapes_list = ["circle", "square", "rectangle", "triangle", "cube", "sphere", "cone"]


def do_work():
    keep_going = "yes"
    while keep_going == "yes":
        user_input2 = input("Do you want to find perimeter (p), area (a), or surface area (sa)? ")
        user_input1 = input("Enter shape(s): ")
        user_list = user_input1.split(" ")

        shapes = []
        for var in user_list:
            if var in shapes_list:
                x = user_list.index(var)
                if user_input2 == "perimeter" or user_input2 == "p":
                    per = perimeter(var, user_list, x)
                    shapes.append((var, per))
                elif user_input2 == "area" or user_input2 == "a":
                    ar = area(var, user_list, x)
                    shapes.append((var, ar))
                elif user_input2 == "surface area" or user_input2 == "sa":
                    sa = surface_area(var, user_list, x)
                    shapes.append((var, sa))

        length = len(shapes)
        if length > 1:
            shapes = sorted(shapes, key=lambda value: int(value[1]), reverse=True)
            print("Greatest value to the least are the following: ")
            z = 0
            while z < length:
                print(str(shapes[z][0]) + "(" + str(shapes[z][1]) + ")")
                z += 1
        elif length == 1:
            print(str(shapes[0][0]) + "(" + str(shapes[0][1]) + ")")

        keep_going = input("keep going? ")



do_work()
