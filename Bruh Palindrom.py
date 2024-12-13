def palindrom(a):
    if len(a)<=1:
        return True
    else :
        if a[0]!=a[-1]:
            return False
    return palindrom(a[1:-1])

vvod=input()
if palindrom(vvod) == True: print("Palindrom")
else : print("No palindrom :(")