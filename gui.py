import pygame
from pygame.locals import *

pygame.init()
screenWidth = 450
screenHeight = 450
game_screen = pygame.display.set_mode((screenWidth,screenHeight))
background = pygame.Surface(game_screen.get_size())
background = background.convert()
background.fill((250, 250, 250))
vertical_points = [(50,0), (50, screenHeight)]
horizontal_points = [(0, 50), (screenWidth, 50)]
i = 0
while i < 7:
    first_Veritcal_tuple = (vertical_points[-2][0] + 50, vertical_points[-2][1])
    second_Veritcal_tuple = (vertical_points[-1][0] + 50, vertical_points[-1][1])
    first_Horizontal_tuple = (horizontal_points[-2][0], horizontal_points[-2][1] + 50)
    second_Horizontal_tuple = (horizontal_points[-1][0], horizontal_points[-1][1] + 50)
    vertical_points.append(first_Veritcal_tuple)
    vertical_points.append(second_Veritcal_tuple)
    horizontal_points.append(first_Horizontal_tuple)
    horizontal_points.append(second_Horizontal_tuple)
    i += 1
#rect = pygame.draw.lines(game_screen, (0,0,0), False, points)

#game_screen.blit(background, rect)

# Event loop
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            break

    game_screen.blit(background, (0, 0))
    j = 0
    while j < len(vertical_points) and j < len(horizontal_points):
        pygame.draw.line(game_screen, (0,0,0), vertical_points[j], vertical_points[j+1])
        pygame.draw.line(game_screen, (0,0,0), horizontal_points[j], horizontal_points[j+1])
        j += 2
    pygame.display.flip()
