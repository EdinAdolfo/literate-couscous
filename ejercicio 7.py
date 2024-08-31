correo = input("Introduce tu correo electrónico: ")
nombre_correo = correo.split('@')[0]
nuevo_correo = f"{nombre_correo}@ceu.es"
print(f"Tu nuevo correo es: {nuevo_correo}")
