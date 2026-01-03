import pygame
import random
import time
pygame.init()
class sprite(pygame.sprite.Sprite):
    def __init__(self,x , y, width, height , color ):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        
print('Welcome to the custom event demo ! ')
time.sleep(3)
print('In this demo , when the two squares touch , they will flicker till they change colour ! ')
time.sleep(3)
print('Use the arrow keys to move the green square around and touch the red square to see the effect ! ')
time.sleep(5)
print('Enjoy ! ')
screen = pygame.display.set_mode((1000, 800))
group = pygame.sprite.Group()
sprite1 = sprite( random.randint(0 , 1000), random.randint(0 , 800), 100, 100 , (pygame.Color('green')))
sprite2 = sprite( random.randint(0 , 1000), random.randint(0 , 800), 100, 100 , pygame.Color('red'))
touchable = True
live = True 
num = 0
while live == True:
    group.draw(screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
        sprite1.rect.x -= 1
    if keys[pygame.K_RIGHT] :   
        sprite1.rect.x += 1
    if keys[pygame.K_UP] :
        sprite1.rect.y -= 1
    if keys[pygame.K_DOWN] :   
        sprite1.rect.y += 1
    screen.fill((255, 255, 255)) # Fill the screen with white
    screen.blit(sprite1.image, sprite1.rect)
    screen.blit(sprite2.image, sprite2.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            live = False
    if pygame.sprite.collide_rect(sprite1, sprite2) :
        for i in (sprite1 , sprite2 , screen) :
            touchable = True
            if touchable == True :
             if i != screen :
                i.image.fill((random.randint(0 , 255) , random.randint(0 , 255) , random.randint(0 , 255)))
             
             touchable = False
            if touchable == False :
                if  pygame.sprite.collide_rect(sprite1, sprite2) == False :
                    touchable = True
            
                
        
    
                       
                       
                       
                         
                        

        
        
   # if pygame.sprite.collide_rect(sprite1, sprite2):
    #    print("Collision detected!")
    pygame.display.update()
        

        