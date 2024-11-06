import pytest
from func import es_primo

# Test para números primos pequeños a medianos
@pytest.mark.parametrize("num", [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71
])
def test_numeros_primos(num):
    assert es_primo(num) == True, f"Error: {num} debería ser primo"

# Test para números no primos comunes
@pytest.mark.parametrize("num", [
    1, 4, 6, 8, 9, 10, 12, 14, 15, 16,
    18, 20, 21, 22, 24, 25, 26, 27, 28, 30
])
def test_numeros_no_primos(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Números no positivos
@pytest.mark.parametrize("num", [0, -1, -2, -10, -17])
def test_numeros_no_positivos(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Flotantes
@pytest.mark.parametrize("num", [1.1, 3.1416, 5.5, -7.7, 2.0])
def test_flotantes(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Cadenas de texto
@pytest.mark.parametrize("num", ["10", "three", "100", "", " "])
def test_cadenas_de_texto(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Otros tipos de datos
@pytest.mark.parametrize("num", [None, [], {}, False, True, [5]])
def test_otros_tipos_de_datos(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Números muy grandes
@pytest.mark.parametrize("num", [
    10**10 + 7, 2**31 - 1, 10**20 + 9, 10**20 - 35, 10**100
])
def test_numeros_muy_grandes(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Primos grandes conocidos
@pytest.mark.parametrize("num", [7919, 104729, 1299709, 15485863, 32452843])
def test_primos_grandes_conocidos(num):
    assert es_primo(num) == True, f"Error: {num} debería ser primo"

# Números grandes no primos o dudosos
@pytest.mark.parametrize("num", [10**10, 10**10 + 1, 2**32, 2**64, 10**18 + 1])
def test_numeros_grandes_no_primos(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Precisión en números flotantes cercanos a primos enteros
@pytest.mark.parametrize("num", [
    2.0000000000000004, 3.0000000000000004, 5.0000000000000004, 
    7.0000000000000004, 11.000000000000004, 13.000000000000004, 
    17.000000000000004, 19.000000000000004, 23.000000000000004, 
    29.000000000000004, 31.000000000000004, 37.000000000000004,
    41.000000000000004, 43.000000000000004, 47.000000000000004,
    53.000000000000004, 59.000000000000004, 61.000000000000004,
    67.000000000000004, 71.000000000000004
])
def test_flotantes_cercanos_a_primos(num):
    assert es_primo(num) == True, f"Error: {num} debería ser reconocido como primo"
