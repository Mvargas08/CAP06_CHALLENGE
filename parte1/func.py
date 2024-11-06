import math
def es_primo_v0(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def es_primo(num):
    # Validar que la entrada sea un número entero o un flotante cercano a un entero primo
    if isinstance(num, float):
        if not num.is_integer():
            num = round(num)  # Redondear flotantes cercanos a números enteros
        else:
            num = int(num)  # Convertir flotantes enteros a int para evitar errores
    
    # Verificar si el número es un entero
    if not isinstance(num, int):
        return False
    
    # Los números menores o iguales a 1 no son primos
    if num <= 1:
        return False
    
    # Optimización: verificar hasta la raíz cuadrada de num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(es_primo(5))
