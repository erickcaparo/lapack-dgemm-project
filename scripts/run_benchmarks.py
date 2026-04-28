import subprocess
import csv
import numpy as np

# Tamaños más densos (curva suave real)
sizes = [50, 75, 100, 125, 150, 200, 300, 400, 600, 800, 1000]

# Número de repeticiones por tamaño
repeats = 5

# Archivo CSV
output_file = "data/results.csv"

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    
    # Cabecera
    writer.writerow([
        "size",
        "blas_mean", "blas_std",
        "naive_mean", "naive_std"
    ])

    for n in sizes:
        print(f"\n🚀 Tamaño {n}")

        blas_times = []
        naive_times = []

        for i in range(repeats):
            print(f"  → Repetición {i+1}/{repeats}")

            # Generar matrices
            subprocess.run(["python3", "scripts/generate_matrices.py", str(n)])

            # Ejecutar programa
            result = subprocess.run(
                ["./build/dgemm", str(n)],
                capture_output=True,
                text=True
            )

            output = result.stdout

            # Extraer tiempos
            for line in output.split("\n"):
                if "BLAS time" in line:
                    blas_times.append(float(line.split()[2]))
                elif "Naive time" in line:
                    naive_times.append(float(line.split()[2]))

        # Estadísticas
        blas_mean = np.mean(blas_times)
        blas_std = np.std(blas_times)

        naive_mean = np.mean(naive_times)
        naive_std = np.std(naive_times)

        # Guardar en CSV
        writer.writerow([
            n,
            blas_mean, blas_std,
            naive_mean, naive_std
        ])

print("\n📊 Resultados guardados en data/results.csv")
