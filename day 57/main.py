def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
    
print(factorial(500))


'''
def factorial(number):
    if number == 0:
        return 1
    else:
        factorials = [1]
        for i in range(1, number + 1):
            factorials.append(factorials[-1] * i)
        return factorials[-1]

print(factorial(500))

'''