cmake_minimum_required(VERSION 3.10)
project(dgemm_project C)

find_package(BLAS REQUIRED)

add_executable(dgemm
    src/main.c
    src/matrix_io.c
    src/naive.c
    src/benchmark.c
)

target_link_libraries(dgemm ${BLAS_LIBRARIES})
