from random import sample
from KreatywnyKoder.bubble_sorting import measure

array = sample(range(1, 10000), 3000)


@measure
def simple_sort(w_array):
    print(w_array[:10])

    for i in range(len(w_array)):
        min_id = i

        for j in range(i + 1, len(w_array)):
            if w_array[min_id] > w_array[j]:
                min_id = j

        w_array[i], w_array[min_id] = w_array[min_id], w_array[i]

    print(w_array[:10])


if __name__ == '__main__':
    simple_sort(array.copy())
