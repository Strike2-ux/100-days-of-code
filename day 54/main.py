import csv

total = 0.0

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    total += float(row["Quantity"]) * float(row["Cost"])

print(f"Total: ${round(total,2)}")


'''
from pathlib import Path
import csv
from decimal import Decimal, ROUND_HALF_UP

def calcular_total(ruta_archivo):
    total = Decimal('0.00')  # Inicializar el total usando Decimal para un cálculo decimal preciso
    
    # Verificar si el archivo existe
    if not Path(ruta_archivo).is_file():
        raise FileNotFoundError("El archivo especificado no existe.")

    try:
        with open(ruta_archivo, "r", newline="") as archivo:
            lector = csv.DictReader(archivo)
            columnas_requeridas = ["Cantidad", "Costo"]
            
            # Verificar si las columnas requeridas están presentes
            if not all(columna in lector.fieldnames for columna in columnas_requeridas):
                raise ValueError("Faltan columnas requeridas en el archivo CSV.")

            for fila in lector:
                cantidad = Decimal(fila["Cantidad"])
                costo = Decimal(fila["Costo"])
                total += cantidad * costo
    except Exception as e:
        raise RuntimeError("Ocurrió un error al procesar los datos del archivo CSV.") from e

    return total

if __name__ == "__main__":
    ruta_archivo = "Day54Totals.csv"
    
    try:
        monto_total = calcular_total(ruta_archivo)
        monto_total_formateado = monto_total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        print(f"Total: ${monto_total_formateado}")
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"Error: {e}")

'''