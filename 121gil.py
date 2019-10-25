# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random

#-----game configuration----
turtleshape = "turtle"
turtlesize = 10
turtlecolor = "blue"
score = (0)
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False




#-----initialize turtle-----
gil = trtl.Turtle(shape=turtleshape)
gil.color(turtlecolor)
gil.shapesize(turtlesize)
gil.speed(5)


score_writer = trtl.Turtle()
score_writer.ht()
score_writer.penup()
score_writer.goto(-370, 270)

font_setup = ("Arial" , 30,  "bold")
score_writer.write( score , font=font_setup)






#-----game functions--------
def change_position():
    gil.penup()
    gil.ht()
    if not timer_up:
     gilx = random.randint(-400, 400)
     gily = random.randint(-300, 300)
     gil.goto(gilx, gily)
     gil.st()


  





def update_score():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write( score , font=font_setup)

counter = trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(300,275)


def  gil_clicked(x,y):
    global turtlesize
    print("gil got clicked")
    change_position()
    update_score()
    turtlesize -=1
    gil.shapesize(turtlesize)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 













#-----events----------------



wn = trtl.Screen()

gil.onclick(gil_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
