'''import datetime

hoy = datetime.date.today()

print("CUENTA REGRESIVA DE EVENTO")
dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))
evento = datetime.date(año, mes, dia)

diferencia = evento - hoy
diferencia = diferencia.days

if diferencia > 0:
    print(f"Faltan {diferencia} días")
elif diferencia < 0:
    print(f"😭😭😭😭😭😭😭 ¡Te lo perdiste por {abs(diferencia)} días!")
else:
    print("🥳🥳🥳🥳🥳🥳🥳 ¡Hoy es el día!")
    '''
import datetime

today = datetime.date.today()

print("EVENT COUNTDOWN")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
event = datetime.date(year, month, day)

difference = event - today
difference = difference.days

if difference>0:
  print(f"{difference} days to go")
elif difference<0:
  print(f"😭😭😭😭😭😭😭 You missed it by {difference} days!")
  
else:
  print("🥳🥳🥳🥳🥳🥳🥳 Today!")
'''
import datetime

def countdown_event(dia, mes, año):
  """Devuelve el número de días hasta un evento dado.

  Argumentos:
    dia: El día del evento.
    mes: El mes del evento.
    año: El año del evento.

  Devuelve:
    El número de días hasta el evento.
  """

  hoy = datetime.date.today()
  evento = datetime.date(año, mes, dia)
  diferencia = evento - hoy
  return diferencia.days

if __name__ == "__main__":
  print("CUENTA REGRESIVA DE EVENTO")
  dia = int(input("Día: "))
  mes = int(input("Mes: "))
  año = int(input("Año: "))
  dias_hasta_evento = countdown_event(dia, mes, año)

  if dias_hasta_evento > 0:
    print(f"Faltan {dias_hasta_evento} días")
  elif dias_hasta_evento < 0:
    print(f"😭😭😭😭😭😭😭 ¡Te lo perdiste por {abs(dias_hasta_evento)} días!")
  else:
    print("🥳🥳🥳🥳🥳🥳🥳 ¡Hoy es el día!")



'''