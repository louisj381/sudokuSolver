import sys, pygame
from pygame.locals import *
import engine as eng
from constants import *


def drawLines(surface):
    vertical_points = [(HORIZONAL_OFFSET,0), (HORIZONAL_OFFSET, BOARD_HEIGHT)]
    horizontal_points = [(HORIZONAL_OFFSET, 0), (BOARD_WIDTH+HORIZONAL_OFFSET, 0)]
    i = 0
    while i < 9:
        first_Vertical_tuple = (vertical_points[-2][0] + 50, vertical_points[-2][1])
        second_Vertical_tuple = (vertical_points[-1][0] + 50, vertical_points[-1][1])
        first_Horizontal_tuple = (horizontal_points[-2][0], horizontal_points[-2][1] + 50)
        second_Horizontal_tuple = (horizontal_points[-1][0], horizontal_points[-1][1] + 50)
        vertical_points.append(first_Vertical_tuple)
        vertical_points.append(second_Vertical_tuple)
        horizontal_points.append(first_Horizontal_tuple)
        horizontal_points.append(second_Horizontal_tuple)
        i += 1
    j = 0
    while j < len(vertical_points) and j < len(horizontal_points):
        if j % 3 == 0:
            lineWidth = 2
        else:
            lineWidth = 1
        pygame.draw.line(surface, (0,0,0), vertical_points[j], vertical_points[j+1], lineWidth)
        pygame.draw.line(surface, (0,0,0), horizontal_points[j], horizontal_points[j+1], lineWidth)
        j += 2


def main():
    pygame.init()

    game_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    boardBackground = pygame.Surface((450,450))
    boardBackground.fill(WHITE)

#TODO: change this into function to convert board
    global font
    font = pygame.font.Font(None,56)
    number = font.render("1", 1, (0,0,0))

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        game_screen.fill(GREY)
        game_screen.blit(boardBackground, (HORIZONAL_OFFSET, 0))
        drawLines(game_screen)
        game_screen.blit(number,(50,50))
        pygame.display.flip()


if __name__ == "__main__":
    main()
