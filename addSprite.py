import pygame
import math
#making two rectangler sprites
print("This program creates and displays two rectangle sprites on the screen. and you can interact with one of them using the arrow keys.")
print("Use the UP, DOWN, LEFT, and RIGHT arrow keys to move the red rectangle around the screen.")
class sprite(pygame.sprite.Sprite) :
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
pygame.init()
screen = pygame.display.set_mode((1000, 800) )
sprite1 = sprite(50, 50, 100, 100, (255, 0, 0))  # Red rectangle
sprite2 = sprite(200, 100, 100, 100, (0, 0, 255))  # Blue rectangle
pygame.display.set_caption("Sprite Example")
running = True
while running:
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        sprite1.rect.y -= 1
        if sprite1.rect.y < 0:
            sprite1.rect.y = 0
    if key[pygame.K_DOWN] :
            sprite1.rect.y += 1
            if sprite1.rect.y > 700:
                sprite1.rect.y = 700
    if key[pygame.K_LEFT] :
            sprite1.rect.x -= 1
            if sprite1.rect.x < 0:
                sprite1.rect.x = 0
    if key[pygame.K_RIGHT] :
            sprite1.rect.x += 1
            if sprite1.rect.x > 900:
                sprite1.rect.x = 900
    for event in pygame.event.get():
         
       if event.type == pygame.QUIT :
            import time
            print("Exiting the sprite program In Progress.....")
            time.sleep(3)
            running = False
            print("Exited the sprite program Successfully.")

    screen.fill((255, 255, 255))  # Fill the screen with white
    sprite1.draw(screen)
    sprite2.draw(screen)
    pygame.display.flip()
