#include <stdio.h>
#include <stdlib.h>
#include "matrix_io.h"

double* read_matrix(const char *filename, int n) {
    FILE *f = fopen(filename, "r");
    if (!f) {
        perror("Error opening file");
        return NULL;
    }

    double *M = (double*) malloc(n * n * sizeof(double));

    for (int i = 0; i < n*n; i++) {
        if (fscanf(f, "%lf", &M[i]) != 1) {
            printf("Error reading matrix\n");
            fclose(f);
            free(M);
            return NULL;
        }
    }

    fclose(f);
    return M;
}

void write_matrix(const char *filename, const double *M, int n) {
    FILE *f = fopen(filename, "w");

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            fprintf(f, "%lf ", M[i*n + j]);
        }
        fprintf(f, "\n");
    }

    fclose(f);
}
