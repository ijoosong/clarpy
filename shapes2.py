""""
1) keep looping until stopped
2) 3D surface areas (cube, sphere, pyramid)
3) multiple entries at once
4) return the biggest to smallest term
"""

shapes_list = ["square", "rectangle", "triangle", "cube", "sphere", "pyramid"]
user_input = input("Enter a shape: ")
user_list = user_input.split(" ")

for shape in shapes_list:
    for var in user_list:
        if var == shape:
            print("yes")