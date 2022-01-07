from random import sample
from KreatywnyKoder.bubble_sorting import measure

array = sample(range(1, 10000), 3000)


@measure
def simple_sort(w_array):
    print(w_array[:10])

    for i in range(1, len(w_array)):

        j = w_array[i]
        k = i - 1

        while k >= 0 and j < w_array[k]:
            w_array[k + 1] = w_array[k]
            k -= 1

        w_array[k + 1] = j

    print(w_array[:10])


if __name__ == '__main__':
    simple_sort(array.copy())
