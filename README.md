# Sorting Algorithm Comparison in Task_1

This Python script compares the performance of three sorting algorithms: **Insertion Sort**, **Merge Sort**, and Python's built-in `sorted()` function. It evaluates their efficiency on a small dataset and a larger randomly generated dataset.

## Features

1. **Insertion Sort**: A simple sorting algorithm effective for small datasets.
2. **Merge Sort**: A divide-and-conquer algorithm that handles larger datasets more efficiently.
3. **Built-in Sort**: Python's optimized sorting method, using Timsort.

## How It Works

- The script defines `insertion_sort`, `merge_sort`, and a helper function `merge` for merging sorted arrays.
- It generates two datasets:
  - `data`: A small predefined list.
  - `random_datadata`: A larger randomly generated list of 1000 integers.
- The `compare_algorithms` function:
  - Executes each sorting algorithm.
  - Measures execution time using the `timeit` module.
  - Ranks the algorithms based on their performance.

## Execution

Run the script to compare sorting times:

```bash
python main.py
```

### Sample Output

```
Sorting algorithms ranked by time:
Built-in Sort: 0.000001 seconds
Insertion Sort: 0.000020 seconds
Merge Sort: 0.000010 seconds
------------------- Compare with bigger data scope -------------------
Sorting algorithms ranked by time:
Built-in Sort: 0.000100 seconds
Merge Sort: 0.000200 seconds
Insertion Sort: 0.500000 seconds
```

## Observations

- **Built-in Sort** consistently performs the fastest.
- **Insertion Sort** works well for small datasets but struggles with larger data.
- **Merge Sort** is a better choice for larger datasets compared to Insertion Sort.

## Dependencies

- Python 3.x
- `timeit` (standard library)
- `random` (standard library)

## Notes

- This script is a simple demonstration of sorting algorithms and their performance characteristics.
- The results may vary depending on the system and dataset used.
