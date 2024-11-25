import re
import subprocess
import ipaddress
from datetime import datetime  # Importamos datetime para manejar fechas y horas

def ping(ip, intentos=1):
    try:
        response = subprocess.run(
            ["ping", "-n", str(intentos), ip], capture_output=True, text=True, timeout=5
        )
        output = response.stdout.lower()

        if "ttl=" in output:
            print(f"{ip} está respondiendo.")
            return True
        else:
            print(f"{ip} no respondió.")
            return False
    except subprocess.TimeoutExpired:
        print(f"{ip} no respondió (timeout alcanzado).")
        return False

def main_script():
    # Rango de IPs a escanear
    inicio = ipaddress.IPv4Address("ACA PONES LA IP DONDE COMIENZA EL RANGO")
    fin = ipaddress.IPv4Address("ACA PONES LA IP DONDE FINALIZA EL RANGO")

    # Número de intentos de ping por IP
    intentos = 1

    # Crear nombre único basado en fecha y hora
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"resultados_{timestamp}.txt"

    with open(filename, "w") as archivo:
        for ip in range(int(inicio), int(fin) + 1):
            current_ip = str(ipaddress.IPv4Address(ip))
            if ping(current_ip, intentos):
                archivo.write(current_ip + "\n")
    print(f"Resultados guardados en {filename}")

if __name__ == "__main__":
    print("Iniciando escaneo de rango de IPs con un intento de ping...")
    main_script()
