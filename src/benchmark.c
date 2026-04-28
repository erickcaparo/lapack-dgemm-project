#include <time.h>
#include <string.h>
#include <cblas.h>

#include "benchmark.h"
#include "naive.h"

double benchmark_blas(int n, const double *A, const double *B, double *C) {
    clock_t start = clock();

    cblas_dgemm(
        CblasRowMajor,
        CblasNoTrans,
        CblasNoTrans,
        n, n, n,
        1.0,
        A, n,
        B, n,
        0.0,
        C, n
    );

    clock_t end = clock();
    return (double)(end - start) / CLOCKS_PER_SEC;
}

double benchmark_naive(int n, const double *A, const double *B, double *C) {
    clock_t start = clock();

    naive_dgemm(n, A, B, C);

    clock_t end = clock();
    return (double)(end - start) / CLOCKS_PER_SEC;
}
