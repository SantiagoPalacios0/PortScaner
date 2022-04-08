import sys
import socket

Target = socket.gethostbyname(input("Ingrese la IP de su objetivo: "))

print("Escaneando objetivo " + Target + " Esto puede tomar un minuto...")

try:
    for port in range(1,150):
        escaneo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = escaneo.connect_ex((Target, port))
        if resultado == 0:
            print("El puerto {} esta abierto".format(port))
            escaneo.close()
except:
    print("\n Terminando escaneo...")
    sys.exit(0)

