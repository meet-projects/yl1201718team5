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
global box_score
box_score = 1
class Square(Turtle):
	def __init__(self, box_score):
		Turtle.__init__(self) 
		self.box_score = box_score
		box_score = 1
		global r
		r = 10
		global SCREEN_WIDTH
		max_square_size = int(((SCREEN_WIDTH*2 - 6*r)/6))
		self.pu()
		size = int(random.randint(1, max_square_size/10 - 5))
		self.shape("square")
		self.shapesize(size)
		red = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(red,g,b)
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
	def top(self):
		return self.ycor()+self.height
	def bottom(self):
		return self.ycor()
	def right(self):
		return self.xcor()+self.width
	def left(self):
		return self.xcor()


SQUARE = []		
square_pos_list = []




def create_square(box_score):
	for i in range(17):
		new_square = Square(4)
		SQUARE.append(new_square)
		new_x = random.randint(-SCREEN_WIDTH,SCREEN_WIDTH)
		new_y = random.randint(-SCREEN_HEIGHT + 50,SCREEN_HEIGHT)
		new_square.pu()
		new_square.goto(new_x, new_y)
		square_pos_list.append((new_x,new_y)) 

NUMBER_BALLS = 1 

Balls = []
def create_ball(event):
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
			Balls.append(ball)
			

			ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

			print("new ball")
			



def create_ball_no_event():
	global Balls
	while len(Balls) < 7:
		
		global NUMBER_OF_BALLS
		NUMBER_OF_BALLS = 7
		for i in range(NUMBER_OF_BALLS):
			# print("hello")
			x = 0
			y = -SCREEN_HEIGHT + 50
			dx = 0
			dy = 0
			
			ball = Ball(dx/100, dy/100)
			Balls.append(ball)
			

			ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

			print("new ball")
			
			
				
	

getcanvas().bind("<Button-1>", create_ball)



getscreen().update()

create_ball_no_event()

global r 
#ball colision check:
#sides of the ball:
for ball in Balls:
	ball.top = ball.xcor()+r 
	ball.bottom = ball.xcor()-r 
	ball.right = ball.ycor()+r 
	ball.left = ball.ycor()-r 
#sides of the square:



def check_collision(Balls,SQUARE):
	#print(r1.height())
	for ball in Balls:
		for box in SQUARE:
			if (ball.top >= box.bottom and ball.right >= box.left and ball.bottom <= box.top and ball.left <= box.right):
				print("the box + ball collide")
				box.box_score += -1
				ball.dx *= -1
				ball.dy *= -1
			return True 
		else :
			print("the ball + box don't coolide")
			return False 
		
if check_collision(Balls,SQUARE) == True:
	NUMBER_BALLS = NUMBER_BALLS + 1 


create_square(box_score)




def check_square_collision(SQUARE):
	for box1 in SQUARE:
		for box2 in SQUARE:
			if  box1 == box2:
				return False 

			if (box1.top >= box2.bottom and box1.right >= box2.left and box1.bottom <= box22.top and box1.left <= box2.right):
				new_x = random.randint(-SCREEN_WIDTH,SCREEN_WIDTH)
				new_y = random.randint(-SCREEN_HEIGHT + 50,SCREEN_HEIGHT)
				square1.pu()
				square1.goto(new_x, new_y)
				return True 
			else:
				return False 






while Running:
	#print(len(Balls))
	Running = check_collision(Balls,SQUARE)
	# time.sleep(0.0077)
	if ball.ycor() >= (-SCREEN_HEIGHT + 50):
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	else:
		ball.goto(0,-SCREEN_HEIGHT + 49)
		if check_collision == True:
			Running = True
		else:
			Running = False
	check_square_collision(SQUARE)

	getscreen().update()
create_ball()
mainloop()