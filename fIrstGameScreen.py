import pygame
#i dint know hopw to centre
pygame.init()
screen = pygame.display.set_mode((500 , 500))
pygame.display.set_caption('first Game Screen')
done = False
image = pygame.image.load("flower.png")
image = pygame.transform.scale(image.convert_alpha(), (200, 200))
font = pygame.font.Font(None, 40)

while not done :
 
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True
    
    # --- draw after events ---
    screen.fill((58 , 58,58))
    rect = image.get_rect(center=(500//2, 500//2))
    screen.blit(image, rect)
    pygame.display.update()
    
