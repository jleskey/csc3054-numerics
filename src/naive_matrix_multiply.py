from sys import argv
from random import randint
from time import perf_counter_ns, process_time_ns

smallest = 0
largest = 256

def print_matrix(matrix: list[list[int]], name: str) -> None:
    title = f'Matrix {name}'
    print(title)
    print('=' * len(title))

    longest_length = max(len(str(column)) for row in matrix for column in row)

    for row in matrix:
        for column in row:
            padded_number = f'{column:>{longest_length}}'
            print(padded_number, end=' ')
        print()
    print()

n = int(argv[1] if len(argv) > 1 else 0)

A = []
B = []
C = []

for row in range(n):
    A.append([])
    B.append([])
    C.append([])
    for column in range(n):
        A[row].append(randint(smallest, largest))
        B[row].append(randint(smallest, largest))
        C[row].append(0)

start_elapsed = perf_counter_ns()
start_cpu = process_time_ns()
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] + B[k][j]
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
