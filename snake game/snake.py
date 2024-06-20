import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((700, 700))
screen.fill((0, 150, 0))

snake_color = (0, 255, 0)
score = 0
facing = "Right"

applex = random.randint(10, 650)
appley = random.randint(10, 650)

fps = pygame.time.Clock()

snake_head = pygame.image.load('snake game/snake_head.png')
snake_left = pygame.image.load('snake game/snake_headl.png')
snake_down = pygame.image.load('snake game/snake_headd.png')
snake_right = pygame.image.load('snake game/snake_headr.png')
snake_body = pygame.image.load('snake game/snake_body.png')
apple = pygame.image.load('snake game/apple.png')

snake_head = pygame.transform.scale(snake_head, (50, 50))
snake_left = pygame.transform.scale(snake_left, (50, 50))
snake_right = pygame.transform.scale(snake_right, (50, 50))
snake_down = pygame.transform.scale(snake_down, (50, 50))
snake_body = pygame.transform.scale(snake_body, (50, 50))
apple = pygame.transform.scale(apple, (20, 20))

snakex, snakey = 250, 250
snake_pos = [snakex, snakey]
snake_segments = [list(snake_pos)]
snake_length = 1

def loose(score):

    my_font = pygame.font.SysFont('Comic Sans MS', 40)
    text_surface = my_font.render('You lost! your score was ' + str(score), False, (0, 0, 0))
    screen.blit(text_surface, (120, 0))
    pygame.display.flip()
    time.sleep(2)
    exit()

def apple_spawn():
    global applex, appley
    applex = random.randint(10, 650)
    appley = random.randint(10, 650)
    pygame.display.update()

while True:
    screen.fill((0, 150, 0))
    screen.blit(apple, (applex, appley))
    apple_hitbox = pygame.Rect(applex, appley, 20, 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:           
        facing = "Right"
    if keys[pygame.K_s]:
        facing = "Down"
    if keys[pygame.K_w]:
        facing = "Up"
    if keys[pygame.K_a]:
        facing = "Left"


    if facing == "Right":
        snakex += 5
        screen.blit(snake_right, (snakex, snakey))
    elif facing == "Left":
        snakex -= 5
        screen.blit(snake_left, (snakex, snakey))
    elif facing == "Down":
        snakey += 5
        screen.blit(snake_down, (snakex, snakey))
    elif facing == "Up":
        snakey -= 5
        screen.blit(snake_head, (snakex, snakey))

    snake_pos = [snakex, snakey]
    snake_segments.append(list(snake_pos))
    if len(snake_segments) > snake_length:
        snake_segments.pop(0)

    for segment in snake_segments:
        screen.blit(snake_body, (segment[0], segment[1]))

    snake_hitbox = pygame.Rect(snakex, snakey, 50, 50)
    if snake_hitbox.colliderect(apple_hitbox):
        score += 1
        snake_length += 10
        apple_spawn()
    
    if snakex > 650 or snakex < 0 or snakey > 650 or snakey < 0:
        loose(score)

    if facing == "Right":
        screen.blit(snake_right, (snakex, snakey))
    elif facing == "Left":
        screen.blit(snake_left, (snakex, snakey))
    elif facing == "Down":
        screen.blit(snake_down, (snakex, snakey))
    elif facing == "Up":
        screen.blit(snake_head, (snakex, snakey))

    pygame.display.flip()
    fps.tick(60)