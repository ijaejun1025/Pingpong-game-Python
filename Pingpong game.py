import turtle as t
import random
import time

# Background color and size
t.bgcolor("Lightblue")
t.setup(500, 700)

# Player
player = t.Turtle()
player.shape("square")
player.shapesize(1,5)
player.up()
player.speed(0)
player.goto(0,-270)

# Controller
def right():
    if player.xcor() < 200:
        player.forward(10)

def left():
    if player.xcor() > -200:
        player.backward(10)

t.listen()
t.onkeypress(right, "Right")
t.onkeypress(left, "Left")

# Ball
ball = t.Turtle()
ball.shape("circle")
ball.shapesize(1.3)
ball.up()
ball.speed(0)
ball.color("green")

# Scoreboard
life = 3
t.up()
t.hideturtle()
t.goto(0,300)
t.write(f"Life : {life}", False, "center", ("", 20))

# Game playing
ball_xspeed = 5
ball_yspeed = 5
game_on = True

while game_on:
    new_x = ball.xcor() + ball_xspeed
    new_y = ball.ycor() + ball_yspeed  
    ball.goto(new_x, new_y)

    # If the ball hits the right or left wall
    if ball.xcor() > 240 or ball.xcor() < -240:
        ball_xspeed *= -1

    # If the ball hits the ceiling
    if ball.ycor() > 340:
        ball_yspeed *= -1

    # If the player hits the ball
    if player.distance(ball) < 50 and -260 < ball.ycor() < -245:
        ball_yspeed *= -1

    # If the player fails to hit the ball (If the ball hits the floor)
    if ball.ycor() < -340:
        # Renew the scoreboard
        life -= 1
        t.clear()
        t.write(f"Life : {life}", False, "center", ("", 20))
        
        # Restart the game
        time.sleep(0.5)
        ball.goto(0,0)
        ball_xspeed *= -1
        ball_yspeed *= -1

        # Game over
        if life == 0:
            game_on = False
            t.goto(0,0)
            t.write("Game Over", False, "center", ("", 20))

t.exitonclick()