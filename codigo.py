import numpy as np
import pandas as pd

np.random.seed(42)

n = 500

df = pd.DataFrame({
    "id_estudiante": range(1, n + 1),
    "edad": np.random.randint(16, 35, n),
    "genero": np.random.choice(["F", "M"], n),
    "lugar_origen": np.random.choice(["Barranquilla", "Cartagena", "Santa Marta", "Monteria", "Otra"], n),
    "promedio_bachillerato": np.round(np.random.normal(3.2, 0.6, n), 2),
    "puntaje_admision": np.random.randint(200, 500, n),
    "nota_primer_semestre": np.round(np.random.normal(3.0, 0.8, n), 2),
    "nivel_socioeconomico": np.random.choice([1, 2, 3, 4, 5], n),
    "beca": np.random.choice(["si", "no"], n),
    "prestamo": np.random.choice(["si", "no"], n),
    "ayuda_financiera": np.random.choice(["si", "no"], n),
})

df["promedio_bachillerato"] = df["promedio_bachillerato"].clip(0.0, 5.0)
df["nota_primer_semestre"] = df["nota_primer_semestre"].clip(0.0, 5.0)

riesgo = (
    (df["nota_primer_semestre"] < 2.8).astype(int) +
    (df["puntaje_admision"] < 320).astype(int) +
    (df["nivel_socioeconomico"] <= 2).astype(int) +
    (df["beca"] == "no").astype(int) +
    (df["ayuda_financiera"] == "no").astype(int)
)

prob = 1 / (1 + np.exp(-(riesgo - 2)))
df["desercion"] = np.where(np.random.rand(n) < prob, "si", "no")

for col in ["edad", "promedio_bachillerato", "puntaje_admision", "nota_primer_semestre"]:
    idx = np.random.choice(df.index, size=10, replace=False)
    df.loc[idx, col] = np.nan

outlier_idx = np.random.choice(df.index, size=8, replace=False)
df.loc[outlier_idx[:4], "edad"] = [45, 50, 52, 60]
df.loc[outlier_idx[4:], "puntaje_admision"] = [50, 80, 700, 900]

df.to_csv("dataset_desercion.csv", index=False)

print(df.head())
print(df.isnull().sum())

df.to_csv("dataset_desercion.csv", index=False)
