def calcular_tiempo_de_escritura(s):
    # Tiempo para escribir el primer carácter
    tiempo = 2
    # Iterar sobre cada carácter en la cadena a partir del segundo
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            # Si el carácter es el mismo que el anterior, toma 1 segundo
            tiempo += 1
        else:
            # Si el carácter es diferente al anterior, toma 2 segundos
            tiempo += 2
    return tiempo

def encontrar_contraseña_con_tiempo_maximo(s):
    tiempo_maximo = 0
    mejor_contraseña = s
    # Probar insertar cada letra del alfabeto en cada posición posible
    for i in range(len(s) + 1):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            nueva_contraseña = s[:i] + c + s[i:]
            tiempo_actual = calcular_tiempo_de_escritura(nueva_contraseña)
            # Actualizar si encontramos un tiempo mayor
            if tiempo_actual > tiempo_maximo:
                tiempo_maximo = tiempo_actual
                mejor_contraseña = nueva_contraseña
    return mejor_contraseña

cases = int(input())

for _ in range(cases):
    s = input()
    print(encontrar_contraseña_con_tiempo_maximo(s))