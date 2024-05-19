from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

#tim.goto(-230,-100)

turtle_racers = []

colors = ["red", "orange", "yellow", "green", "blue", "violet"]


is_race_on = True
spacer = -100

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, spacer)
    new_turtle.stamp()
    new_turtle.write(color)
    spacer += 50
    turtle_racers.append(new_turtle)

num_racers = len(turtle_racers)

while is_race_on:
    for t in range(num_racers):
        turtle_racers[t].clear()
        speed = random.randint(10, 50)
        turtle_racers[t].forward(speed)
        if turtle_racers[t].xcor() > 230:
            winner = turtle_racers[t].pencolor()
            is_race_on = False

print(winner)


#
# for color in colors:
#     tim.color(color)
#     tim.goto(-230, spacer)
#     tim.stamp()
#     tim.write(color)
#     spacer += 50
#     turtle_racers[color] = tim.

#user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race")

# while is_race_on:
#     for tim in turtle_racers:
#         turtle_racers[tim].forward(100)




screen.exitonclick()


