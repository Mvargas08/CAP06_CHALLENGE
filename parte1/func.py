import math
def es_primo_v0(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def es_primo(num):
    # Verificar si el número es un booleano
    if isinstance(num, bool):
        raise TypeError("El input no debe ser un valor booleano.")
    
    # Verificar si el número es un flotante (entero o no)
    if isinstance(num, float):
        raise TypeError("El input debe ser un número entero.")  # Lanzar TypeError para cualquier flotante
    
    # Verificar si el número es un entero
    if not isinstance(num, int):
        raise TypeError("El input debe ser un número entero.")
    
    # Números menores o iguales a 1 no son primos
    if num <= 1:
        return False

    # Verificar divisibilidad solo hasta la raíz cuadrada de num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True



if __name__ == "__main__":
    print(es_primo(5))
