import math

ctto = float(input("Comprimento do cateto oposto: "))
ctta = float(input("Comprimento do cateto adjacente: "))
hipt = math.sqrt(math.pow(ctto, 2) + math.pow(ctta, 2))
print(f"a hipotenusa vai medir: {hipt}")
