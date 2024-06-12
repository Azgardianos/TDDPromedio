def calcular_promedio(conjunto):
    if len(conjunto) == 0:
        return 0
    return sum(conjunto) / len(conjunto)

# Ejemplo de uso
conjunto = [1, 2, 3, 4, 5]
promedio = calcular_promedio(conjunto)
print(f"El promedio es: {promedio}")
