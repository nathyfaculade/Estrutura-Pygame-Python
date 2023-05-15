import pygame
import sys
pygame.init()

SCREEN_WIDTH =640
SCREEN_HEIGHT = 480
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_SIZE = 10
PADDLE_SPEED = 5
BALL_SPEED = 3

WHITE = (255,255,255)
BLACK = (0,0,0)

score_a = 0
score_b = 0

#Fonte
font_filr = 'C:/Users/nathi/Downloads/Press_Start_2P/PressStart2P-Regular.ttf'
font = pygame.font.Font(font_filr, 36)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

#pygame.React(x,y,widht,height)
paddle_a = pygame.Rect(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(SCREEN_WIDTH- 20 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen,WHITE,(SCREEN_WIDTH // 2, 0),(SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_a.bottom < SCREEN_HEIGHT:
        paddle_a.y += PADDLE_SPEED

    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_b.bottom < SCREEN_HEIGHT:
        paddle_b.y += PADDLE_SPEED

    ball.x += ball_dx
    ball.y -= ball_dy

    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_dx = -ball_dx
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_dy = -ball_dy

    if ball.left <= 0:
        score_b += 1
        ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        ball_dx = -ball_dx
        print(f"Ponto para B:{score_b}")

    if ball.right >= SCREEN_WIDTH:
        score_a += 1
        ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        ball_dx = -ball_dx
        print(f"Ponto para A:{score_a}")

    #Mostra o placar na tela
    score_text = font.render(f"{score_a} X {score_b}", True, WHITE)
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 30))
    screen.blit(score_text, score_rect)

    #Atualizar a tela
    pygame.display.flip()

    #Controlar FPS
    clock = pygame.time.Clock()
    clock.tick(60)