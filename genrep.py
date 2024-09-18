#Author: Björn Rönnberg
#Date: 2024-09-18

def ser_utr(resistorvarden):
    summa = 0
    antal_resistorer = len(resistorvarden)
    for rakna in range(antal_resistorer):
        resultat = int(resistorvarden[rakna]) + summa
        summa = resultat
    return resultat

def par_utr(resistorvarden):
    delsumma = 0
    antal_resistorer = len(resistorvarden)
    for rakna in range(antal_resistorer):
        delresultat = (1 / int(resistorvarden[rakna])) + delsumma
        delsumma = delresultat
    slutresultat = (1 / delresultat)
    return slutresultat

print('Hej och välkommen till resistorprogrammet!')

resistanser = input('Vänligen ange resistorvärden: ').split()

if resistanser == []:
    print(f'Serieresistans    : 0 Ω\nParallellresistans: 0 Ω\nTack för denna gång!')
else:
    print(f'Serieresistans    : {ser_utr(resistanser)} Ω\nParallellresistans: {par_utr(resistanser)} Ω\nTack för denna gång!')
