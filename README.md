# 🚀 LAPACK DGEMM Benchmark Project

## 🧠 Descripción

Este proyecto implementa un sistema completo de **benchmarking para multiplicación de matrices densas**, comparando:

* 🔹 Implementación clásica (naive)
* 🔹 Implementación optimizada usando **BLAS (`cblas_dgemm`)**

El objetivo es evaluar el rendimiento real, analizar la escalabilidad y demostrar el impacto de bibliotecas optimizadas en computación científica.

---

## 🏗️ Arquitectura del Sistema

El proyecto sigue un pipeline reproducible:

```
Generación de matrices → Ejecución (C) → Benchmark → CSV → Visualización
```

### 🔁 Flujo completo

1. `generate_matrices.py`

   * Genera matrices aleatorias `A` y `B`

2. `main.c`

   * Lee matrices desde `data/`
   * Ejecuta:

     * DGEMM (BLAS)
     * Implementación naive
   * Valida resultados

3. `benchmark.c`

   * Mide tiempos de ejecución

4. `run_benchmarks.py`

   * Automatiza pruebas para múltiples tamaños
   * Ejecuta múltiples repeticiones
   * Calcula media y desviación estándar

5. `plot_results.py`

   * Genera gráficas de rendimiento

---

## 📁 Estructura del Proyecto

```
lapack-dgemm-project/
│
├── src/
│   ├── main.c
│   ├── benchmark.c
│   ├── naive.c
│   ├── matrix_io.c
│
├── scripts/
│   ├── generate_matrices.py
│   ├── run_benchmarks.py
│   └── plot_results.py
│
├── data/
│   ├── input_A.txt
│   ├── input_B.txt
│   ├── results.csv
│   ├── performance.png
│   └── complexity_fit.png
│
├── build/
├── CMakeLists.txt
├── Makefile
└── README.md
```

---

## ⚙️ Requisitos

### 🔧 Sistema

* Linux (probado en Kali)
* GCC / G++
* CMake

### 📚 Librerías

* BLAS / LAPACK (OpenBLAS recomendado)
* Python 3

### 🐍 Python

```bash
pip install numpy pandas matplotlib
```

---

## 🧮 Fundamento Teórico

La multiplicación de matrices tiene complejidad:

```
O(n³)
```

Sin embargo, implementaciones optimizadas como **DGEMM**:

* Usan vectorización SIMD
* Optimizan uso de caché
* Paralelizan operaciones

👉 Resultado: **mejor rendimiento real sin cambiar la complejidad teórica**

---

## ⚙️ Compilación

```bash
mkdir build
cd build
cmake ..
make
```

---

## ▶️ Ejecución Manual

```bash
./build/dgemm 100
```

### 📌 Salida esperada:

```
BLAS time:  0.0023 seconds
Naive time: 0.1456 seconds
Results match ✅
```

---

## ⏱️ Sistema de Benchmark

El archivo `run_benchmarks.py` ejecuta pruebas automáticas:

### 🔁 Características:

* Tamaños de matriz:

  ```
  50 → 1000
  ```
* 5 repeticiones por tamaño
* Generación automática de matrices
* Extracción de tiempos desde stdout
* Cálculo de:

  * media (`mean`)
  * desviación estándar (`std`)

---

## 🚀 Ejecutar Benchmark Completo

```bash
python3 scripts/run_benchmarks.py
```

Esto genera:

```
data/results.csv
```

---

## 📊 Visualización

```bash
python3 scripts/plot_results.py
```

Genera:

* 📈 `performance.png` → comparación directa
* 📉 `complexity_fit.png` → ajuste de complejidad

---

## 🔍 Validación Numérica

El sistema verifica la correcta implementación:

```c
diff += fabs(C_blas[i] - C_naive[i]);
```

Criterio:

```
diff < 1e-6 → resultados correctos
```

👉 Esto garantiza integridad numérica del benchmark.

---

## 🧠 Análisis Técnico

### 🔹 DGEMM (BLAS)

```c
cblas_dgemm(...)
```

Implementa:

```
C = αAB + βC
```

Ventajas:

* Optimización a nivel de hardware
* Uso eficiente de memoria caché
* Paralelismo interno

---

### 🔹 Implementación Naive

```c
naive_dgemm(...)
```

* Triple bucle clásico
* Sin optimización
* Referencia base para comparación

---

## 📈 Resultados Esperados

* DGEMM supera ampliamente al método naive
* Diferencia crece con el tamaño de matriz
* Curva experimental ≈ O(n³)

---

## 🔁 Reproducibilidad

```bash
Clonar el repositorio.

cd lapack-dgemm-project

mkdir build && cd build
cmake .. && make

cd ..
python3 scripts/run_benchmarks.py
python3 scripts/plot_results.py
```

---

## 📚 Aplicaciones

* Machine Learning
* Simulación numérica
* Procesamiento de señales
* Ingeniería estructural
* HPC (High Performance Computing)

---

## 👨‍💻 Autor

**Erick Fosh Caparó Chávez**
Ingeniero Civil | Maestría en Ciencias de la Computación.

---

## 🏆 Valor del Proyecto

Este proyecto demuestra:

✔ Uso de librerías científicas reales (BLAS)
✔ Benchmarking reproducible
✔ Validación numérica
✔ Automatización completa
✔ Visualización de resultados

👉 Nivel: **Computación científica aplicada / HPC básico**

---

## ⭐ Posibles Mejoras

* Uso de OpenMP (paralelismo)
* Medición con `omp_get_wtime()`
* Implementación bloqueada (cache-aware)
* Comparación con Strassen
* Versión GPU (CUDA)

---

## 📎 Licencia

Uso académico y educativo.

