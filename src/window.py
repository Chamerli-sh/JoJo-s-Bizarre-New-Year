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


# infinite loop
while True:
	countdown.delta_time()
	text = font.render(countdown.remain_time(), True, BLACK, WHITE)


	textRect = text.get_rect()

	textRect.center = (X // 2, Y // 2)

	display_surface.fill(WHITE)

	display_surface.blit(text, textRect)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:

			pygame.quit()

			quit()

	time.sleep(0.01)
	pygame.display.update()
