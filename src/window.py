# import pygame module in this program
import pygame
import countdown
import time
pygame.init()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption("Jojo's Bizarre New Year")

font = pygame.font.Font('font.ttf', 32)

bg = pygame.image.load("assets/bg.png")

display_surface.blit(bg, (0, 0))

import webbrowser

def display():
	# infinite loop
	while True:
		print(countdown.delta_time() + " | " + countdown.BTD_OP.strftime(countdown.format))
		if countdown.delta_time() == countdown.BTD_OP.strftime(countdown.format):
			webbrowser.open("https://www.youtube.com/watch?v=E3SLE19QLEs")

		text = font.render(countdown.remain_time(), True, BLACK, WHITE)

		textRect = text.get_rect()
		textRect.center = (X // 2, Y // 2)

		display_surface.blit(text, textRect)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:

				pygame.quit()

				quit()

		time.sleep(0.01)
		pygame.display.update()
