telefono = input("Introduce el número de teléfono con el formato prefijo-número-extensión: ")
numero_principal = telefono.split('-')[1]
print(f"El número sin prefijo y extensión es: {numero_principal}")
