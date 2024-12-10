from sys import argv
from time import perf_counter_ns, process_time_ns

# Though ctypes provides a builtin wrapper for the C float type, the one
# provided by numpy is arguably tidier and more Pythonic, integrating well with
# other numpy operations. We'll also use the numpy RNG for consistency.
from numpy import float32
from numpy.random import uniform

smallest = 0
largest = 256

def print_matrix(matrix: list[list[float32]], name: str) -> None:
    title = f'Matrix {name}'
    print(title)
    print('=' * len(title))

    longest_length = max(len(f'{column:.9f}') for row in matrix for column in row)

    for row in matrix:
        for column in row:
            padded_number = f'{column:>{longest_length}.9f}'
            print(padded_number, end='  ')
        print()
    print()

def random_float32(min: float32, max: float32) -> float32:
    return float32(uniform(min, max))

n = int(argv[1] if len(argv) > 1 else 0)

A = []
B = []
C = []

for row in range(n):
    A.append([])
    B.append([])
    C.append([])
    for column in range(n):
        A[row].append(random_float32(smallest, largest))
        B[row].append(random_float32(smallest, largest))
        C[row].append(float32(0))

start_elapsed = perf_counter_ns()
start_cpu = process_time_ns()
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]
end_cpu = process_time_ns()
end_elapsed = perf_counter_ns()

start_timer_elapsed = perf_counter_ns()
start_timer_cpu = process_time_ns()
end_timer_cpu = process_time_ns()
end_timer_elapsed = perf_counter_ns()

elapsed_cpu_timer_time = end_timer_elapsed - start_timer_elapsed

elapsed_time = end_elapsed - start_elapsed
adjusted_elapsed_time = elapsed_time - elapsed_cpu_timer_time
cpu_time = end_cpu - start_cpu

print(
    f'Elapsed time:\t\t{elapsed_time / 10 ** 9:.4f}s '
    f'({elapsed_time / 10 ** 3:.0f}us)'
)

print(
    f'Adjusted elapsed time:\t{adjusted_elapsed_time / 10 ** 9:.4f}s '
    f'({adjusted_elapsed_time / 10 ** 3:.0f}us)'
)

print(
    f'CPU time:\t\t{cpu_time / 10 ** 9:.4f}s '
    f'({cpu_time / 10 ** 3:.0f}us)'
)
