from turtle import *
 
 #We want draw a house
 
 # step 1: draw a squre

width(7)

color("cyan")

speed(5)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#step 2: draw a door


forward(70)
left(90)

begin_fill()

forward(110)
right(90)

forward(60)
right(90)

forward(110)

end_fill()
 
# step 3: draw a roof

penup()
goto(200,200)
pendown()

color("red")

begin_fill()

right(150)
forward(200)
left(120)
forward(200)

end_fill()

# step 4:draw a window

color("brown")


penup()
goto(20,110)
pendown()
begin_fill()
left(120)
left(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)

end_fill()

penup()
goto(160,110)
pendown()
begin_fill()

right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)

end_fill()

exitonclick()

#end of drawing
