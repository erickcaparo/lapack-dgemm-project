#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "matrix_io.h"
#include "benchmark.h"

int main(int argc, char *argv[]) {

    if (argc < 2) {
        printf("Usage: %s <matrix_size>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);

    // Leer matrices
    double *A = read_matrix("data/input_A.txt", n);
    double *B = read_matrix("data/input_B.txt", n);

    if (!A || !B) {
        printf("Error loading matrices\n");
        return 1;
    }

    double *C_blas = (double*) malloc(n * n * sizeof(double));
    double *C_naive = (double*) malloc(n * n * sizeof(double));

    // Benchmark
    double time_blas = benchmark_blas(n, A, B, C_blas);
    double time_naive = benchmark_naive(n, A, B, C_naive);

    printf("BLAS time:  %f seconds\n", time_blas);
    printf("Naive time: %f seconds\n", time_naive);

    // Validación
    double diff = 0.0;
    for (int i = 0; i < n*n; i++) {
        diff += fabs(C_blas[i] - C_naive[i]);
    }

    if (diff < 1e-6) {
        printf("Results match ✅\n");
    } else {
        printf("Results differ ❌ (diff=%f)\n", diff);
    }

    free(A);
    free(B);
    free(C_blas);
    free(C_naive);

    return 0;
}
