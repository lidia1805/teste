import pygame

pygame.init()

write = (255, 255, 255)
grey = (212, 210, 212)
black = (0, 0, 0)
blue = (0, 97, 148)
red = (162, 8, 0)
orange = (183, 119, 0)
green = (0, 127, 33)
yellow = (197, 199, 37)

width = 800
height = 600
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BREAKOUT")
clock = pygame.time.Clock()

paddle_width = 54
paddle_height = 20
paddle_x = 250


all_sprites_list = pygame.sprite.Group()


class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


all_bricks = pygame.sprite.Group()

brick_width = 55
brick_height = 10
x_gap = 4.5
y_gap = 4
wall_width = 16


def bricks():
    for j in range(8):
        for i in range(14):
            if j < 2:
                if i == 0:
                    brick = Brick(red, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(red, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 1 < j < 4:
                if i == 0:
                    brick = Brick(orange, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(orange, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 3 < j < 6:
                if i == 0:
                    brick = Brick(green, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(green, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 5 < j < 8:
                if i == 0:
                    brick = Brick(yellow, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(yellow, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)


brick_wall = bricks()


class Ball:
    def __init__(self):
        self.x = width / 2.0
        self.y = height / 2.0
        self.dx = 6
        self.dy = -6
        self.width = 15
        self.height = 15

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        # Check for border collision
        if self.x < 0 + self.width / 2.0:
            self.x = 0 + self.width / 2.0
            self.dx *= -1

        elif self.x > width - self.width / 2.0:
            self.x = width - self.width / 2.0
            self.dx *= -1

        if self.y < 0 + self.height / 2.0:
            self.y = 0 + self.height / 2.0
            self.dy *= -1

        elif self.y > height - self.height / 2.0:
            self.y = height - self.height / 2.0
            self.x = width / 2.0
            self.y = height / 2.0

    def render(self):
        pygame.draw.rect(screen, grey, pygame.Rect(int(self.x - self.width / 2.0),
                                                   int(self.y - self.height / 2.0), self.width, self.height))


class Paddle:
    def __init__(self):
        self.x = width / 2.0
        self.y = 550
        self.dx = 0
        self.width = 54
        self.height = 20
        self.score = 0

    def left(self):
        self.dx = -12

    def right(self):
        self.dx = 12

    def move(self):
        self.x = self.x + self.dx

        # Check for border collision
        if self.x < 0 + self.width / 2.0:
            self.x = 0 + self.width / 2.0
            self.dx = 0

        elif self.x > width - self.width / 2.0:
            self.x = width - self.width / 2.0
            self.dx = 0

    def render(self):
        pygame.draw.rect(screen, blue,
                         pygame.Rect(int(self.x - self.width / 2.0), int(self.y - self.height / 2.0), self.width,
                                     self.height))


ball = Ball()

paddle = Paddle()


def main():
    clock.tick(60)

    carry = True
    while carry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry = False
        all_sprites_list.update()

        screen.fill(black)

        pygame.draw.line(screen, grey, [0, 10], [width, 10], 30)
        pygame.draw.line(screen, grey, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, height], wall_width)
        pygame.draw.line(screen, grey, [(width - wall_width / 2) - 1, 0], [(width - wall_width / 2) - 1, height],
                         wall_width)

        pygame.draw.line(screen, blue, [(wall_width / 2) - 1, height - 65 + paddle_height / 2 - 54 / 2],
                         [(wall_width / 2) - 1, height - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
        pygame.draw.line(screen, blue, [(width - wall_width / 2) - 1, height - 65 + paddle_height / 2 - 54 / 2],
                         [(width - wall_width / 2) - 1, height - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)

        pygame.draw.line(screen, red, [(wall_width / 2) - 1, 100],
                         [(wall_width / 2) - 1, 100 + 2 * brick_height + 2 * y_gap], wall_width)
        pygame.draw.line(screen, red, [(width - wall_width / 2) - 1, 100],
                         [(width - wall_width / 2) - 1, 100 + 2 * brick_height + 2 * y_gap], wall_width)

        pygame.draw.line(screen, orange, [(wall_width / 2) - 1, 100 + 2 * brick_height + 2 * y_gap],
                         [(wall_width / 2) - 1, 100 + 4 * brick_height + 4 * y_gap], wall_width)
        pygame.draw.line(screen, orange, [(width - wall_width / 2) - 1, 100 + 2 * brick_height + 2 * y_gap],
                         [(width - wall_width / 2) - 1, 100 + 4 * brick_height + 4 * y_gap], wall_width)

        pygame.draw.line(screen, green, [(wall_width / 2) - 1, 100 + 4 * brick_height + 4 * y_gap],
                         [(wall_width / 2) - 1, 100 + 6 * brick_height + 6 * y_gap], wall_width)
        pygame.draw.line(screen, green, [(width - wall_width / 2) - 1, 100 + 4 * brick_height + 4 * y_gap],
                         [(width - wall_width / 2) - 1, 100 + 6 * brick_height + 6 * y_gap], wall_width)

        pygame.draw.line(screen, yellow, [(wall_width / 2) - 1, 100 + 6 * brick_height + 6 * y_gap],
                         [(wall_width / 2) - 1, 100 + 8 * brick_height + 8 * y_gap], wall_width)
        pygame.draw.line(screen, yellow, [(width - wall_width / 2) - 1, 100 + 6 * brick_height + 6 * y_gap],
                         [(width - wall_width / 2) - 1, 100 + 8 * brick_height + 8 * y_gap], wall_width)

        paddle.move()
        paddle.render()
        ball.render()

        all_sprites_list.draw(screen)

        pygame.display.update()

    pygame.quit()


main()
