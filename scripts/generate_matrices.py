import sys
import numpy as np

# Argumentos
n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
seed = int(sys.argv[2]) if len(sys.argv) > 2 else 42

np.random.seed(seed)

print(f"🔧 Generando matrices {n}x{n} con seed={seed}")

A = np.random.rand(n, n)
B = np.random.rand(n, n)

np.savetxt("data/input_A.txt", A)
np.savetxt("data/input_B.txt", B)

print(" Matrices generadas correctamente")
