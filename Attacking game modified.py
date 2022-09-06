import turtle
import math
import time

#Boundary
Boundary = turtle.Turtle()
Boundary.penup()
Boundary.pensize(20)
Boundary.speed(0)
Boundary.goto(-450, -300)
Boundary.color("white")
Boundary.pendown()
Boundary.forward(900)
Boundary.left(90)
Boundary.forward(600)
Boundary.left(90)
Boundary.forward(900)
Boundary.left(90)
Boundary.forward(600)


#Screen size and color
window = turtle.Screen()
window.bgcolor("black")
window.setup(width=900, height=500)
window.tracer(0)

#Score
score_1 = -1
score_2 = -1


#The first player
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("yellow")
player_1.shapesize(stretch_wid=3, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)


#The second player
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("green")
player_2.shapesize(stretch_wid=3, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)

#Bullet player 1
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 40


#ready - ready to fire
#fire - bullet is firing
bulletcondition = "ready to shoot"

#Bullet for player 2
bullet_2 = turtle.Turtle()
bullet_2.color("green")
bullet_2.shape("circle")
bullet_2.penup()
bullet_2.speed(0)
bullet_2.setheading(90)
bullet_2.shapesize(0.5, 0.5)
bullet_2.hideturtle()

bullet_2speed = -40
bullet_2condition = "ready to shoot"

#Scoring system
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write("Player 1: 0     Player 2: 0", align = "center", font = ("Impact", 28, "normal"))

#Movement of the first player
def player_1_up():
    y = player_1.ycor()
    y += 50
    player_1.sety(y)

def player_1_down():
    y = player_1.ycor()
    y -= 50
    player_1.sety(y)

#Movement of the second player
def player_2_up():
    y = player_2.ycor()
    y += 50
    player_2.sety(y)

def player_2_down():
    y = player_2.ycor()
    y -= 50
    player_2.sety(y)

#Defining firing the bullet
def shoot_bullet():
    #Declare bullet as a global if it needs to change
    global bulletcondition
    if bulletcondition == "ready to shoot":
        bulletcondition = "shoot"
        #Move the bullet to the right
        x = player_1.xcor() + 10
        y = player_1.ycor()
        bullet.setposition(x, y)
        bullet.showturtle()

def shoot_bullet_2():
    global bullet_2condition
    if bullet_2condition == "ready to shoot":
        bullet_2condition = "shoot"
        #Move bullet 2
        x = player_2.xcor() 
        y = player_2.ycor()
        bullet_2.setposition(x-10, y)
        bullet_2.showturtle()

def bulletCollision(p1, p2):
    distance = math.sqrt(math.pow(p2.xcor()-p1.xcor(),2)) + math.sqrt(math.pow(p2.ycor()-p1.ycor(),2))
    if distance < 13:
        return True


#Key controls for player 1
window.listen()
window.onkeypress(player_1_up, "w")
window.onkeypress(player_1_down, "s")
window.onkeypress(shoot_bullet, "space")

#Key controls for player 2
window.listen()
window.onkeypress(player_2_up, "Up")
window.onkeypress(player_2_down, "Down")
window.onkeypress(shoot_bullet_2, "p")

while True:
    window.update()
    #Player boundaries
    if player_1.ycor() > 248:
        player_1.goto(-350, 248)
    if player_1.ycor() < -248:
        player_1.goto(-350, -248)
    if player_2.ycor() > 248:
        player_2.goto(350, 248)
    if player_2.ycor() < -248:
        player_2.goto(350, -248)
    #Move the bullet for player 1
    x = bullet.xcor()
    x += bulletspeed
    bullet.setx(x)

    #Check to see if the bullet has gone off the boundary.
    if bullet.xcor() > 355:
        bullet.hideturtle()
        bulletcondition = "ready to shoot"
    if bullet_2.xcor() < -355:
        bullet_2.hideturtle()
        bullet_2condition = "ready to shoot"


    #Bullet 2
    p = bullet_2.xcor()
    p += bullet_2speed
    bullet_2.setx(p)



    if bulletCollision(bullet, player_2):
        #Reset the bullet
        bullet.hideturtle()
        bulletcondition = "ready to shoot"
        bullet.setposition(360,0)
        #Reset player 2
        player_2.setposition(350, 0)
        score_1 += 1
        score.clear()
        score.write("Player 1: {}     Player 2: {}".format(score_1, score_2), align = "center", font = ("Impact", 28, "normal"))
      

    if bulletCollision(bullet_2, player_1):
        #Reset the bullet
        bullet_2.hideturtle()
        bullet_2condition = "ready to shoot"
        bullet_2.setposition(-340,0)
        #Reset player 2
        player_1.setposition(-350, 0)
        score_2 += 1
        score.clear()
        score.write("Player 1: {}     Player 2: {}".format(score_1, score_2), align = "center", font = ("Impact", 28, "normal"))

    if score_1 == 10:
        player_1.hideturtle();
        player_2.hideturtle();
        window.listen()
        player_1.setposition(1000, 1000)
        player_2.setposition(1100 , 1000)
        win_1 = turtle.Turtle()
        win_1.speed(0)
        win_1.color("white")
        win_1.penup()
        win_1.hideturtle()
        win_1.goto(0, 0)
        win_1.write("Player 1 is the winner", align = "center", font = ("Impact", 28, "normal"))
        GG_1 = turtle.Turtle()
        GG_1.speed(0)
        GG_1.color("yellow")
        GG_1.penup()
        GG_1.hideturtle()
        GG_1.goto(0, -175)
        GG_1.write("Good Game", align = "center", font = ("Impact", 36, "bold"))
        

    if score_2 == 10:
        player_1.hideturtle();
        player_2.hideturtle();
        window.listen()
        player_1.setposition(1000, 1000)
        player_2.setposition(1100 , 1000)
        win_2 = turtle.Turtle()
        win_2.speed(0)
        win_2.color("white")
        win_2.penup()
        win_2.hideturtle()
        win_2.goto(0, 0)
        win_2.write("Player 2 is the winner", align = "center", font = ("Impact", 28, "normal"))
        GG_2 = turtle.Turtle()
        GG_2.speed(0)
        GG_2.color("green")
        GG_2.penup()
        GG_2.hideturtle()
        GG_2.goto(0, -175)
        GG_2.write("Good Game", align = "center", font = ("Impact", 36, "bold"))
        
