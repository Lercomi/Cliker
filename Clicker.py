from unittest import skipIf

import pygame
import sys


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clicker")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

font = pygame.font.Font(None, 120)
font2 = pygame.font.Font(None, 50)
font3 = pygame.font.Font(None, 50)

score = 0
step = 1

button_text = font.render("Click", True, RED)
button_text2 = font2.render("БАФ X2", True, RED)
button_text3 = font3.render("БАФ X4", True, RED)
button_width = 200
button_width2 = 150
button_width3 = 150
button_height = 100
button_height2 = 75
button_height3 = 75
button_color = BLACK
button_color2 = YELLOW
button_color3 = YELLOW
button_rect = pygame.Rect((screen_width // 2 - button_width // 2, screen_height // 2 - button_height // 2, button_width, button_height))
button_rect2 = pygame.Rect((screen_width // 800 + button_width2 // 15, screen_height // 15 + button_height2 // 5, button_width2, button_height2))
button_rect3 = pygame.Rect((screen_width // 3 + button_width3 // 17, screen_height // 17 + button_height3 // 5, button_width3, button_height3))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                score += step
            if button_rect2.collidepoint(event.pos) and score >=100:
                score -= 100
                step = step * 2
            elif score < 100:
                continue
            if button_rect3.collidepoint(event.pos):
                score -= 150
                step = step * 4


    screen.fill(WHITE)

    pygame.draw.rect(screen, button_color, button_rect)
    pygame.draw.rect(screen, button_color2, button_rect2)
    pygame.draw.rect(screen, button_color3, button_rect3)
    screen.blit(button_text, (screen_width // 2 - button_width // 2, screen_height // 2 - button_height // 2))
    screen.blit(button_text2, (screen_width // 800 + button_width2 // 10, screen_height // 10 + button_height2 // 5))
    screen.blit(button_text3, (screen_width // 3 + button_width3 // 11, screen_height // 11 + button_height3 // 5))

    score_text = font.render(str(score), True, BLACK)
    screen.blit(score_text, (screen_width // 2, screen_height // 4))



    pygame.display.flip()

pygame.quit()
sys.exit()