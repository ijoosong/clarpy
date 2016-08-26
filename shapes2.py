""""
1) keep looping until stopped
2) 3D surface areas (cube, sphere, pyramid)
3) multiple entries at once
4) return the biggest to smallest term

Here are some hints
1) Use a while loop.  while "stop" not in user_input: do something and then at the end of it, do user_input = input("would you like to do more or stop?")
2) Use the area function we had already
3) You could ask first!  user_input = input("Would you like to put in multiple shapes or just one shape?") 
And then you could say "separate them by spaces or commas" and then use what you did.  That's right!
4) You can do this :)
"""

shapes_list = ["square", "rectangle", "triangle", "cube", "sphere", "pyramid"]
user_input = input("Enter a shape: ")
user_list = user_input.split(" ")

for shape in shapes_list:
    for var in user_list:
        if var == shape:
            print("yes")
