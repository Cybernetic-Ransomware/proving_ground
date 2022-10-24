import matplotlib.pyplot as plt
import math


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('X position')
    plt.ylabel('Y position')
    plt.title('Trajectory of projective')


def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval

    return numbers


def draw_trajectory(u, theta_d):
    theta = math.radians(theta_d)
    g = 9.8

    t_flight = 2 * u * math.sin(theta) / g
    intervals = frange(0, t_flight, 0.001)

    x = []
    y = []

    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t**2)

    draw_graph(x, y)
    print(f'Graph: {u} [m/s], {theta_d} [°]')
    print(f'Max X distance: {x[-1]:.3f}m')
    print(f'Max Y distance: {max(y):.3f}m')
    print(f'Time of flying: {t_flight:.3f}:m')


if __name__ == '__main__':
    try:
        count = int(input('Set drawnings amount: '))
        u_list = []
        thetas_list = []

        for i in range(count):
            u_list.append(float(input('Set start velocity: ')))
            thetas_list.append(float(input('Set angle in degrees: ')))
    except ValueError:
        print('Input values error')
    else:
        for u, theta in dict(zip(u_list, thetas_list)).items():
            print('---' * 5)
            draw_trajectory(u, theta)
        plt.legend(u_list)
        plt.show()
