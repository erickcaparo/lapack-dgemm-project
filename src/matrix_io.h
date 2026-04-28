#ifndef MATRIX_IO_H
#define MATRIX_IO_H

double* read_matrix(const char *filename, int n);
void write_matrix(const char *filename, const double *matrix, int n);

#endif
