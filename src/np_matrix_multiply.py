from sys import argv
import numpy as np
from time import perf_counter_ns, process_time_ns

smallest = 0
largest = 256

def print_matrix(matrix: np.ndarray, name: str) -> None:
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

n = int(argv[1] if len(argv) > 1 else 0)

A = np.random.uniform(smallest, largest + 1, size=(n, n)).astype(np.float32)
B = np.random.uniform(smallest, largest + 1, size=(n, n)).astype(np.float32)

start_elapsed = perf_counter_ns()
start_cpu = process_time_ns()

C = np.matmul(A, B)

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
