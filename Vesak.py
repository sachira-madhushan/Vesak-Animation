#vesak animation program using python turtle - developed by J.P.sachira madhushan
from turtle import *
from time import sleep
import turtle
import threading
import pygame
import colorsys as c
import time

bgcolor("black")
t = [Turtle(), Turtle()]
x = 6
colors = ["red", "yellow", "blue", "lime"]
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.title("Vesak Animation")

#play music in background
def music():
	# Initialize pygame mixer
	pygame.mixer.init()

	# Load music file
	pygame.mixer.music.load("Buddha.mp3")

	# Play music in a loop
	pygame.mixer.music.play(loops=-1)

#buddha image
def buddha():
	screen.bgpic("buddha.gif")
#buddha image end

#pattern 01 function
def Pattern01():
	for index, i in enumerate(t):
		i.speed(0)
		i.color("white")
		i.shape("circle")
		i.shapesize(0.3)
		i.width(3)
		i.pu()
		i.seth(90)
		i.fd(350)
		i.seth(-180)
		i.pd()
	t[0].pu()

	delay(0)
	speed(0)
	ht()
	sleep(4)
	for i in colors:
		color(i)
		for i in range(360):
			t[0].fd(x)
			t[0].lt(1)
			pu()
			goto(t[0].pos())
			pd()
			t[1].fd(2 * x)
			t[1].lt(2)
			goto(t[1].pos())
	
#pattern 01 function end

#pattern 02
def Pattern02():
	speed(15)
	r, g, b = 255, 0, 0
	penup()
	setpos(-25,25)
	pendown()
	for i in range(255*2):
	    colormode(255)
	    
	    if i < 255//3:
	        g += 3
	    elif i < (255*2)//3:
	        r -= 3
	    elif i < 255:
	        b += 3
	    elif i < (255*4)//3:
	        g -= 3
	    elif i < (255*5)//3:
	        r += 3
	    else:
	        b -= 3
	        
	    fd(50+i)
	    rt(91)
	    pencolor(r, g, b)
#end of pattern 02

#pattern 03
def Pattern03():
	t=turtle.Turtle()
	s=turtle.Screen()
	t.width(2)
	t.speed(15)

	col=('white','pink','cyan')
	for i in range (300):
	    t.pencolor(col[i%3])
	    t.forward(i*4)
	    t.right(121)
	t.clear()
#end of pattern 03

#pattern 04
def Pattern04():
	turtle. speed(0)
	turtle.pensize (2)
	col=('yellow','white','red','green','blue')
	for i in range(5):
		turtle.color (col[i])
		penup()
		setpos(-90,250)
		pendown()
		for i in range (36):
			for j in range (4):
				turtle. forward (200)
				turtle.right (90)
				turtle.right (10)
		clear()	

#end of pattern 04

#function that write happy vesak day
def Text():
	t = turtle.Turtle()
	t.font = ('Arial', 18)
	t.penup()
	t.goto(-220, -300)
	t.pendown()
	t.color('red')
	x=-350
	text = "Happy Vesak Day I'm Sachira Madhushan"
	for char in text:
		t.goto(x, -300)
		t.write(char, font=t.font)
		time.sleep(0.2)
		x+=20
#end of text function

#call all functions
music()
buddha()
Text()
Pattern04()
clear()
Pattern01()
clear()
Pattern02()
clear()
Pattern03()
clear()

#while loop to show happy vesak day msg infinitly without end the program
while True:
	clear()
	Text()
#End of the program