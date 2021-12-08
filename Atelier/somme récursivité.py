def somme(n):
    if n<=0:
        return 0
    else:
        return ( n+somme(n-1))
    nombre=int(input("entrer un nombre:"))
    print("la somme de",nombre,"est",somme(nombre))