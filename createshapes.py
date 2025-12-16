import pygame
import random
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Shape Creator")
print("This program creates shapes on the screen.")
   
def draw():
    font = pygame.font.SysFont(None, 40)
    text_surface = font.render("My shapes", True, (255, 255, 255))
    screen.blit(text_surface, (100, 100))
    pygame.draw.circle(screen , pygame.Color('blue'), (250, 250), 50)
    pygame.draw.polygon(screen , pygame.Color('green'), [(300, 300), (350, 250), (400, 300) , (375, 350)])
    pygame.draw.ellipse(screen , pygame.Color('yellow'), (150, 350, 100, 50))
    pygame.draw.line(screen , pygame.Color('white'), (0, 0), (500, 500), 5)
    pygame.draw.line(screen , pygame.Color('white'), (500, 0), (0, 500), 5)
    pygame.draw.arc(screen , pygame.Color('purple'), (200, 200, 100, 100), 0, 3.14, 3)
    pygame.draw.polygon(screen , pygame.Color('orange'), [(50, 400), (75, 350), (100, 400) , (75, 450)])
    pygame.display.update()
done = False
while done == False:
 draw()
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        done = True
        print("Exited the shape creator.")