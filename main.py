import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
size = (650, 720)
height = 20
width = 160
x = 250
y = 650
vel = 0.5

screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2021.01.30")
screen.fill(COLOR_BLACK)
font = pygame.font.Font('PressStart2P.ttf', 44)

# paddle

#paddle = pygame.draw.rect(screen, COLOR_WHITE, [x, y, width, height])


# ball
ball = pygame.draw.ellipse(screen, COLOR_WHITE, [300, 500, 20, 20])
ball_x = 300
ball_y = 350
ball_dx = 5
ball_dy = 5

# ball movement


pygame.display.flip()
game_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    ball = pygame.draw.ellipse(screen, COLOR_WHITE, [300, 500, 20, 20])

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 650 - width:
        x += vel
    screen.fill((0, 0, 0))

    paddle = pygame.draw.rect(screen, COLOR_WHITE, [x, y, width, height])
    pygame.display.update()
    game_clock.tick()
    pygame.display.flip()
