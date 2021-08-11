cadena = 'Geringoso'
capadepenapa = ''
for letra in cadena:
    capadepenapa += letra
    print(capadepenapa)
    if letra == 'a':
        capadepenapa+='pa'
    if letra == 'e':
        capadepenapa+='pe'
    if letra == 'i':
        capadepenapa+='pi'
    if letra == 'o':
        capadepenapa+='po'
    if letra == 'u':
        capadepenapa+='pu'


print(capadepenapa)