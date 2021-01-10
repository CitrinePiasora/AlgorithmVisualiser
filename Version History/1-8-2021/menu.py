import pygame, sys
from pygame.locals import *
 
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Main Menu')
screen = pygame.display.set_mode((800, 600),0,32)
 
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

font = pygame.font.SysFont("Comic Sans MS", 30)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
def main_menu():
    click = False
    while True:
 
        screen.fill((WHITE))
        draw_text('Main Menu', font, (BLACK), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
    
        button_1 = pygame.Rect(50, 100, 300, 50)
        button_2 = pygame.Rect(50, 200, 150, 50)
        button_3 = pygame.Rect(50, 300, 110, 50)

        pygame.draw.rect(screen, (WHITE), button_1)
        pygame.draw.rect(screen, (WHITE), button_2)
        pygame.draw.rect(screen, (WHITE), button_3)

        draw_text('Breadth First Search', font, (BLACK), screen, 50, 100)
        draw_text('A* Search', font, (BLACK), screen, 50, 200)
        draw_text('Credits', font, (BLACK), screen, 50, 300)

        if button_1.collidepoint((mx, my)):
            if click:
                bfs()
        if button_2.collidepoint((mx, my)):
            if click:
                djikstra()
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
 
def bfs():
    running = True
    while running:
        screen.fill((255, 0, 0))
        
        draw_text('BFS', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def djikstra():
    running = True
    while running:
        screen.fill((1, 255, 18))
 
        draw_text('Djikstra', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
        
def credits():
    running = True
    while running:
        screen.fill((10, 225 ,249))
 
        draw_text('Credits', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    
                
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()
