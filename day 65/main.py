class character:
  name = None
  health = 100
  mp = 100

  def __init__(self, name):
    self.name = name

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}")

  def setStats(self, health, mp):
    self.health = health
    self.mp = mp

class player(character):
  nickname = None
  lives = 3

  def __init__(self, nickname):
    self.name = "Player"
    self.nickname = nickname

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tNickname: {self.nickname}\tLives: {self.lives}")

  def isAlive(self):
    if self.lives > 0:
      print(f"{self.nickname} lives on!")
      return True
    else:
      print(f"{self.nickname} has expired!")
      return False

ian = player("Ian the mighty")
ian.print()
print(ian.isAlive())

class enemy(character):
  type = None
  strength = None

  def __init__(self, name, type, strength):
    self.name = name
    self.type = type
    self.strength = strength

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}")

class orc(enemy):
  speed = None

  def __init__(self, speed):
    self.name = "Orc"
    self.type = "Orc"
    self.strength = 200
    self.speed = speed

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tSpeed: {self.speed}")

sharron = orc(250)
gary = orc(205)

sharron.print()
gary.print()

class vampire(enemy):
  day = True

  def __init__(self, day):
    self.name = "Vampire"
    self.type = "Vampire"
    self.strength = 150
    self.day = day

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tDay: {self.day}")

eric = vampire(False)
eric.print()

'''
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.mp = 100

    def mostrar(self):
        print(f"{self.nombre}\tSalud: {self.salud}\tPuntos de magia: {self.mp}")

    def establecer_stats(self, salud, mp):
        self.salud = salud
        self.mp = mp

class Jugador(Personaje):
    def __init__(self, apodo):
        super().__init__("Jugador")
        self.apodo = apodo
        self.vidas = 3

    def mostrar(self):
        print(f"{self.nombre}\tSalud: {self.salud}\tPuntos de magia: {self.mp}\tApodo: {self.apodo}\tVidas: {self.vidas}")

    def esta_vivo(self):
        if self.vidas > 0:
            print(f"¡{self.apodo} sigue vivo!")
            return True
        else:
            print(f"¡{self.apodo} ha expirado!")
            return False

ian = Jugador("Ian el poderoso")
ian.mostrar()
print(ian.esta_vivo())

class Enemigo(Personaje):
    def __init__(self, nombre, tipo, fuerza):
        super().__init__(nombre)
        self.tipo = tipo
        self.fuerza = fuerza

    def mostrar(self):
        print(f"{self.nombre}\tSalud: {self.salud}\tPuntos de magia: {self.mp}\tTipo: {self.tipo}\tFuerza: {self.fuerza}")

class Orco(Enemigo):
    def __init__(self, velocidad):
        super().__init__("Orco", "Orco", 200)
        self.velocidad = velocidad

    def mostrar(self):
        print(f"{self.nombre}\tSalud: {self.salud}\tPuntos de magia: {self.mp}\tTipo: {self.tipo}\tFuerza: {self.fuerza}\tVelocidad: {self.velocidad}")

sharron = Orco(250)
gary = Orco(205)

sharron.mostrar()
gary.mostrar()

class Vampiro(Enemigo):
    def __init__(self, es_de_dia):
        super().__init__("Vampiro", "Vampiro", 150)
        self.es_de_dia = es_de_dia

    def mostrar(self):
        print(f"{self.nombre}\tSalud: {self.salud}\tPuntos de magia: {self.mp}\tTipo: {self.tipo}\tFuerza: {self.fuerza}\tEs de día: {self.es_de_dia}")

eric = Vampiro(False)
eric.mostrar()


'''


'''
class Character:
  name = None
  health = 100
  mp = 100

  def __init__(self, name):
    self.name = name

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}")

  def setStats(self, health, mp):
    self.health = health
    self.mp = mp

class Player(Character):
  nickname = None
  lives = 3

  def __init__(self, nickname):
    super().__init__(nickname)
    self.nickname = nickname

  def print(self):
    super().print()
    print(f"Nickname: {self.nickname}\tLives: {self.lives}")

  def isAlive(self):
    if self.lives > 0:
      print(f"{self.nickname} lives on!")
      return True
    else:
      print(f"{self.nickname} has expired!")
      return False

class Enemy(Character):
  type = None
  strength = None

  def __init__(self, name, type, strength):
    super().__init__(name)
    self.type = type
    self.strength = strength

  def print(self):
    super().print()
    print(f"Type: {self.type}\tStrength: {self.strength}")

class Orc(Enemy):
  speed = None

  def __init__(self, speed):
    super().__init__("Orc", "Orc", 200)
    self.speed = speed

class Vampire(Enemy):
  day = True

  def __init__(self, day):
    super().__init__("Vampire", "Vampire", 150)
    self.day = day

  def print(self):
    super().print()
    print(f"Day: {self.day}")

ian = Player("Ian the mighty")
ian.print()
print(ian.isAlive())

sharron = orc(250)
gary = orc(205)

sharron.print()
gary.print()

eric = vampire(False)
eric.print()

'''