import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer datos
df = pd.read_csv("data/results.csv")

# ===============================
# 📊 GRÁFICA 1: TIEMPO vs TAMAÑO
# ===============================

plt.figure(figsize=(9,6))

plt.errorbar(
    df["size"], df["blas_mean"], yerr=df["blas_std"],
    marker='o', linewidth=2, capsize=4,
    label="BLAS (Optimizado)"
)

plt.errorbar(
    df["size"], df["naive_mean"], yerr=df["naive_std"],
    marker='s', linewidth=2, capsize=4,
    label="Multiplicación clásica de matrices"
)

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Tamaño de la matriz (N × N)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de rendimiento: DGEMM")

plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()

plt.tight_layout()
plt.savefig("data/performance.png", dpi=300)
plt.show()

# =====================================
# 📈 GRÁFICA 2: AJUSTE TEÓRICO (log-log)
# =====================================

# Solo método clásico
x = np.log(df["size"])
y = np.log(df["naive_mean"])

# Ajuste lineal
coef = np.polyfit(x, y, 1)
pendiente = coef[0]

print(f"\n📈 Pendiente estimada (orden de complejidad): {pendiente:.3f}")

# Recta ajustada
y_fit = np.polyval(coef, x)

plt.figure(figsize=(8,6))

plt.plot(x, y, 'o', label="Datos experimentales")
plt.plot(x, y_fit, '-', label=f"Ajuste lineal (pendiente ≈ {pendiente:.2f})")

plt.xlabel("log(N)")
plt.ylabel("log(Tiempo)")
plt.title("Validación experimental de complejidad O(n³)")

plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("data/complexity_fit.png", dpi=300)
plt.show()
