from turtle import *
import time
import random
import math
colormode(255)

tracer(0)
ht()


SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2


class Ball(Turtle):
	def __init__(self,dx,dy):
		Turtle.__init__(self)
		self.pu()
		self.ht()
		self.goto(0, -SCREEN_HEIGHT + 50)
		self.st()
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		global r
		r = 10
		self.shapesize(r/10)
		red = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(red,g,b)
	def move(self,screen_width, screen_hight):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + r 
		left_side_ball = new_x - r
		bottom_ball = new_y - r
		upper_ball_side = new_y + r
		self.goto(new_x, new_y)
		if bottom_ball < -screen_hight or upper_ball_side > (screen_hight - 3*r):
			self.dy *= -1
		elif left_side_ball < (-screen_width + 3*r) or right_side_ball > (screen_width - 3*r):
			self.dx *= -1

class Square(Turtle):
	def __init__(self, health, serial_number):
		Turtle.__init__(self) 
		self.health = health
		self.serial_number = serial_number
		self.color("Pink")
		global r
		r = 10
		global SCREEN_WIDTH
		square_size = ((SCREEN_WIDTH*2 - 6*r)/6)
		self.begin_poly()
		self.pu()
		
		for i in range(4):
			self.pu()
			fd(square_size - 10)
			left(90)
		self.end_poly()
		p = self.get_poly()
		register_shape("poly",p)
		self.pd()
		self.shape("poly")
	def life(health):
		pu()
		fd(-square_size*0.5 - 5)
		left(90)
		fd(square_size*0.5 - 5)
		write(1)
		fd(-square_size*0.5 + 5)
		right(90)
		fd(square_size*0.5 + 5)


SQUARE = []		
def create(r, SCREEN_WIDTH, SCREEN_HEIGHT):
	global square_size
	square_size = ((SCREEN_WIDTH*2 - 6*r)/6)
	st()
	
	b = 0
	for i in range(4):
		pu()
		goto(-SCREEN_WIDTH + 2*r, SCREEN_HEIGHT - (i+1)*square_size)
		goto(-SCREEN_WIDTH + 3*r, SCREEN_HEIGHT - (i+1)*square_size)
		for square in range(6):
			b+=1
			pd()
			square = Square(3,b)
			pu()
			fd(square_size)
			pd()
			SQUARE.append(square)
			square.life()
			print("new square")
			ht()

create(10, SCREEN_WIDTH, SCREEN_HEIGHT)




NUMBER_BALLS = 1 



Balls = []
global Create1 
Create1 = NUMBER_BALLS
def create_ball(Create1):
	global NUMBER_OF_BALLS
	global Balls
	NUMBER_OF_BALLS = 1
	for i in range(NUMBER_OF_BALLS):
		# print("hello")
		x = 0
		y = -SCREEN_HEIGHT + 50
		dx = event.x - SCREEN_WIDTH - x
		dy = SCREEN_HEIGHT - event.y - y
		
		new_ball = Ball(dx/100, dy/100)
		Balls.append(new_ball)
		new_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

		print("new ball")
		
		if new_ball.xpos()== plus_square.xpos():
			NUMBER_BALLS = NUMBER_BALLS + 1 
getcanvas().bind("<Button-1>", create_ball)

while True:
	print(len(Balls))
	for ball in Balls:
		# time.sleep(0.0077)
		if ball.ycor() >= (-SCREEN_HEIGHT + 50):
			ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
		else:
			ball.goto(0,-SCREEN_HEIGHT + 49)
	getscreen().update()
# Ball1 = Ball(1,1) 
# while True:
# 	Ball1.move(SCREEN_WIDTH, SCREEN_HEIGHT)
# create_ball(event)
# create_ball(event)

#ball colision check:
#sides of the ball:
ball.top = ball.xpos()+radius 
ball.bottom = ball.xpos()-radius 
ball.right = ball.ypos()+radius 
ball.left = ball.ypos()-radius  
#sides of the square:

def top(self):
	return self.ycor()+self.height
def bottom(self):
	return self.ycor()
def right(self):
	return self.xcor()+self.width
def left(self):
	return self.xcor()

def check_collision(ball,box):
	#print(r1.height())
	if (ball.top() >= box.bottom() and 
		ball.right() >= box.left() and 
		ball.bottom() <= rbox.top() and 
		ball.left() <= box.right()):
		print("the rectangles collide")
		return True 
	else :
		print("the rectangles don't coolide")
		return False 


if check_collision == True:
	#number in box go down by one
	box_number = box_number -1 
	ball.dx = ball.dx - 45
	#(does this work???) 

	# ball angle to change and move in the other direction 






mainloop()