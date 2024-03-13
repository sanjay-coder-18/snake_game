from turtle import Turtle

size=[20,40,60]
move_distance=20

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.all_snake=[]
        self.create_snake()

    def create_snake(self):
        
        for i in range(0,len(size)):
    
            turtle=Turtle(shape="square")
            turtle.color('white')
            turtle.penup()
            turtle.goto(x=size[i],y=0)
            self.all_snake.append(turtle)

    def reset(self):
        for i in range (0,len(self.all_snake)):
            self.all_snake[i].goto(1000,1000)
        self.all_snake.clear()
        self.create_snake()

    def extend(self):
        last_segment = self.all_snake[-1]
        turtle = Turtle(shape="square")
        turtle.color('white')
        turtle.penup()
        turtle.goto(last_segment.xcor(), last_segment.ycor())
        self.all_snake.append(turtle)

        


    def move(self):
        for i in range(len(self.all_snake)-1,0,-1):
            new_x=self.all_snake[i-1].xcor()
            new_y=self.all_snake[i-1].ycor()
            self.all_snake[i].goto(new_x,new_y)

        self.all_snake[0].forward(move_distance)

    
    def up(self):
        if self.all_snake[0].heading() != DOWN:
            self.all_snake[0].setheading(UP)

    
    def down(self):
        if self.all_snake[0].heading() != UP:
            self.all_snake[0].setheading(DOWN)

    def right(self):
        if self.all_snake[0].heading() != LEFT:
            self.all_snake[0].setheading(RIGHT)

    def left(self):
        if self.all_snake[0].heading() != RIGHT:
            self.all_snake[0].setheading(LEFT)
