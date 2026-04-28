#ifndef BENCHMARK_H
#define BENCHMARK_H

double benchmark_blas(int n, const double *A, const double *B, double *C);
double benchmark_naive(int n, const double *A, const double *B, double *C);

#endif
