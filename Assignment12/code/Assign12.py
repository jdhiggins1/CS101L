import turtle  
class Point(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self,x1,y1,width,height,color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        

class BoxFill(Box):
    def __init__(self,x1,y1,width,height,color,fill_color):
        super().__init__(self,x1,y1,width,height,color)
        self.fill_folor = fill_color

    def draw_action(self):
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

        



b = BoxFill(4, 2, 100, 200, "red", "Blue")
b.draw()
