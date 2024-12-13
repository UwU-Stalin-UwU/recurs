def search_max(a):
    if len(a)==0:
        return 0
    return a[0] if a[0]> search_max(a[1:]) else search_max(a[1:])

vvod = input()
spis=vvod.split()
for i in range (0, len(spis)):
    spis[i]=int(spis[i])
print(search_max(spis))