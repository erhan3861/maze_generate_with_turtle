from turtle import *
from random import randint

wn = Screen()
wn.bgcolor("black")
wn.addshape("grass_wall.gif")
wn.addshape("cube.gif")
wn.addshape("straw.gif")
wn.addshape("stone.gif")
wn.addshape("ss.gif")
wn.addshape("so.gif")
wn.addshape("gb.gif")



box = Turtle()
box.shape("cube.gif")
box.up()

square = Turtle()
square.ht()
square.up()
square.color("yellow")
square.speed(0)

box_list = []

# function definition
def make_maze(x, y):
  box.goto(x, y)
  shape = textinput("shape", "enter shape name")
  tekrar = int(numinput("Tekrar sayısı", "iteration"))
  angle = int(numinput("Angle", "enter angle"))
  
  for i in range(tekrar):
    new_box = box.clone()
    new_box.seth(angle)
    new_box.shape(shape + ".gif")
    new_box.fd(i * 40)
    box_list.append(new_box)
  
  print(box_list)

wn.onscreenclick(make_maze)
