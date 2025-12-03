import pygame

pygame.init()

pygame.mixer.init

scrn_height = 800
scrn_width = 800

screen = pygame.display.set_mode((scrn_height, scrn_width))
pygame.display.set_caption('Python-paint v1.0')

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

white = (255, 255, 255)
black = (0, 0, 0)
whiteish = (245, 245, 245)
whiteish2 = (230, 230, 230)
whiteish3 = (210, 210, 210)
greyish1 = (150, 150, 150)
greyish2 = (75, 75, 75)

canvas = pygame.Surface((1000, 1000))
canvasrect = pygame.Rect(0, 95, 1000, 1000)
canvas.fill(white)

font1 = pygame.font.SysFont('Arial', 15)
font2 = pygame.font.SysFont('Arial', 20)

class TextBox():
	def __init__(self, x, y, width, height, label, maxval, startval):
		self.rect = pygame.Rect(x, y, width, height)

		self.textinput = startval

		self.text = font2.render(self.textinput, True, black)
		self.label = font2.render(str(label), True, black)

		self.maxval = maxval

	def get_sym(self):
		if self.rect.collidepoint((mouse_x, mouse_y)):
			if event.key == pygame.K_BACKSPACE:
				self.textinput = self.textinput[:-1]
				if self.textinput == '':
					self.textinput = '0'
			if event.unicode in numbers:
				if self.textinput == '0':
					self.textinput = event.unicode
				else:
					if int(str(self.textinput + event.unicode)) <= self.maxval:
						self.textinput += event.unicode
		self.text = font2.render(self.textinput, True, black)

r = TextBox(145, 21, 75, 22, 'R', 255, '0')
g = TextBox(145, 45, 75, 22, 'G', 255, '0')
bl = TextBox(145, 68, 75, 22, 'B', 255, '0')

get_erasersize = TextBox(375, 23, 71, 22, '', 1000, '32')
get_brushsize = TextBox(302, 23, 71, 22, '', 1000, '15')

class Brush():
	def __init__(self):
		self.brushsize = 15
		self.brushnum = 1

		self.erasersize = 32
b = Brush()

eraser = pygame.Rect(0, 0, b.erasersize, b.erasersize)

def sqrpaint():
	pygame.draw.rect(canvas, (int(r.textinput), int(g.textinput),\
	 int(bl.textinput)), (mouse_x - b.brushsize // 2, mouse_y - 95 - b.brushsize // 2, b.brushsize, b.brushsize))

def circpaint():
	pygame.draw.circle(canvas, (int(r.textinput), int(g.textinput), \
	 int(bl.textinput)), (mouse_x, mouse_y - 95), b.brushsize // 2)

circbrush = True
sqrbrush = False

def erase():
	if circbrush:
		pygame.draw.circle(canvas, white, (mouse_x, mouse_y - 95), b.erasersize // 2)
	if sqrbrush:
		pygame.draw.rect(canvas, white, (mouse_x - b.erasersize // 2, mouse_y - 95 - b.erasersize // 2, b.erasersize, b.erasersize))

# images HERE.
circleimg = pygame.image.load('circ.png')
circleselectimg = pygame.image.load('circ_selected.png')
squareimg = pygame.image.load('sqr.png')
squareselectimg = pygame.image.load('sqr_selected.png')

eraser_sizeimg = pygame.image.load('eraser_size.png')
brush_sizeimg = pygame.image.load('brush_size.png')

## toolbar ##
titlerect = pygame.Rect(0, 0, 90, 15)
title = font1.render('Paint: Python Edition v1.0', True, black)

circle = circleimg.get_rect()
circle.center = (107, 56)
square = squareimg.get_rect()
square.center = (36, 56)

erasersizerect = eraser_sizeimg.get_rect()
erasersizerect.center = (410, 69)
brushsizerect = eraser_sizeimg.get_rect()
brushsizerect.center = (337, 69)

color_canvas = pygame.Surface((150, 70))
color_blank = pygame.Rect(146, 20, 150, 71)

color_display = pygame.Rect(223, 22, 69, 69)

size_canvas = pygame.Surface((150, 70))
size_blank = pygame.Rect(299, 20, 150, 71)

toolbar_cover = pygame.Rect(0, 0, 800, 95)
##        ##

clock = pygame.time.Clock()
running = True
while running:
	clock.tick(125)
	screen.fill(whiteish)

	mouse_helders = pygame.mouse.get_pressed()
	mouse_x, mouse_y = pygame.mouse.get_pos() 
	mouse_move = pygame.mouse.get_rel()
	mouse_xmove = mouse_move[0]
	mouse_ymove = mouse_move[1]
	keys = pygame.key.get_pressed()

	eraser = pygame.Rect(mouse_x - b.erasersize // 2, mouse_y - b.erasersize // 2, b.erasersize, b.erasersize)

	b.erasersize = int(get_erasersize.textinput)
	b.brushsize = int(get_brushsize.textinput)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if circle.collidepoint(event.pos):
					circbrush = True
					sqrbrush = False
				if square.collidepoint(event.pos):
					sqrbrush = True 
					circbrush = False
		if event.type == pygame.KEYDOWN:
			r.get_sym()
			g.get_sym()
			bl.get_sym()

			get_erasersize.get_sym()
			get_brushsize.get_sym()

	if mouse_helders[0]:
		if canvasrect.collidepoint((mouse_x, mouse_y)):
			if circbrush:
				circpaint()
			if sqrbrush:
				sqrpaint()

	screen.blit(canvas, canvasrect)

	if mouse_helders[2]:
		if canvasrect.collidepoint((mouse_x, mouse_y)):
			if circbrush:
				pygame.draw.circle(screen, (100, 100, 100), (mouse_x, mouse_y), b.erasersize // 2)
			if sqrbrush:
				pygame.draw.rect(screen, (100, 100, 100), eraser)
			erase()

	pygame.draw.rect(screen, whiteish, toolbar_cover)

	screen.blit(title, titlerect)
	screen.blit(r.text, r.rect)

	if sqrbrush:
		screen.blit(squareselectimg, square)
		screen.blit(circleimg, circle)
	if circbrush:
		screen.blit(squareimg, square)
		screen.blit(circleselectimg, circle)

	pygame.draw.rect(screen, whiteish2, color_blank)
	pygame.draw.rect(screen, whiteish2, size_blank)

	screen.blit(brush_sizeimg, brushsizerect)
	screen.blit(eraser_sizeimg, erasersizerect)

	pygame.draw.rect(screen, whiteish3, r.rect)
	pygame.draw.rect(screen, whiteish3, g.rect)
	pygame.draw.rect(screen, whiteish3, bl.rect)
	pygame.draw.rect(screen, whiteish3, get_erasersize.rect)
	pygame.draw.rect(screen, whiteish3, get_brushsize.rect)

	pygame.draw.rect(screen, (int(r.textinput), int(g.textinput), int(bl.textinput)), color_display)

	screen.blit(r.text, (r.rect.x + 36, r.rect.y - 1))
	screen.blit(r.label, (r.rect.x + 6, r.rect.y - 1))

	screen.blit(g.text, (g.rect.x + 36, g.rect.y - 1))
	screen.blit(g.label, (g.rect.x + 6, g.rect.y - 1))

	screen.blit(bl.text, (bl.rect.x + 36, bl.rect.y - 1))
	screen.blit(bl.label, (bl.rect.x + 6, bl.rect.y - 1))

	screen.blit(get_erasersize.text, (get_erasersize.rect.x + 22, get_erasersize.rect.y - 1))
	screen.blit(get_brushsize.text, (get_brushsize.rect.x + 22, get_brushsize.rect.y - 1))

	pygame.display.flip()