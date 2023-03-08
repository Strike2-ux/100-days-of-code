print("Generator Identifier")

YofB = int(input("Wich year were you born?"))
if YofB < 1883:
    print("You're lying, be honest")
elif YofB <= 1904 and YofB >= 1883:
    print("You are a Lost generation")
elif YofB <= 1927 and YofB >= 1901:
    print("Your are from the greatest generation")
elif YofB <= 1945 and YofB >= 1928:
    print("Silent generation, you are, my respects")
elif YofB <= 1964 and YofB >= 1946:
    print("Baby Boomers, Respect to, alot of knowledge")
elif YofB <= 1980 and YofB >= 1965:
    print("Generation X, Evolution")
elif YofB <= 1996 and YofB >= 1981:
    print("Generation Z, Bruh, ramen and egg?")
elif YofB <= 2012 and YofB >= 1997:
    print("Generation Alpha, Lets keep evolving")
else:
    print("Please enter a real value in the generetor idendifier por favor, s'il vous plaît") 