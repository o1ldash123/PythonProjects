import pygame
import random
import time
# pre game setup
print("Can you get a 100 points in 30 seconds ?   ")
time.sleep(5)
print('\neach wave has 7 blocks and each block is worth 5 points ')
time.sleep(5)
print('\nuse the arrow keys to move the green block to hit the red blocks ')
time.sleep(5)
print('\nhit as many as you can before the timer runs out.')
time.sleep(5)
print('Goodluck ! ')
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
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
screen = pygame.display.set_mode((1000, 800))
player = sprite(50, 50, 100, 100, pygame.Color('green'))  # Red rectangle
enemies = []
for _ in range(7) :
    x = random.randint(0, 900)
    y = random.randint(0, 700)
    enemy = sprite(x, y, 100, 100, pygame.Color('red'))
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
    controls(key , player)
     #event section
    for event in pygame.event.get():
        for enemy in enemies :
          if pygame.sprite.collide_rect(player, enemy) :
            enemies.remove(enemy)
            group.remove(enemy)
            score += 5
            print("one defeated successfully! ")
            print(f"Score: {score}")
          if score == 100 or (score + 5)  > 100 :
            print("You win!")
            running = False
          if len(enemies) == 0 :
            print("regenerating enemies...")
            for _ in range(7) :
                x = random.randint(0, 900)
                y = random.randint(0, 700)
                enemy = sprite(x, y, 100, 100, pygame.Color('red'))
                enemies.append(enemy)
                group.add(enemy)

        if event.type == pygame.QUIT :
            running = False
    #screen render section
    scoreFont = font.render(f'Score: {score}', True, (0, 0, 0))

    times = max(0, 30 - pygame.time.get_ticks() // 1000)
    timer = font.render(f'Time: {times}', True, (0, 0, 0) , )
    screen.blit(timer , (500, 10))
    screen.blit(scoreFont, (10, 10))
    if times == 0:
        del scoreFont
        del timer
        clock.tick(5)
        
        print("Time's up! You lose kiddo .")
        running = False

       
   
    
    pygame.display.update()

