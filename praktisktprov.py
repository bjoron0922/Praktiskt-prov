#Author: Björn Rönnberg
#Date: 2024-09-25

tabeller = input('Vilka tabeller vill du beräkna? ').split()

if tabeller == []:
    pass
else:
#Det kanske ser random ut med alla new lines, men jag vill ha varje ny tabell separerad med två blanka rader för att lätt kunna hitta den man är ute efter när man scrollar igenom, samt en ny rad som skiljer tabell-rubriken från beräkningarna.
    for i in range(len(tabeller)):
        print(f'\n\n{tabeller[i]}:\n')
        for j in range(1, 11):
            print(f'{tabeller[i]} * {j} = {str(j * int(tabeller[i]))}')
