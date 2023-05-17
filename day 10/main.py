mySpend = float(input("How much did you spend?: "))
tipPercentage = float(input("What percentage do you want to tip? "))/100
numberOfPeople = int(input("How many people in your group? "))
answer = (mySpend / numberOfPeople) / tipPercentage
answer = round(answer, 2)
print("You each owe", answer)





#myBill = float(input("Whatwas the bill?: "))
#numberOfPeople = int(input("How many people?: "))
#answer = myBill / numberOfPeople
#answer = round(answer, 2)
#print("You all owe", answer)
