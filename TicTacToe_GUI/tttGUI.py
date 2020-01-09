import pygame

pygame.init()
width=900
height=674

#Create a screen 800x600
screen=pygame.display.set_mode((width,height))

#Title and Icon
pygame.display.set_caption("Tic Tac Toe")
icon=pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)

#Player piece
player_x=pygame.image.load("x.png")
player_o=pygame.image.load("o.png")

#Background
back_ground=pygame.image.load("background.jpg")


#Functions
def player_piece(piece,x,y):
	screen.blit(piece,(x,y))


running=True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False

	screen.fill((200,20,200))
	screen.blit(back_ground,(0,0))
	player_piece(player_x,50,50)
	player_piece(player_x,250,255)
	player_piece(player_x,450,460)
	player_piece(player_o,450,250)
	player_piece(player_o,50,250)
	player_piece(player_o,450,50)
	pygame.display.update()
	



