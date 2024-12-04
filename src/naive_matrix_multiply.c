#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define smallest 0.0f
#define largest 256.0f

float std_rand();
float rand_float(float min, float max);

int main(int argc, char* argv[]) {
    int n = argc > 1 ? atoi(argv[1]) : 0;

    srand(time(NULL));

    float** A = (float**) malloc(n * sizeof(float*));
    float** B = (float**) malloc(n * sizeof(float*));
    float** C = (float**) malloc(n * sizeof(float*));

    for (int i = 0; i < n; i++) {
        A[i] = (float*) malloc(n * sizeof(float));
        B[i] = (float*) malloc(n * sizeof(float));
        C[i] = (float*) malloc(n * sizeof(float));
        for (int j = 0; j < n; j++) {
            A[i][j] = rand_float(smallest, largest);
            B[i][j] = rand_float(smallest, largest);
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

float std_rand() {
    return rand() / (RAND_MAX + 1.0f);
}

float rand_float(float min, float max) {
    return min + std_rand() * (max - min + 1);
}
