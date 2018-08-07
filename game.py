import turtle
import math
import random

#set up the screen
windows = turtle.Screen()
windows.bgcolor('gray')

#draw boarder
border_pen = turtle.Turtle()
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.forward(680)
    border_pen.left(90)
border_pen.hideturtle()

#create turtle player 
player = turtle.Turtle()
player.shape('turtle')
player.penup()
player.speed(0)

#food section
food = turtle.Turtle()
food.color("red")
food.shape("circle")
food.penup()
food.speed(0)
food.setposition(-100,-100)

#set speed variable
speed = 1

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed+=1

def decreasespeed():
    global speed
    speed-=1


#set keyboard
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")
turtle.onkey(decreasespeed,"Down")

score = 0
while True:
    player.forward(speed)
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    
    if player.ycor() > 300 or player.ycor() < -300:
        player.left(180)
    
    distance = math.sqrt(math.pow(player.xcor()-food.xcor(),2) + math.pow(player.ycor() - food.ycor(),2))
    if distance < 20:
        food.setposition(random.randint(-300,300),random.randint(-300,300))
        score += 1
        print('{}'.format(score))
        #show score
        



    