import pygame
import math
import sys

pygame.init()

WIDTH = 700
HEIGHT = 400
X_CENTRE = WIDTH / 2
Y_CENTRE = HEIGHT / 2
LINEWIDTH = 7
LINEWIDTH_COMP = LINEWIDTH / 2
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

# Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,191,255)

def draw_border():
    pygame.draw.rect(
        SURFACE,
        WHITE,
        (0, 0, WIDTH, HEIGHT),
        math.floor(LINEWIDTH + LINEWIDTH_COMP)
    )
    
def draw_centre_line(number_of_dashes):
    compensation = LINEWIDTH * 2
    total_available_height = HEIGHT - compensation
    dash_count = number_of_dashes
    dash_height = total_available_height / dash_count
    dash_Y_pos = LINEWIDTH + (dash_height / 2)
    iterator = 1

    for dash in range(dash_count - 1):
        if iterator % 2 == 0:
            dash_colour = BLACK
        else:
            dash_colour = WHITE

        pygame.draw.rect(SURFACE, dash_colour, (X_CENTRE, dash_Y_pos, LINEWIDTH, dash_height))

        dash_Y_pos += dash_height
        iterator += 1

def make_paddle(x_pos):
    paddle_height = math.floor(HEIGHT / 8)
    paddle = pygame.rect.Rect(x_pos, (Y_CENTRE - (paddle_height / 2)), LINEWIDTH,paddle_height)
    return paddle

de baf make_ball():
   ll = pygame.rect.Rect(X_CENTRE, Y_CENTRE, LINEWIDTH, LINEWIDTH)

    return ball

def draw_rectangle(element_object, colour=WHITE):
    pygame.draw.rect(SURFACE, colour, element_object)

def setup():
    draw_border()
    draw_centre_line(20)

    ball = draw_ball()
    paddle_player = make_paddle(LINEWIDTH * 2)
    paddle_cpu = make_paddle(WIDTH - (LINEWIDTH * 3))

    GameObjects = {'player': paddle_player, 'cpu': paddle_cpu, 'ball': ball}

    draw_rectangle(paddle_player)
    draw_rectangle(paddle_cpu)

    return GameObjects

GameObjects = setup()

def redraw():
    draw_border()
    draw_centre_line(20)
    draw_rectangle(GameObjects['player'])
    draw_rectangle(GameObjects['cpu'])


while True:
    CLOCK.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        GameObjects['player'].y -= 2 
        print(GameObjects['player'].y)
        
    if keys[pygame.K_s]:
        GameObjects['player'].y += 2
        print(GameObjects['player'].y)


    SURFACE.fill(BLACK)
    redraw()
    pygame.display.update()