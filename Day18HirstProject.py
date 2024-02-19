import colorgram
import turtle
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle.colormode(255)
cursor = turtle.Turtle()
color_list = [(171, 159, 143), (27, 133, 78), (23, 93, 139), (238, 220, 50), (140, 96, 60), (242, 220, 3), (169, 166, 38), (7, 107, 59), (165, 20, 52), (48, 166, 113), (126, 181, 141), (78, 19, 37), (154, 59, 90), (226, 231, 237), (220, 75, 59), (16, 55, 87), (138, 165, 184), (5, 88, 111), (190, 141, 159), (206, 76, 101), (204, 227, 211), (73, 33, 14), (27, 62, 120), (150, 29, 16), (231, 211, 220), (19, 63, 38), (86, 89, 11), (157, 216, 165), (58, 156, 171)]

# ht = hide turtle, can also use .hideturtle()
cursor.ht()
cursor.speed("fastest")
cursor.penup()
cursor.setheading(225)
cursor.forward(300)
cursor.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    cursor.dot(20, random.choice(color_list))
    cursor.forward(50)

    if dot_count % 10 == 0:
        cursor.setheading(90)
        cursor.forward(50)
        cursor.setheading(180)
        cursor.forward(500)
        cursor.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
