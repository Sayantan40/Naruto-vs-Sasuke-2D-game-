# install the pygame module/library in your environment
# If using pycharm go to settings download the module from interpreter
# if using jupiter notebook use the below syntax
# import sys
# !{sys.executable} -m pip install pygame==2.1.0 or most current version


import pygame




pygame.init()

win = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Naruto VS Sasuke (SONU)")

walkRight = [pygame.image.load('pics\\NR2.png'), pygame.image.load('pics\\NR3.png'), pygame.image.load('pics\\NR1.png')]
walkLeft = [pygame.image.load('pics\\NL2.png'), pygame.image.load('pics\\NL3.png'), pygame.image.load('pics\\NL1.png')]

bg = pygame.image.load('pics\\bg.png')
stan = pygame.image.load('pics\\Nstanding.png')

Nh = pygame.image.load('pics\\Nh.png')
Sh = pygame.image.load('pics\\Sh.png')

clock = pygame.time.Clock()

bgm = pygame.mixer.music.load('pics\\theme.wav')

hitsound = pygame.mixer.Sound('pics\\hit.wav')

shurikensound=pygame.mixer.Sound('pics\\shuriken.wav')
pygame.mixer.music.play()


class player(object):

	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = 10
		self.isJump = False
		self.jumpheight = 10
		self.left = False
		self.right = False
		self.walkcount = 0
		self.standing = True
		self.hitbox = (self.x +10, self.y +5, 80, 80)
		self.health = 200

	def draw(self, win):
		if self.health >0:
			if self.walkcount +1 >=6:
				self.walkcount=0

			if not (self.standing):
				if self.left:
					win.blit(walkLeft[self.walkcount//2], (self.x, self.y))
					self.walkcount += 1

				elif self.right:
					win.blit(walkRight[self.walkcount//2], (self.x, self.y))
					self.walkcount += 1

			else:
				if self.right:
					win.blit(pygame.image.load('pics\\NR1.png'), (self.x, self.y))

				else:
					win.blit(pygame.image.load('pics\\NL1.png'), (self.x, self.y))

			self.hitbox = (self.x +10, self.y +5, 80, 80)
			Nbar2 = pygame.draw.rect(win,(255, 0, 0), (80, 40, 210, 25))
			Nbar = pygame.draw.rect(win,(255, 255, 0), (89, 45, self.health, 15))
            #pygame.draw.rect(win,(255,0,0).self.hitbox,2)
		else:
			text = font.render('Sasuke Wins', True, (255, 100, 10), (0, 0, 100))
			win.blit(text, (200, 200))
			win.blit(pygame.image.load('pics\\Nd.png'), (self.x,self.y))
			naruto.isJump=False
			pygame.K_SPACE=False

	def hit(self):
		if self.health >0:
			self.health -=5
		else:
			print("Naruto died")


class weapon():
	def __init__(self, x, y, width, height, facing):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.facing = facing
		self.vel = 8 * facing
		self.hitbox = (self.x, self.y, 40, 40)

	def draw(self, win):
		win.blit(pygame.image.load('pics\\shur.png'), (self.x, self.y))
		self.hitbox = (self.x, self.y, 40, 40)


class enemy(object):
	walkRightS = [pygame.image.load('pics\\SR2.png'), pygame.image.load('pics\\SR3.png'),
	              pygame.image.load('pics\\SR1.png')]
	walkLeftS = [pygame.image.load('pics\\SL2.png'), pygame.image.load('pics\\SL3.png'),
	             pygame.image.load('pics\\SL1.png')]

	def __init__(self, x, y, width, height, end):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		self.path = [self.x, self.end]
		self.speed = 8
		self.walkcount = 0
		self.hitbox = (self.x +10, self.y +5, 80, 80)
		self.health = 200

	def draw(self, win):
		self.move()
		if self.health >0:
			if self.walkcount +1 >= 6:
				self.walkcount = 0
			if self.speed > 0:
				win.blit(self.walkRightS[self.walkcount//2], (self.x, self.y))
				self.walkcount += 1

			else:
				win.blit(self.walkLeftS[self.walkcount//2], (self.x, self.y))
				self.walkcount +=1

			self.hitbox = (self.x +10, self.y +5, 80, 80)
			Sbar2 = pygame.draw.rect(win,(255, 0, 0), (410, 40, 210, 25))
			Sbar = pygame.draw.rect(win,(255, 255, 0), (410, 45, self.health, 15))

		else:
			self.speed = 0
			text = font.render('Naruto Wins ', True, (255, 100, 10), (0, 0, 100))
			win.blit(text, (200, 200))
			win.blit(pygame.image.load('pics\\Sd.png'), (self.x, self.y))

	def move(self):
		if self.speed >0:
			if self.x + self.speed < self.path[1]:

				self.x += self.speed

			else:
				self.speed = self.speed * -1
				self.walkcount = 0


		else:
			if self.x - self.speed > self.path[0]:
				self.x += self.speed

			else:
				self.speed = self.speed * -1
				self.walkcount = 0

	def hit(self):
		if self.health >0:
			self.health -=10
		else:
			print("Sasuke died")

run=True

def redrawgamewindow():
	win.blit(bg,(0, 0))
	naruto.draw(win)
	sasuke.draw(win)
	win.blit(Nh,(10, 10))
	win.blit(Sh,(600, 10))
	for shuriken in shurikens:
		shuriken.draw(win)

	pygame.display.update()


font = pygame.font.SysFont('Comicsans', 50, True)

naruto = player(10, 400, 100, 100)
sasuke = enemy(100, 400, 100, 100, 600)

shurikens = []

throwspeed = 0

run = True

while run:

	##### FRAME RATE  ####
	clock.tick(25)
	################

	if throwspeed >0:
		throwspeed += 1
	if throwspeed >3:
		throwspeed = 0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	if naruto.health >0 and sasuke.health >0:
		if naruto.hitbox[1] < sasuke.hitbox[1] + sasuke.hitbox[3] and naruto.hitbox[1] + naruto.hitbox[3] > \
				sasuke.hitbox[1]:

			if naruto.hitbox[0] + naruto.hitbox[2] > sasuke.hitbox[0] and naruto.hitbox[0] < sasuke.hitbox[0] + \
					sasuke.hitbox[
						2]:
				naruto.hit()
				hitsound.play()
	else:
		if naruto.health == 0:
			naruto.speed = 0

	for shuriken in shurikens:
		if sasuke.health >0:
			if shuriken.hitbox[1] + round(shuriken.hitbox[3] // 2) > sasuke.hitbox[1] and shuriken.hitbox[1] + round(
					shuriken.hitbox[3] // 2) < sasuke.hitbox[1] + sasuke.hitbox[3]:
				if shuriken.hitbox[0] + shuriken.hitbox[2] > sasuke.hitbox[0] and shuriken.hitbox[0] + shuriken.hitbox[
					2] < sasuke.hitbox[0] + sasuke.hitbox[2]:
					sasuke.hit()
					hitsound.play()
					shurikens.pop(shurikens.index(shuriken))


		else:
			sasuke.speed = 0

		if shuriken.x < 699 and shuriken.x > 0:
			shuriken.x += shuriken.vel
		else:
			shurikens.pop(shurikens.index(shuriken))


	keys=pygame.key.get_pressed()

	if keys[pygame.K_SPACE] and throwspeed==0:
		shurikensound.play()

		if naruto.left==True:
			facing=-1
		else:
			facing=1

		if len(shurikens)<5:
			shurikens.append(weapon(round(naruto.x+naruto.width//2),round(naruto.y+naruto.height//2),40,40,facing))
			throwspeed=1

	if keys[pygame.K_LEFT] and naruto.x>naruto.speed:
		naruto.x-=naruto.speed
		naruto.left=True
		naruto.right=False
		naruto.standing=False

	elif keys[pygame.K_RIGHT] and naruto.x<690-naruto.width-naruto.speed:
		naruto.x += naruto.speed
		naruto.left=False
		naruto.right=True
		naruto.standing=False


	else:


		naruto.standing=True
		naruto.walkcount=0







	if not (naruto.isJump):
		if keys[pygame.K_UP]:
			naruto.isJump=True
			naruto.right=False
			naruto.left=False
			naruto.walkcount=0

	else:
		if naruto.jumpheight>=-10:
			neg=1
			if naruto.jumpheight<0:
				neg=-1
			naruto.y-=(naruto.jumpheight**2)*0.5*neg
			naruto.jumpheight-=1

		else:
			naruto.isJump=False
			naruto.jumpheight=10



	redrawgamewindow()




pygame.quit()
