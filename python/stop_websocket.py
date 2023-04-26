import time

file= 'closing.txt'
# Abrimos el archivo en modo escritura
with open(file, 'w') as f:
    # Escribimos el valor 1 en el archivo
    print("writing 1")
    f.write('1')

# Esperamos 5 segundos
time.sleep(5)

# Abrimos el archivo en modo escritura
with open(file, 'w') as f:
    # Escribimos el valor 0 en el archivo
    print("writing 0")
    f.write('0')
