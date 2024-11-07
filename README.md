# Documentación de la Función es_primo()

## Descripción General
La función `es_primo()` implementada en `func.py` determina si un número es primo. Un número primo es aquel que solo es divisible por 1 y por sí mismo.

## Implementación Detallada

### Validaciones de Entrada
1. **Manejo de Flotantes**:
   - Convierte números flotantes a enteros si son cercanos a un número entero
   - Redondea flotantes próximos a números enteros
   - Convierte flotantes enteros a int para evitar errores

2. **Validación de Tipo**:
   - Verifica que la entrada sea un número entero
   - Retorna False para tipos no numéricos

3. **Validación de Rango**:
   - Números menores o iguales a 1 no son considerados primos
   - Retorna False para números negativos

### Algoritmo Principal
- Utiliza optimización verificando hasta la raíz cuadrada del número
- Implementa el método de división por prueba hasta √n
- Complejidad temporal: O(√n)

## Casos de Prueba

### 1. Números Primos Conocidos
- Verifica números primos básicos (2, 3, 5, 7, 11, etc.)
- Asegura que la función retorne True para estos casos

### 2. Números No Primos
- Prueba números compuestos conocidos (4, 6, 8, 9, etc.)
- Verifica casos especiales como 0 y 1
- Asegura que la función retorne False

### 3. Números Negativos
- Prueba números negativos (-1, -2, -3, etc.)
- Verifica que todos sean identificados como no primos

### 4. Números Grandes
- Prueba la eficiencia con números como 1000003 (primo)
- Verifica números grandes no primos como 1000004

### 5. Entradas No Enteras
- Prueba con decimales (2.3, 3.9)
- Verifica manejo de strings ("tres")
- Prueba con valores None y booleanos

### 6. Casos Especiales
- Verifica el comportamiento con listas vacías
- Prueba con strings numéricos
- Valida el manejo de None

### 7. Precisión Flotante
- Verifica números flotantes cercanos a primos
- Prueba casos como 19.000000000000004
- Asegura el correcto redondeo y evaluación

## Uso
```python
from func import es_primo

# Ejemplos de uso
es_primo(5)    # True
es_primo(4)    # False
es_primo(2.0)  # True
```

# Estructura del Proyecto

## Archivos Principales

### `/parte1/func.py`
Contiene la implementación de la función `es_primo()`. Este archivo es el núcleo del proyecto y contiene:
- Implementación base `es_primo_v0()` 
- Implementación optimizada `es_primo()`
- Validaciones y manejo de tipos de datos
- Optimizaciones matemáticas

### `/parte1/func_test.py` 
Suite de pruebas unitarias para validar el funcionamiento de `es_primo()`. Incluye:
- Tests para casos básicos
- Pruebas de edge cases
- Validaciones de tipos
- Pruebas de rendimiento
- Cobertura de casos especiales

## Carpeta de Evidencias

### `/evidencias/`
Contiene capturas y documentación que demuestran:
- Ejecución exitosa de pruebas ***(5 failed, 157 passed in 0.23s)***
- Cobertura de código alcanzada
- Resultados de pruebas de rendimiento
- Ejecución de pruebas unitarias
- Conversación con la IA ChatGPT y Cody
- Capturas de pantalla y detalles de la conversación

## Reporte de Cobertura de Pruebas

La cobertura de pruebas fue analizada usando pytest-cov, alcanzando los siguientes resultados por archivo:

### func_test.py
- Cobertura total: 100%
- Líneas cubiertas: 12/12 
- Ramas cubiertas: 4/4

### reference_test.py
- Cobertura total: 100%
- Líneas cubiertas: 40/40
- Ramas cubiertas: 8/8

### solucion/solucion_test.py  
- Cobertura total: 100%
- Líneas cubiertas: 40/40
- Ramas cubiertas: 8/8

Para ejecutar el reporte de cobertura completo:

```bash
pytest --cov=. parte1/
