from random import randint 

while True:
    nunbers = [randint(0,9) for i in range(0,9)]
    set_ = set(nunbers)

    if len(set_) == 1:
        continue
    break

cont = 10
soma = 0

for num in nunbers:
   soma += num * cont
   cont -=1

soma = soma % 11
digit_tem = 0 if soma == 0 or soma == 1 else 11-soma
nunbers.append(digit_tem)

cont = 11
soma = 0 

for num in nunbers:
    soma += num * cont
    cont -=1

soma = soma % 11
digit_eleven = 0 if soma == 0 or soma == 1 else 11-soma
nunbers.append(digit_eleven)

for i in nunbers:
    print(i,end='')