from turtle import *
import time
import random
import math
colormode(255)

tracer(0)
ht()

Running = True
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
	def __init__(self, box_score):
		Turtle.__init__(self) 
		self.box_score = box_score
		global r
		r = 10
		global SCREEN_WIDTH
		max_square_size = int(((SCREEN_WIDTH*2 - 6*r)/6))
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
		size = int(random.randint(10, max_square_size)/10)
		self.shapesize(size)
		box_score = size

	def life(box_score):
		pu()
		fd(-size*0.5 - 5)
		left(90)
		fd(size*0.5 - 5)
		write(box)
		fd(-size*0.5 + 5)
		right(90)
		fd(size*0.5 + 5)
		


SQUARE = []		
square_pos_list = []




def create_square(score):
	for i in range(17):
		new_square = Square(4)
		SQUARE.append(new_square)
		new_x = random.randint(-SCREEN_WIDTH,SCREEN_WIDTH)
		new_y = random.randint(-SCREEN_HEIGHT,SCREEN_HEIGHT)
		new_square.goto(new_x, new_y)
		square_pos_list.append((new_x,new_y)) 

NUMBER_BALLS = 1 

Balls = []	
global Create1 
Create1 = NUMBER_BALLS
def create_ball(Create1, event):
	global Balls
	while len(Balls) < 7:
		
		global NUMBER_OF_BALLS
		NUMBER_OF_BALLS = 7
		for i in range(NUMBER_OF_BALLS):
			# print("hello")
			x = 0
			y = -SCREEN_HEIGHT + 50
			dx = event.x - SCREEN_WIDTH - x
			dy = SCREEN_HEIGHT - event.y - y
			
			ball = Ball(dx/100, dy/100)
			Balls.append(new_ball)
			

			ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

			print("new ball")
			
			if ball.xpos()== plus_square.xpos():
				NUMBER_BALLS = NUMBER_BALLS + 1 

getcanvas().bind("<Button-1>", create_ball)



getscreen().update()




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

def check_collision(Balls,SQUARE):
	#print(r1.height())
	for ball in Balls:
		for box in SQUARE:
			if (ball.top() >= box.bottom() and ball.right() >= box.left() and ball.bottom() <= rbox.top() and ball.left() <= box.right()):
				print("the box + ball collide")
				box.score += -1
				ball.dx *= -1
				ball.dy *= -1
			return True 
		else :
			print("the rectangles don't coolide")
			return False 
		

create_ball()
create_square()

while Running:
	#print(len(Balls))
		Running = check_collision()
		# time.sleep(0.0077)
		if ball.ycor() >= (-SCREEN_HEIGHT + 50):
			ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
		else:
			ball.goto(0,-SCREEN_HEIGHT + 49)
			if check_collision == True:
				Running = True
			else:
				Running = False

mainloop()