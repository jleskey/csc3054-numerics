#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define smallest 0
#define largest 256

double std_rand();
int rand_int(int min, int max);

int main(int argc, char* argv[]) {
    int n = argc > 1 ? atoi(argv[1]) : 0;

    srand(time(NULL));

    int** A = (int**) malloc(n * sizeof(int*));
    int** B = (int**) malloc(n * sizeof(int*));
    int** C = (int**) malloc(n * sizeof(int*));

    for (int i = 0; i < n; i++) {
        A[i] = (int*) malloc(n * sizeof(int));
        B[i] = (int*) malloc(n * sizeof(int));
        C[i] = (int*) malloc(n * sizeof(int));
        for (int j = 0; j < n; j++) {
            A[i][j] = rand_int(smallest, largest);
            B[i][j] = rand_int(smallest, largest);
            C[i][j] = 0;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    for (int i = 0; i < n; i++) {
        free(A[i]);
        free(B[i]);
        free(C[i]);
    }
    free(A);
    free(B);
    free(C);

    return 0;
}

double std_rand() {
    return rand() / (RAND_MAX + 1.0);
}

int rand_int(int min, int max) {
    return min + std_rand() * (max - min + 1);
}
