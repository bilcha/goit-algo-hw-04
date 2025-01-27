import timeit
import random

data = [60, 60, 4, 95, 88, 94, 38, 82, 81, 84, 64, 20, 11, 47, 94, 91, 84, 82, 83, 21, 81, 5, 33, 6, 82, 88, 30, 40, 21]

random_datadata = [random.randint(0, 1000) for _ in range(1000)]

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged



def compare_algorithms(n):
    times = []

    times.append(("Insertion Sort", timeit.timeit(lambda: insertion_sort(n[:]), number=1)))

    times.append(("Merge Sort", timeit.timeit(lambda: merge_sort(n[:]), number=1)))

    times.append(("Built-in Sort", timeit.timeit(lambda: sorted(n), number=1)))

    times.sort(key=lambda x: x[1])

    print("Sorting algorithms ranked by time:")
    for algo, time_taken in times:
        print(f"{algo}: {time_taken:.6f} seconds")

compare_algorithms(data)

print("------------------- Compare with bigger data scope -------------------")
# compare with bigger scope
compare_algorithms(random_datadata)


''' 
  Best result for build-in sorting, 
  Insertion sort works good for smaller scope of data, but for bigger Merge Sort is better than Insertion
'''