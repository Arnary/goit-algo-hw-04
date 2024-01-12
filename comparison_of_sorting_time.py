from timeit import timeit
import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort

small_data = [random.randint(1, 1000) for _ in range(1000)]
medium_data = [random.randint(1, 10000) for _ in range(10000)]
large_data = [random.randint(1, 100000) for _ in range(100000)]

insertion_small = timeit(lambda: insertion_sort(small_data[:]), number=10)
merge_small = timeit(lambda: merge_sort(small_data[:]), number=10)
sorted_small = timeit(lambda: sorted(small_data[:]), number=10)
sort_small = timeit(lambda: small_data[:].sort(), number=10)

insertion_medium = timeit(lambda: insertion_sort(medium_data[:]), number=10)
merge_medium = timeit(lambda: merge_sort(medium_data[:]), number=10)
sorted_medium = timeit(lambda: sorted(medium_data[:]), number=10)
sort_medium = timeit(lambda: medium_data[:].sort(), number=10)

insertion_large = timeit(lambda: insertion_sort(large_data[:]), number=10)
merge_large = timeit(lambda: merge_sort(large_data[:]), number=10)
sorted_large = timeit(lambda: sorted(large_data[:]), number=10)
sort_large = timeit(lambda: large_data[:].sort(), number=10)

print(f"{'| Algorithm': <17} | {'Processing time for small data': <31} | {'Processing time for medium data': <20} | {'Processing time for large data': <20}")
print(f"| {'-'*15} | {'-'*31} | {'-'*31} | {'-'*31}")
print(f"| {'Insertion sort': <15} | {insertion_small:^31f} | {insertion_medium:^31f} | {insertion_large:^31f}")
print(f"| {'Merge sort': <15} | {merge_small:^31f} | {merge_medium:^31f} | {merge_large:^31f}")
print(f"| {'Python sorted': <15} | {sorted_small:^31f} | {sorted_medium:^31f} | {sorted_large:^31f}")
print(f"| {'Python sort': <15} | {sort_small:^31f} | {sort_medium:^31f} | {sort_large:^31f}")
