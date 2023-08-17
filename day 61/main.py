from replit import db
import datetime, os, time

def agregarTweet():
  tweet = input("🐥 > ")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key] = tweet
  time.sleep(1)
  os.system("clear")

def verTweet():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.3)
    counter+=1
    if(counter%10==0):
      carryOn = input("Siguiente 10?: ")
      if(carryOn.lower()=="no"):
        break
  time.sleep(1)
  os.system("clear")


while True:
  print("Twitter")
  menu = input("1: Agregar un Tweet\n2: Ver Tweets\n> ")
  if menu == "1":
    agregarTweet()
  else:
    verTweet()

# No entendí bien el metodo de definir la clase con atributos de DB a lo de replit con sus funciones predeterminadas. Pero asumo que es porque sí, sin cuestionar.

    '''
    import datetime
import os
import time

class TwitterApp:
    def __init__(self):
        self.db = {}
        self.load_data()

    def load_data(self):
        # Load data from a persistent storage (e.g., a database)
        # Replace this with your own method of loading data
        pass

    def save_data(self):
        # Save data to a persistent storage (e.g., a database)
        # Replace this with your own method of saving data
        pass

    def agregar_tweet(self):
        tweet = input("🐥 > ")
        timestamp = datetime.datetime.now()
        key = f"mes{timestamp.strftime('%Y%m%d%H%M%S')}"
        self.db[key] = tweet
        self.save_data()
        time.sleep(1)
        os.system("clear")

    def ver_tweets(self):
        matches = [tweet for key, tweet in self.db.items() if key.startswith("mes")]
        matches.reverse()
        counter = 0
        for i, tweet in enumerate(matches, start=1):
            print(tweet)
            print()
            time.sleep(0.3)
            counter += 1
            if counter % 10 == 0:
                carry_on = input("Siguiente 10? (si/no): ")
                if carry_on.lower() == "no":
                    break
        time.sleep(1)
        os.system("clear")

    def run(self):
        while True:
            print("Twitter")
            menu = input("1: Agregar un Tweet\n2: Ver Tweets\n3: Salir\n> ")
            if menu == "1":
                self.agregar_tweet()
            elif menu == "2":
                self.ver_tweets()
            elif menu == "3":
                break
            else:
                print("Opción inválida. Por favor, elija nuevamente.")

if __name__ == "__main__":
    app = TwitterApp()
    app.run()

    '''