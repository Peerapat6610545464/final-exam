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
        self.polygon_side = polygon_side
        self.num_polygon = random.randint(0, 20)
        self.polygon_list = []
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        for i in range(self.num_polygon):
            self.polygon_side = polygon_side
            self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            self.size = random.randint(50, 150)
            self.orientation = random.randint(0, 90)
            self.location = [random.randint(-300, 300), random.randint(-200, 200)]
            self.border_size = random.randint(1, 10)
            self.polygon_list.append(
                Polygon(polygon_side, self.color, self.size, self.orientation, self.location, self.border_size))

    def run(self):
        while (True):
            turtle.clear()
            for i in range(self.num_polygon):
                self.polygon_list[i].draw_polygon()
            turtle.update()


polygon_side = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: "))
simulator = Simulator(polygon_side)
simulator.run()



# polygon_side = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: "))
# if polygon_side == 1:
#     shape = draw(3)
#     shape.draw_polygon()
# if polygon_side == 2:
#     shape = draw(4)
#     print(shape.draw_polygon())
# if polygon_side == 3:
#     shape = draw(5)
#     print(shape.draw_polygon())

# draw a polygon at a random location, orientation, color, and border line thickness
# num_sides = random.randint(3, 5)  # triangle, square, or pentagon
# size = random.randint(50, 150)
# orientation = random.randint(0, 90)
# location = [random.randint(-300, 300), random.randint(-200, 200)]
# border_size = random.randint(1, 10)
#
# # specify a reduction ratio to draw a smaller polygon inside the one above
# reduction_ratio = 0.618
#
# # reposition the turtle and get a new location
# turtle.penup()
# turtle.forward(size * (1 - reduction_ratio) / 2)
# turtle.left(90)
# turtle.forward(size * (1 - reduction_ratio) / 2)
# turtle.right(90)
# location[0] = turtle.pos()[0]
# location[1] = turtle.pos()[1]
#
# # adjust the size according to the reduction ratio
# size *= reduction_ratio

# draw the second polygon embedded inside the original 


# hold the window; close it by clicking the window close 'x' mark
turtle.done()
