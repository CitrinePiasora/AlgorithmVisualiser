import pygame, sys
from pygame.locals import *
import Visualizers
 
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Main Menu')
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

MMFont = pygame.font.SysFont("Comic Sans MS", 75)
OptionFont = pygame.font.SysFont("Comic Sans MS", 50)
HelpFont = pygame.font.SysFont("Comic Sans MS", 17)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
def main_menu():
    click = False
    while True:
 
        WIN.fill((WHITE))
        draw_text('Main Menu', MMFont, (BLACK), WIN, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
    
        button_1 = pygame.Rect(50, 150, 510, 75)
        button_2 = pygame.Rect(50, 250, 250, 75)
        button_3 = pygame.Rect(50, 350, 175, 75)

        pygame.draw.rect(WIN, (WHITE), button_1)
        pygame.draw.rect(WIN, (WHITE), button_2)
        pygame.draw.rect(WIN, (WHITE), button_3)

        draw_text('Breadth First Search', OptionFont, (BLACK), WIN, 50, 150)
        draw_text('A* Search', OptionFont, (BLACK), WIN, 50, 250)
        draw_text('Credits', OptionFont, (BLACK), WIN, 50, 350)
        draw_text('Controls: Left Click (Start->End->Barriers), Right Click to REMOVE TILES, C to Clear Screen',
        HelpFont, (BLACK), WIN, 30, 725)
        draw_text('Space to Start Visualizer, Backspace to Main Menu (When in Visualizer)',
        HelpFont, (BLACK), WIN, 110, 750)
        
        if button_1.collidepoint((mx, my)):
            if click:
                Visualizers.mainBFS(WIN, WIDTH)
        if button_2.collidepoint((mx, my)):
            if click:
                Visualizers.mainAStar(WIN, WIDTH)
        if button_3.collidepoint((mx, my)):
            if click:
                credits()
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
        
def credits():
    running = True
    while running:
        WIN.fill((10, 225 ,249))
 
        draw_text('Credits', HelpFont, (255, 255, 255), WIN, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    running = False
                    
                
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()