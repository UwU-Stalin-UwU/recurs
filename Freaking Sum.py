def sum(a):
    if len(a)==0 : return 0
    return sum(a[1:])+a[0]

vvod=input()
spis=vvod.split()
for i in range (0, len(spis)):
    spis[i]=int(spis[i])
final=sum(spis)
print(final)