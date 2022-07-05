import time
import psutil


def display_usage(cpu_usage, memory_usage, bars=20):
    cpu_perc = (cpu_usage / 100.0)
    memory_perc = (memory_usage / 100.0)

    cpu_bar = '█' * int(cpu_perc * bars) + '-' * (bars - int(cpu_perc * bars))
    memory_bar = '█' * int(memory_perc * bars) + '-' * (bars - int(memory_perc * bars))

    print(f'\rCPU usage: |{cpu_bar}| {cpu_usage:.2f}% ', end='')
    print(f'Memory usage: |{memory_bar}| {memory_usage:.2f}% ', end='')


while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 25)
    time.sleep(2)
