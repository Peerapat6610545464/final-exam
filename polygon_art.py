import turtle
import random


class Polygon:

    def __init__(self, polygon_side, color, size, orientation, location, border_size):
        self.sides = polygon_side
        self.color = color
        self.size = size
        self.orientation = orientation
        self.location = location
        self.border_size = border_size

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.left(360 / self.sides)
        turtle.penup()


class Simulator:
    def __init__(self, polygon_side):
        if art_num == 1:
            self.polygon_side = 3
        if art_num == 2:
            self.polygon_side = 4
        if art_num == 3:
            self.polygon_side = 5
        self.num_polygon = random.randint(25, 30)
        self.polygon_list = []
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        for i in range(self.num_polygon):
            if art_num == 4:
                self.polygon_side = random.randint(3, 5)
            self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            self.size = random.randint(50, 150)
            self.orientation = random.randint(0, 90)
            self.location = [random.randint(-300, 300), random.randint(-200, 200)]
            self.border_size = random.randint(1, 10)
            self.polygon_list.append(
                Polygon(self.polygon_side, self.color, self.size, self.orientation, self.location, self.border_size))

    def run(self):
        while (True):
            turtle.clear()
            for i in range(self.num_polygon):
                self.polygon_list[i].draw_polygon()
            turtle.update()


art_num = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: "))
simulator = Simulator(art_num)
simulator.run()
# import turtle
# import random
#
#
# class Polygon:
#
#     def __init__(self, polygon_side, color, size, orientation, location, border_size):
#         self.sides = polygon_side
#         self.color = color
#         self.size = size
#         self.orientation = orientation
#         self.location = location
#         self.border_size = border_size
#
#     def draw_polygon(self):
#         if self.sides in [3.1, 4.1, 5.1]:
#             if self.sides == 3.1:
#                 self.sides = 3
#             if self.sides == 4.1:
#                 self.sides = 4
#             if self.sides == 5.1:
#                 self.sides = 5
#                 Polygon.change_size(self)
#         turtle.penup()
#         turtle.goto(self.location[0], self.location[1])
#         turtle.setheading(self.orientation)
#         turtle.color(self.color)
#         turtle.pensize(self.border_size)
#         turtle.pendown()
#         for _ in range(self.sides):
#             turtle.forward(self.size)
#             turtle.left(360 / self.sides)
#             turtle.penup()
#
#     def change_size(self):
#         reduction_ratio = 0.618
#         turtle.penup()
#         turtle.forward(self.size * (1 - reduction_ratio) / 2)
#         turtle.left(90)
#         turtle.forward(self.size * (1 - reduction_ratio) / 2)
#         turtle.right(90)
#         self.location[0] = turtle.pos()[0]
#         self.location[1] = turtle.pos()[1]
#         self.size *= reduction_ratio
#
#
# class Simulator:
#     def __init__(self, art_num):
#         self.num_polygon = random.randint(25, 30)
#         self.polygon_list = []
#         turtle.speed(0)
#         turtle.bgcolor('black')
#         turtle.tracer(0)
#         turtle.colormode(255)
#         for i in range(self.num_polygon):
#             if art_num == 1:
#                 self.polygon_side = 3
#             if art_num == 2:
#                 self.polygon_side = 4
#             if art_num == 3:
#                 self.polygon_side = 5
#             if art_num == 4:
#                 self.polygon_side = random.randint(3, 5)
#             if art_num == 5:
#                 self.polygon_side = 3.1
#             if art_num == 6:
#                 self.polygon_side = 4.1
#             if art_num == 7:
#                 self.polygon_side = 5.1
#             for i in range(self.num_polygon):
#                 self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
#                 self.size = random.randint(50, 150)
#                 self.orientation = random.randint(0, 90)
#                 self.location = [random.randint(-300, 300), random.randint(-200, 200)]
#                 self.border_size = random.randint(1, 10)
#                 self.polygon_list.append(
#                     Polygon(self.polygon_side, self.color, self.size, self.orientation, self.location, self.border_size))
#
#     def run(self):
#         while (True):
#             turtle.clear()
#             for i in range(self.num_polygon):
#                 self.polygon_list[i].draw_polygon()
#             turtle.update()
#
#
# art_num = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: "))
# simulator = Simulator(art_num)
# simulator.run()
#
# turtle.done()
#
