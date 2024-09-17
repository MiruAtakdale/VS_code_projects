import random
moznosti = ['kamen', 'nuzky', 'papir']
hrac = 'kamen'
pocitac = random.choice(moznosti)

print('Hráč:',hrac)
print('Počítač:', pocitac)

if hrac == 'kamen' and pocitac == 'nuzky':
    print("Vyhrál jsi!")

elif hrac == 'kamen' and pocitac == 'papir':
    print("Prohrál jsi!")
else: 
    print("Nerozhodně!")