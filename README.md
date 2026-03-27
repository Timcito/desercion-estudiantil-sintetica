# Dataset sintético de deserción estudiantil

Este dataset sintético simula información de estudiantes universitarios para predecir si desertan o no durante el primer año académico.

## Tamaño
- Registros: 500
- Variable objetivo: `desercion` (si/no)

## Variables

### Identificación
- `id_estudiante`: entero único por estudiante.

### Demográficas
- `edad`: numérica, rango aproximado 16 a 35, con algunos valores atípicos.
- `genero`: categórica, valores `F` y `M`.
- `lugar_origen`: categórica, valores como Barranquilla, Cartagena, Santa Marta, Monteria y Otra.

### Académicas
- `promedio_bachillerato`: numérica, rango 0.0 a 5.0.
- `puntaje_admision`: numérica, rango aproximado 200 a 500, con algunos outliers.
- `nota_primer_semestre`: numérica, rango 0.0 a 5.0.

### Financieras
- `nivel_socioeconomico`: categórica/ordinal, valores de 1 a 5.
- `beca`: categórica, valores `si` y `no`.
- `prestamo`: categórica, valores `si` y `no`.
- `ayuda_financiera`: categórica, valores `si` y `no`.

### Variable objetivo
- `desercion`: categórica binaria, valores `si` y `no`.

## Valores nulos
Se introdujeron valores nulos de forma aleatoria en variables numéricas como `edad`, `promedio_bachillerato`, `puntaje_admision` y `nota_primer_semestre`.

## Valores atípicos
Se introdujeron outliers manualmente en:
- `edad`: valores como 45, 50, 52 y 60.
- `puntaje_admision`: valores como 50, 80, 700 y 900.

## Uso
Este dataset puede utilizarse para tareas de clasificación binaria en machine learning, especialmente con modelos como regresión logística, árboles de decisión o random forest.
