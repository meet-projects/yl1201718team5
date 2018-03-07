from turtle import *
import time
import random
import math
colormode(255)

tracer(0)
ht()
goto(-338,100)
write("try to touch all of the boxes, in the least amount of moves, GOOD LUCK!", font=("Arial", 15, "normal"))
time. sleep(3)
clear()
Running = True
SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2


class Ball(Turtle):
	def __init__(self,dx,dy):
		Turtle.__init__(self)
		self.pu()
		self.ht()
		# self.goto(0, -SCREEN_HEIGHT + 50)
		self.st()
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.r = 10
		self.shapesize(self.r/10)
		red = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(red,g,b)
		self.new = True
	def move(self,screen_width, screen_hight):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		# print(self.right(), screen_width)
		# right_side_ball = new_x + self.r 
		# left_side_ball = new_x - self.r
		# bottom_ball = new_y - self.r
		# upper_ball_side = new_y + self.r
		if(self.ycor() < -SCREEN_HEIGHT + 50 and self.new):
			self.goto(0, current_y+1)
		else:
			self.goto(new_x,new_y)

		if(self.ycor() > -SCREEN_HEIGHT + 50 and self.new):
			self.new = False
		if self.top() >= (screen_hight):
			self.dy *= -1

		if self.left() <= (-screen_width) or self.right() > (screen_width):
			self.dx = self.dx * -1


	def top(self):
		return self.ycor() + self.r

	def bottom(self):
		return self.ycor() - self.r

	def right(self):
		return self.xcor() + self.r
		
	def left(self):
		return self.xcor() - self.r


global box_score
box_score = 1
class Square(Turtle):
	def __init__(self, box_score):
		Turtle.__init__(self) 
		self.box_score = box_score
		self.box_score = 1
		global r
		r = 10
		global SCREEN_WIDTH
		max_square_size = int(((SCREEN_WIDTH*2 - 6*r)/6))
		self.pu()
		self.size = int(random.randint(1, max_square_size/10 - 5))

		self.shape("square")
		self.shapesize(self.size)
		red = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(red,g,b)
		self.box_score = self.size

	def life(self):
		pu()
		fd(-self.size*0.5 - 5)
		left(90)
		fd(self.size*0.5 - 5)
		write(self.box_score)
		fd(-self.size*0.5 + 5)
		right(90)
		fd(self.size*0.5 + 5)

	def top(self):
		return self.ycor() + self.size*10

	def bottom(self):
		return self.ycor() - self.size*10

	def right(self):
		return self.xcor() + self.size*10

	def left(self):
		return self.xcor() - self.size*10


SQUARE = []		
square_pos_list = []




def create_square(box_score):
	for i in range(17):
		new_square = Square(4)
		# SQUARE.append(new_square)
		new_x = random.randint(-SCREEN_WIDTH,SCREEN_WIDTH)
		new_y = random.randint(-SCREEN_HEIGHT + 50,SCREEN_HEIGHT)
		new_square.pu()

		new_square.goto(new_x, new_y)
		collided = True
		while(collided):
			collided = False
			for square in SQUARE:
				if(collide(new_square, square) == True):
					new_x = random.randint(-SCREEN_WIDTH + 50,SCREEN_WIDTH - 50)
					new_y = random.randint(-SCREEN_HEIGHT + 70,SCREEN_HEIGHT - 30)
					new_square.goto(new_x, new_y)
					collided = True

		SQUARE.append(new_square)

# def check_square_col():
# 	for box1 in SQUARE:
# 			for box2 in SQUARE:
# 				if (box1.top() >= box2.bottom() and box1.right() >= box2.left() and box1.bottom() <= box2.top() and box1.left() <= box2.right()):
# 					return True
# 				else:
# 					return False



NUMBER_BALLS = 1 

Balls = []
def create_ball(event):
	print("creating a ball!")
	# global Balls
	while len(Balls) < 7: 
		# global NUMBER_OF_BALLS
		NUMBER_OF_BALLS = 7
		for i in range(NUMBER_OF_BALLS):
			# print("hello")
			x = 0
			y = -SCREEN_HEIGHT + 50 - (20*i)
			dx = event.x - SCREEN_WIDTH
			dy = SCREEN_HEIGHT - event.y - y
			dx = dx/300
			if dx < 0:
				dx = int(dx)
				if (dx == 0):
					dx = -1
			if dx > 0:
				dx = int(dx)
				if (dx == 0):
					dx = -1
			dy = dy/300
			dy = int(dy)
			if dy <= 0:
				dy = 1
			ball = Ball(dx, dy)
			# print(x,y)
			ball.goto(x,y)
			Balls.append(ball)

			# ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
			getscreen().update()

			print("new ball")
			



# def create_ball_no_event():
# 	global Balls
# 	while len(Balls) < 7:
# 		global NUMBER_OF_BALLS
# 		NUMBER_OF_BALLS = 7
# 		for i in range(NUMBER_OF_BALLS):
# 			# print("hello")
# 			x = 0
# 			y = -SCREEN_HEIGHT + 50
# 			dx = 0
# 			dy = 0
			
# 			ball = Ball(dx/100, dy/100)
# 			Balls.append(ball)
			

# 			ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

# 			print("new ball")
			
			
				
	

getcanvas().bind("<Button-1>", create_ball)


# create_ball_no_event()

global r 
#ball colision check:
#sides of the ball:
# for ball in Balls:
# 	ball.top = ball.xcor()+r 
# 	ball.bottom = ball.xcor()-r 
# 	ball.right = ball.ycor()+r 
# 	ball.left = ball.ycor()-r 
#sides of the square:

def collide(block1,block2):
	if(block1 == block2):
		return False
	if (block1.top() >= block2.bottom() and block1.right() >= block2.left() and block1.bottom() <= block2.top() and block1.left() <= block2.right()):
		return True
	return False


def check_collision(ball,box):
	#print(r1.height())
	if (ball.top() >= box.bottom() and ball.right() >= box.left() and ball.bottom() <= box.top() and ball.left() <= box.right()):
		print("the box + ball collide")
		box.ht()
		SQUARE.remove(box)
		ball.dy *= -1
		return True 
	else :
		print("the ball + box don't coolide")
		return False 

# if check_collision(Balls,SQUARE) == True:
# 	NUMBER_BALLS = NUMBER_BALLS + 1 


create_square(box_score)



while Running:
	#print(len(Balls))
	# Running = check_collision(Balls,SQUARE)
	# time.sleep(0.0077)
	for ball in Balls:
		for box in SQUARE:
			check_collision(ball,box)
	for ball in Balls:
		# if ball.ycor() >= (-SCREEN_HEIGHT + 50):
			# print("lol")
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
		if(ball.ycor() < -SCREEN_HEIGHT+50 and not ball.new):
			Balls.remove(ball)
			ball.ht()
		# else:
		# 	ball.ht()
		# 	Balls.remove(ball)
		# else:
		# 	ball.goto(0,-SCREEN_HEIGHT + 49)
		# 	if check_collision == True:
		# 		Running = True
		# 	else:
		# 		Running = False

	getscreen().update()
# create_ball()
# mainloop()