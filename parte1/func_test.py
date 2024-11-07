import pytest
from func import es_primo

# Test para números primos pequeños a medianos
@pytest.mark.parametrize("num", [2, 3, 5, 7, 13])
def test_primos_pequenos_a_medianos(num):
    assert es_primo(num) == True, f"Error: {num} debería ser primo"

# Test para números no primos comunes
@pytest.mark.parametrize("num", [4, 6, 8, 9, 12])
def test_no_primos_comunes(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Números no positivos
@pytest.mark.parametrize("num", [-10, -1, 0, 1, -5])
def test_numeros_no_positivos(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Flotantes (se espera que lancen un TypeError)
@pytest.mark.parametrize("num", [2.5, 4.5, 5.1, 9.9, 15.3])
def test_flotantes(num):
    with pytest.raises(TypeError, match="El input debe ser un número entero."):
        es_primo(num)

# Cadenas de texto (deberían lanzar un TypeError)
@pytest.mark.parametrize("num", ["texto", "123", "True", "", "None"])
def test_cadenas_texto(num):
    with pytest.raises(TypeError, match="El input debe ser un número entero."):
        es_primo(num)

# Otros tipos de datos (deberían lanzar un TypeError)
@pytest.mark.parametrize("num", [[1, 2, 3], {1: "one"}, (1, 2), None, set()])
def test_otros_tipos_datos(num):
    with pytest.raises(TypeError, match="El input debe ser un número entero."):
        es_primo(num)

# Primos grandes conocidos
@pytest.mark.parametrize("num", [101, 103, 107, 109, 113])
def test_primos_grandes_conocidos(num):
    assert es_primo(num) == True, f"Error: {num} debería ser primo"

# Números grandes no primos o dudosos
@pytest.mark.parametrize("num", [104, 108, 110, 114, 120])
def test_numeros_grandes_no_primos(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Pruebas para números primos conocidos
@pytest.mark.parametrize("num", [7, 11, 17, 19, 23])
def test_pruebas_primos_conocidos(num):
    assert es_primo(num) == True, f"Error: {num} debería ser primo"

# Pruebas para números no primos
@pytest.mark.parametrize("num", [9, 14, 15, 16, 18])
def test_pruebas_no_primos(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Pruebas para números no positivos
@pytest.mark.parametrize("num", [0, -2, -8, -20, -100])
def test_pruebas_no_positivos(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Pruebas para entradas de tipo booleano
@pytest.mark.parametrize("num", [True, False])
def test_tipo_booleano(num):
    with pytest.raises(TypeError, match="El input no debe ser un valor booleano."):
        es_primo(num)

# Pruebas para entradas no numéricas
@pytest.mark.parametrize("num", [None, "abc", {}, [], (1,)])
def test_tipo_no_numerico(num):
    with pytest.raises(TypeError, match="El input debe ser un número entero."):
        es_primo(num)

# Pruebas para flotantes enteros que deberían generar un TypeError
@pytest.mark.parametrize("num", [2.0, 3.0, 5.0, 7.0, 11.0])
def test_flotantes_enteros(num):
    with pytest.raises(TypeError, match="El input debe ser un número entero."):
        es_primo(num)

# Pruebas para números muy grandes (cercanos a la capacidad máxima)
@pytest.mark.parametrize("num", [10*18 + 5, 10*18 + 3, 10*18 + 11, 10*18 + 13, 10*18 + 17])
def test_numeros_extremadamente_grandes(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Ejemplos de grandes números primos
@pytest.mark.parametrize("num", [1299709, 15485863, 32452843, 49979687, 67867967])
def test_grandes_numeros_primos(num):
    assert es_primo(num) == True, f"Error: {num} debería ser primo"

# Ejemplos de grandes números no primos
@pytest.mark.parametrize("num", [1299710, 15485864, 32452844, 49979688, 67867968])
def test_grandes_numeros_no_primos(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"
