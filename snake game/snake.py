import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((700,700))
screen.fill((0, 150, 0))

snake_color = ((0,255,0))
score = 0
length = 1
facing = "Right"
applex = random.randint(10,650)
appley = random.randint(10,650)


fps = pygame.time.Clock()

snake_head = pygame.image.load('snake game\snake_head.png')
snake_left = pygame.image.load('snake game\snake_headl.png')
snake_down = pygame.image.load('snake game\snake_headd.png')
snake_right = pygame.image.load('snake game\snake_headr.png')
snake_body = pygame.image.load('snake game\snake_body.png')
apple = pygame.image.load('snake game/apple.png')



snake_head = pygame.transform.scale(snake_head,(50,50))
snake_left = pygame.transform.scale(snake_left,(50,50))
snake_right = pygame.transform.scale(snake_right,(50,50))
snake_down = pygame.transform.scale(snake_down,(50,50))
snake_body = pygame.transform.scale(snake_body,(50,50))
apple = pygame.transform.scale(apple,(20,20))

snakex, snakey = 250,250



def loose(score):
    my_font = pygame.font.SysFont('Comic Sans MS', 40)
    text_surface = my_font.render(('You lost! your score was ' + str(score)), False, (0, 0, 0))
    screen.blit(text_surface, (120,0))
    pygame.display.flip()
    time.sleep(2)
    exit()

def apple_spawn(applex,appley):
    applex = random.randint(10,650)
    appley = random.randint(10,650)
    

while True:
    fps = 60
    screen.fill((0,150,0))
    screen.blit(apple,(applex,appley))
    apple_hitbox = pygame.Rect(applex,appley,applex,appley)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    snake_hitbox = pygame.Rect(snakex,snakey,snakex,snakey)
    
    if snake_hitbox.colliderect(apple_hitbox):
        loose(score)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and snakex < 500:           
        facing = "Right"
        print(facing) 
    if keys[pygame.K_s] and snakey < 380:
        facing = "Down"
        print(facing)
    if keys[pygame.K_w] and snakey > 25:
        facing = "Up"
        print(facing)
    if keys[pygame.K_a] and snakex > 0:
        facing = "Left"
        print(facing)
    
    if facing == "Right" and snakex < 650:
        snakex +=0.1
        screen.blit(snake_right,(snakex,snakey))
    elif facing == "Left" and snakex > 0:
        snakex -=0.1
        screen.blit(snake_left,(snakex,snakey))
    elif facing == "Down" and snakey < 650:
        snakey +=0.1
        screen.blit(snake_down,(snakex,snakey))
    elif facing == "Up" and snakey > 0:
        snakey -=0.1
        screen.blit(snake_head,(snakex,snakey))

    if snakex > 650:
        loose(score)
    elif snakex < 0:
        loose(score)
    elif snakey > 650:
        loose(score)
    elif snakey < 0:
        loose(score)
    
    pygame.display.flip()