from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False 
  while True:
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : "))
    if stop_playback == 2:
      source.paused = True 
      return 
    else: 
      continue
  
while True:
  os.system("clear")
  print("🎵 MyPOD Reproductor de Música")
  time.sleep(1)
  print("Presiona 1 para Correr")
  time.sleep(1)
  print("Presiona 2 para Salir")
  time.sleep(1)
  print("Presiona cualquier cosa para volver al menú")
  userInput = int(input())
  if userInput == 1:
    print("Andando su música correspondiente!")
    play()
  elif userInput == 2:
    exit()
  else :
    continue