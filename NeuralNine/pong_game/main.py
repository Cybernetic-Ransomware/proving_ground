import pygame


# const and var
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 600

pygame.init()
game_font = pygame.font.SysFont('Ubuntu', 40)

delay = 30

paddle_speed = 20
paddle_width = 10
paddle_height = 100

p1_x_position = 10
p1_y_position = HEIGHT / 2 - paddle_height / 2

p2_x_position = WIDTH - paddle_width - 10
p2_y_position = HEIGHT / 2 - paddle_height / 2


p1_score = 0
p2_score = 0

p1_up = False
p1_down = False
p2_up = False
p2_down = False

ball_x_position = WIDTH / 2
ball_y_position = HEIGHT / 2

ball_x_vel = -12
ball_y_vel = 0

ball_width = 8

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# drawing objects


def draw_objects():
    pygame.draw.rect(screen, WHITE, (int(p1_x_position), int(p1_y_position), paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (int(p2_x_position), int(p2_y_position), paddle_width, paddle_height))
    pygame.draw.circle(screen, WHITE, (int(ball_x_position), int(ball_y_position)), ball_width)
    score = game_font.render(f'{str(p1_score)} : {str(p2_score)}', False, WHITE)
    screen.blit(score, (WIDTH / 2, 30))


def apply_player_movement():
    global p1_y_position, p2_y_position

    if p1_up:
        p1_y_position = max(p1_y_position - paddle_speed, 10)
    elif p1_down:
        p1_y_position = min(p1_y_position + paddle_speed, HEIGHT)

    if p2_up:
        p2_y_position = max(p2_y_position - paddle_speed, 10)
    elif p2_down:
        p2_y_position = min(p2_y_position + paddle_speed, HEIGHT)


def apply_ball_movement():
    global ball_x_position, ball_y_position
    global ball_x_vel, ball_y_vel
    global p1_score, p2_score

    if (ball_x_position + ball_x_vel < p1_x_position + paddle_width) and \
            (p1_y_position < ball_y_position + ball_y_vel + ball_width < p1_y_position + paddle_height):
        ball_x_vel = -ball_x_vel + 1
        ball_y_vel = (p1_y_position + paddle_height / 2 - ball_y_position) / 15
        ball_y_vel = -(ball_y_vel + 1)
    elif ball_x_position + ball_x_vel < 0:
        p2_score += 1
        ball_x_position = WIDTH / 2
        ball_y_position = HEIGHT / 2
        ball_x_vel = 12
        ball_y_vel = 0

    if (ball_x_position + ball_x_vel > p2_x_position - paddle_width) and \
            (p2_y_position < ball_y_position + ball_y_vel + ball_width < p2_y_position + paddle_height):
        ball_x_vel = -ball_x_vel - 1
        ball_y_vel = (p2_y_position + paddle_height / 2 - ball_y_position) / 15
        ball_y_vel = -(ball_y_vel + 1)
    elif ball_x_position + ball_x_vel > WIDTH:
        p1_score += 1
        ball_x_position = WIDTH / 2
        ball_y_position = HEIGHT / 2
        ball_x_vel = -12
        ball_y_vel = 0

    if ball_y_position + ball_y_vel > HEIGHT or ball_y_position + ball_y_vel < 0:
        ball_y_vel = -ball_y_vel

    ball_x_position += ball_x_vel
    ball_y_position += ball_y_vel


pygame.display.set_caption('Bonk dizz nut')
screen.fill(BLACK)
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                p1_up = True
            if event.key == pygame.K_s:
                p1_down = True
            if event.key == pygame.K_UP:
                p2_up = True
            if event.key == pygame.K_DOWN:
                p2_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1_up = False
            if event.key == pygame.K_s:
                p1_down = False
            if event.key == pygame.K_UP:
                p2_up = False
            if event.key == pygame.K_DOWN:
                p2_down = False

    screen.fill(BLACK)
    apply_player_movement()
    apply_ball_movement()
    draw_objects()
    pygame.display.flip()
    pygame.time.wait(delay)
