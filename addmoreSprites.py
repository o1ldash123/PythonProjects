import pygame
import random
import time
# pre game setup
lose = True
control = True
def controls(key , player) :
   if key[pygame.K_UP]:
        player.rect.y -= 1
        if player.rect.y < 0:
            player.rect.y = 0
   if key[pygame.K_DOWN] :
            player.rect.y += 0.5
            if player.rect.y > 700:
                player.rect.y = 700
   if key[pygame.K_LEFT] :
            player.rect.x -= 1
            if player.rect.x < 0:
                player.rect.x = 0
   if key[pygame.K_RIGHT] :
            player.rect.x += 1
            if player.rect.x > 900:
                player.rect.x = 900

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

class sprite (pygame.sprite.Sprite) :
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
screen = pygame.display.set_mode((1000, 800))
player = sprite(50, 50, 100, 100,"player.png" )  # Red rectangle
enemies = []
for _ in range(7) :
    x = random.randint(0, 900)
    y = random.randint(0, 700)
    enemy = sprite(x, y, 100, 100,'enemy.png')
    enemies.append(enemy)
group = pygame.sprite.Group()
group.add(player)
for enemy in enemies :
    group.add(enemy)
running = True
score = 0
#live game section
while running :
    screen.fill((255, 255, 255))  # Fill the screen with white
    group.draw(screen)
    key = pygame.key.get_pressed()
    if lose != False and control == True :
      controls(key , player)
     #event section
    for event in pygame.event.get():
        for enemy in enemies :
          if pygame.sprite.collide_rect(player, enemy) :
            enemies.remove(enemy)
            group.remove(enemy)
            score += 5
          if score == 100 or (score + 5)  > 100 :
              lose = False

          if len(enemies) == 0 :
           
            for _ in range(7) :
                x = random.randint(0, 900)
                y = random.randint(0, 700)
                enemy = sprite(x, y, 100, 100, "enemy.png")
                enemies.append(enemy)
                group.add(enemy)

        if event.type == pygame.QUIT :
            running = False
    #screen render section
    
    scoreFont = font.render(f'Score: {score}', True, (0, 0, 0))
    if  lose != False :
      times = max(0, 30 - pygame.time.get_ticks() // 1000)
      timer = font.render(f'Time: {times}', True, (0, 0, 0) , )
      screen.blit(timer , (500, 10))
      screen.blit(scoreFont, (10, 10))
    if times == 0 and lose == True :
        control = False
        del scoreFont
        del timer
        fontEnd = font.render('Time is up! Game Over!', True, (255, 0, 0))
        screen.blit(fontEnd, (300, 400))
    if lose == False :
        del scoreFont
        fontWin = font.render('You Win! Congratulations!', True, (0, 255, 0))
        screen.blit(fontWin, (300, 400))
        

        
       

    pygame.display.update()

