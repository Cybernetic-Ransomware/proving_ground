import pygame
from random import sample
from KreatywnyKoder.bubble_sorting import second_improved_sort


pygame.init()


class DrawInformation:

    CLRS = {
        'RED': (255, 0, 0),
        'GREEN': (0, 255, 0),
        'BLUE': (0, 0, 255),
        'YELLOW': (255, 255, 0),
        'WHITE': (255, 255, 255),
        'BLACK': (0, 0, 0),
        'PURPLE': (128, 0, 128),
        'ORANGE': (255, 165, 0),
        'GREY': (128, 128, 128),
        'TURQUOISE': (64, 224, 208)
    }
    BACKGROUND_COLOR = CLRS['WHITE']
    SIDE_PAD = 100
    TOP_PAD = 150

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
        self.bar_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def generate_array(min_val, max_val, n):
    return sample(range(min_val, max_val), n)


if __name__ == '__main__':
    array = generate_array(100, 2000, 300)

    second_improved_sort(array.copy())

    run = True
    clock = pygame.time.Clock()

    draw_info = DrawInformation(1024, 768, array.copy())

    while run:
        clock.tick(75)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
