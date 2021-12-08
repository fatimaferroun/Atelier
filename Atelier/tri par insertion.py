def tri_insertion(tab):
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k
tab = [98, 22, 15, 32, 2, 74, 63, 70]
tri_insertion(tab)
print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("% d" % tab[i])