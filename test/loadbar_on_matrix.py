import numpy as np
import time


filled = '■'
not_filled = '□'
load_step = 8


progress = 0
visualisation = np.full((4, 25), not_filled)


def show_progress_bar(progress):
    for i in range(progress):
        col = i // 4
        row = i % 4
        visualisation[row, col] = filled

    print(f'Progress: {progress}%')
    print('\n'.join(' '.join(x for x in y) for y in visualisation), end='\n\n')


if __name__ == '__main__':
    for i in range(0, 101 + load_step, load_step):
        progress = i if i < 100 else 100
        show_progress_bar(progress)
        time.sleep(0.25)
    print('Success!')
