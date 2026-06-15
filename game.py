# import random
# import pygame
#
# pygame.init()
#
# WIDTH=800
# HEIGHT=600
#
# screen=pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("My first game")
#
# WHITE=(255,255,255)
# RED=(255,0,0)
# GREEN=(0,255,0)
# BLUE=(0,0,255)
# BLACK=(0,0,0)
# SKY=(135,206,250)
# GOLD=(255,215,0)
#
#
#
# player_x=150
# player_y=200
# player_size=70
# player_speed=5
# player_hp=100
# player_score=0
#
# obstacle_x=random.randint(0,WIDTH-64)
# obstacle_y=random.randint(0,HEIGHT-64)
# obstacle_size=20
#
#
#
#
# running=True
# while running:
#     pygame.time.delay(30)
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             running=False
#
#     keys=pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         player_x-=player_speed
#     if keys[pygame.K_RIGHT]:
#         player_x+=player_speed
#     if keys[pygame.K_UP]:
#         player_y-=player_speed
#     if keys[pygame.K_DOWN]:
#         player_y+=player_speed
#
#     if player_x < 0:
#         player_x = 0
#         player_hp -= 1
#
#     if player_x > WIDTH - player_size:
#         player_x = WIDTH - player_size
#         player_hp -= 1
#
#     if player_y < 0:
#         player_y = 0
#         player_hp -= 1
#
#     if player_y > HEIGHT - player_size:
#         player_y = HEIGHT - player_size
#         player_hp -= 1
#
#
#     screen.fill(SKY)
#     pygame.draw.rect(screen,RED,(player_x,player_y,player_size,player_size))
#     pygame.draw.circle(screen,GOLD,(coin_x,coin_y),coin_size)
#     pygame.draw.rect(screen,BLACK (obstacle_x,obstacle_y,obstacle_size,obstacle_size)
#
#     player_rect=pygame.Rect(player_x,player_y,player_size,player_size)
#     coin_rect=pygame.Rect(coin_x,coin_y,coin_size,coin_size)
#     obstacle_rect=pygame.Rect(obstacle_x,obstacle_y,obstacle_size,obstacle_size)
#     if player_rect.colliderect(coin_rect):
#         player_score+=1
#         coin_x=random.randint(0,WIDTH-64)
#         coin_y=random.randint(0,HEIGHT-64)
#
#     if obstacle_rect.colliderect(player_rect):
#         player_hp-=1
#         obstacle_x=random.randint(0,WIDTH-64)
#         obstacle_y=random.randint(0,HEIGHT-64)
#
#
#
#     hp_text=pygame.font.SysFont("Arial",30).render("HP: "+str(player_hp),True,BLACK)
#     score_text=pygame.font.SysFont("Arial",30).render("Score: "+str(player_score),True,BLACK)
#     screen.blit(hp_text,(10,10))
#     screen.blit(score_text,(10,50))
#     pygame.display.update()
#
# pygame.quit()
#
#

import random

import pygame

# pygame.init()
#
# WIDTH=800
# HEIGHT=600
#
# screen=pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Моя первая игра")
#
# WHITE=(255,255,255)
# RED=(255,0,0)
# GREEN=(0,255,0)
# BLUE=(0,0,255)
# BLACK=(0,0,0)
# SKY=(135,206,250)
# GOLD=(255,215,0)
#
# player_x=150
# player_y=200
# player_size=70
# player_speed=30
# player_hp=100
# player_score=0
#
# coin_x=random.randint(0,WIDTH-64)
# coin_y=random.randint(0,HEIGHT-64)
# coin_size=30
#
# obstacle_x = random.randint(0, WIDTH - 64)
#
# obstacle_y = random.randint(0, HEIGHT - 64)
# obstacle_size = 30
#
# running=True
# while running:
#     pygame.time.delay(30)
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             running=False
#
#     keys=pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         player_x-=player_speed
#     if keys[pygame.K_RIGHT]:
#         player_x+=player_speed
#     if keys[pygame.K_UP]:
#         player_y-=player_speed
#     if keys[pygame.K_DOWN]:
#         player_y+=player_speed
#
#     screen.fill(SKY)
#
#     pygame.draw.rect(screen,RED,(player_x,player_y,player_size,player_size))
#     pygame.draw.circle(screen,GOLD,(coin_x,coin_y),coin_size)
#
#     pygame.draw.rect(screen, BLACK,(obstacle_x, obstacle_y, obstacle_size, obstacle_size))
#     obstacle_rect=pygame.Rect(obstacle_x,obstacle_y,obstacle_size,obstacle_size)
#     player_rect=pygame.Rect(player_x,player_y,player_size,player_size)
#     coin_rect=pygame.Rect(coin_x,coin_y,coin_size,coin_size)
#
#     if player_rect.colliderect(coin_rect):
#         player_score+=1
#         coin_x=random.randint(0,WIDTH-64)
#         coin_y=random.randint(0,HEIGHT-64)
#
#     if obstacle_rect.colliderect(player_rect):
#         player_hp -= 1
#         obstacle_x = random.randint(0, WIDTH - 64)
#         obstacle_y = random.randint(0, HEIGHT - 64)
#
#
#
#     hp_text=pygame.font.SysFont("Arial",30).render("HP: "+str(player_hp),True,BLACK)
#     score_text=pygame.font.SysFont("Arial",30).render("Score: "+str(player_score),True,BLACK)
#     screen.blit(hp_text,(10,10))
#     screen.blit(score_text,(10,50))
#     pygame.display.update()
#
# pygame.quit()


# import pygame
#
# pygame.init()
#
# WIDTH = 1000
# HEIGHT = 600
#
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Мини-Футбол")
#
# WHITE = (255, 255, 255)
# GREEN = (0, 150, 0)
# BLUE = (0, 0, 255)
# RED = (255, 0, 0)
# BLACK = (0, 0, 0)
#
# player = pygame.Rect(100, 250, 40, 40)
# ball = pygame.Rect(300, 280, 25, 25)
#
# goal = pygame.Rect(950, 200, 50, 200)
#
# player_speed = 5
# ball_speed_x = 0
# ball_speed_y = 0
#
# score = 0
#
# font = pygame.font.SysFont(None, 50)
#
# clock = pygame.time.Clock()
#
# running = True
# while running:
#     clock.tick(60)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_LEFT]:
#         player.x -= player_speed
#     if keys[pygame.K_RIGHT]:
#         player.x += player_speed
#     if keys[pygame.K_UP]:
#         player.y -= player_speed
#     if keys[pygame.K_DOWN]:
#         player.y += player_speed
#
#     if player.colliderect(ball):
#         ball_speed_x = 8
#         if player.centery < ball.centery:
#             ball_speed_y = 3
#         else:
#             ball_speed_y = -3
#
#     ball.x += ball_speed_x
#     ball.y += ball_speed_y
#
#     ball_speed_x *= 0.98
#     ball_speed_y *= 0.98
#
#     if ball.left <= 0 or ball.right >= WIDTH:
#         ball_speed_x *= -1
#
#     if ball.top <= 0 or ball.bottom >= HEIGHT:
#         ball_speed_y *= -1
#
#     if ball.colliderect(goal):
#         score += 1
#         ball.x = 300
#         ball.y = 280
#         ball_speed_x = 0
#         ball_speed_y = 0
#
#     screen.fill(GREEN)
#
#     pygame.draw.rect(screen, WHITE, goal)
#     pygame.draw.rect(screen, BLUE, player)
#     pygame.draw.circle(screen, BLACK, ball.center, 12)
#
#     score_text = font.render(f"Голы: {score}", True, WHITE)
#     screen.blit(score_text, (20, 20))
#
#     pygame.display.update()
#
# pygame.quit()

import pygame
import random

pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Футбол 1 на 1")

WHITE = (255, 255, 255)
GREEN = (0, 140, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

player = pygame.Rect(150, 280, 40, 40)
enemy = pygame.Rect(810, 280, 40, 40)
ball = pygame.Rect(490, 290, 20, 20)

left_goal = pygame.Rect(0, 200, 20, 200)
right_goal = pygame.Rect(980, 200, 20, 200)

ball_dx = 0
ball_dy = 0

player_score = 0
enemy_score = 0

font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # Границы игрока
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH
    if player.top < 0:
        player.top = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT

    # ИИ соперника
    if enemy.centerx > ball.centerx:
        enemy.x -= 3
    if enemy.centerx < ball.centerx:
        enemy.x += 3

    if enemy.centery > ball.centery:
        enemy.y -= 3
    if enemy.centery < ball.centery:
        enemy.y += 3

    # Границы соперника
    if enemy.left < 0:
        enemy.left = 0
    if enemy.right > WIDTH:
        enemy.right = WIDTH
    if enemy.top < 0:
        enemy.top = 0
    if enemy.bottom > HEIGHT:
        enemy.bottom = HEIGHT

    # Удар игрока
    if player.colliderect(ball):
        ball_dx = 8
        ball_dy = random.randint(-4, 4)

    # Удар соперника
    if enemy.colliderect(ball):
        ball_dx = -8
        ball_dy = random.randint(-4, 4)

    # Движение мяча
    ball.x += ball_dx
    ball.y += ball_dy

    ball_dx *= 0.98
    ball_dy *= 0.98

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1


    if ball.colliderect(right_goal):
        player_score += 1

        player.x = 150
        player.y = 280

        enemy.x = 810
        enemy.y = 280

        ball.x = 490
        ball.y = 290

        ball_dx = 0
        ball_dy = 0

    # Гол соперника
    if ball.colliderect(left_goal):
        enemy_score += 1

        player.x = 150
        player.y = 280

        enemy.x = 810
        enemy.y = 280

        ball.x = 490
        ball.y = 290

        ball_dx = 0
        ball_dy = 0

    # Отрисовка
    screen.fill(GREEN)

    # Граница поля
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT), 5)

    # Ворота
    pygame.draw.rect(screen, WHITE, left_goal)
    pygame.draw.rect(screen, WHITE, right_goal)

    # Центральная линия
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 3)

    # Игроки
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    # Мяч
    pygame.draw.circle(screen, BLACK, ball.center, 10)
    if enemy.left < 0:
        enemy.left = 0
    if enemy.right > WIDTH:
        enemy.right = WIDTH
    if enemy.top < 0:
        enemy.top = 0
    if enemy.bottom > HEIGHT:
        enemy.bottom = HEIGHT


    # Счёт
    text = font.render(f"{player_score} : {enemy_score}", True, WHITE)
    screen.blit(text, (450, 20))

    pygame.display.flip()

pygame.quit()