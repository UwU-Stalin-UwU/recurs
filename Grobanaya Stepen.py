def stepen(a, b):
    if b==0:
        return 1
    return stepen(a, b-1)*a

chislo=input()
step=input() 
chislo=int(chislo)
step=int(step)
final = stepen(chislo, step)
print(final)