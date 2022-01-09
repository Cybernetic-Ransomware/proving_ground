import math
import pygame
from random import sample
import time


pygame.init()


class DrawInformation:

    CLRS = {
        'YELLOW': (238, 255, 65),
        'GREEN': (0, 255, 0),
        'BLUE': (0, 0, 255),
        'WARM_WHITE': (255, 243, 224),
        'BLACK': (0, 0, 0),
        'PURPLE': (128, 0, 128),
        'LIMON': (198, 255, 0),
    }
    
    BACKGROUND_COLOR = CLRS['WARM_WHITE']
    FADES_VARIABLES = [
        (255, 204, 188),
        (255, 171, 145),
        (255, 138, 101)
    ]
    
    FONT = pygame.font.SysFont('Rockwell', 20)
    L_FONT = pygame.font.SysFont('Rockwell', 26)
    SIDE_PAD = 100
    TOP_PAD = 250

    def __init__(self, width, height, array):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Sorting Algorithm Visualisation')

        self.set_array(array)

    def set_array(self, array):
        self.array = array
        self.min_val = min(array)
        self.max_val = max(array)

        self.bar_width = round((self.width - self.SIDE_PAD) / len(array))
        self.min_bar_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def generate_array(min_val, max_val, n):
    return sample(range(min_val, max_val), n)


def bubble_sorting(draw_info, ascending = True):
    swapped = True
    temp = 0
    count = 0
    w_array = draw_info.array

    while swapped:
        swapped = False
        for i in range(len(w_array) - 1 - temp):
            count += 1
            if (w_array[i] > w_array[i + 1] and ascending) or (w_array[i] < w_array[i + 1] and not ascending):
                w_array[i], w_array[i + 1] = w_array[i + 1], w_array[i]
                draw_data_bars(draw_info, {i: draw_info.CLRS['YELLOW'], i + 1: draw_info.CLRS['LIMON']}, True)
                swapped = True
                yield True
        temp += 1

    return w_array


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    keyboard = [
                draw_info.FONT.render('A - Ascending | D - Descending', 1, draw_info.CLRS['BLACK']),
                draw_info.FONT.render('Q - Insertion | B - Bubble', 1, draw_info.CLRS['BLACK']),
                draw_info.FONT.render('SPACE - START', 1, draw_info.CLRS['BLACK']),
                draw_info.FONT.render('ESC - QUIT', 1, draw_info.CLRS['BLACK']),
                draw_info.FONT.render('R - RESET', 1, draw_info.CLRS['BLACK']),
    ]
    for count, line in enumerate(keyboard):
        draw_info.window.blit(line, (draw_info.width - line.get_width() - 10, 10 + count * 26))

    draw_data_bars(draw_info)
    pygame.display.update()


def draw_data_bars(draw_info, color_positions={}, clear_background=False):
    array = draw_info.array

    if clear_background:
        clear_bars_pole = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD,
                           draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_bars_pole)


    for i, value in enumerate(array):
        x = draw_info.start_x + i * draw_info.bar_width
        y = draw_info.height - (value - draw_info.min_val) * draw_info.min_bar_height

        color = draw_info.FADES_VARIABLES[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.bar_width, draw_info.min_bar_height * value))

        if clear_background:
            pygame.display.update()


if __name__ == '__main__':
    array = generate_array(1, 500, 30)

    run = True
    clock = pygame.time.Clock()

    draw_info = DrawInformation(1024, 768, array.copy())
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sorting
    sorting_algorithm_name = 'Bubble sorting'
    sorting_algorithm_generator = None

    while run:
        clock.tick(75)

        if sorting:
            try:
                next(sorting_algorithm_generator)
                time.sleep(0.1)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_r:
                array = generate_array(1, 500, 30)
                draw_info.set_array(array.copy())
                sorting = False
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False

    pygame.quit()
