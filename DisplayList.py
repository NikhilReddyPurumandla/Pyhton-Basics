#Display first and last color of given list

color_list = ["Red","Green","White" ,"Black"]

for color in color_list:
    if color == color_list[0]:
       print(color)
    elif color == color_list[3]:
        print(color)
    else:
        continue