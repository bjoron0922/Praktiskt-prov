#Author: Björn Rönnberg
#Date: 2024-09-25

tabeller = input('Vilka tabeller vill du beräkna? ').split()

if tabeller == []:
    pass
else:
    for i in range(len(tabeller)):
        print(f'\n{tabeller[i]}:\n')
        for j in range(1, 11):
            print(f'{tabeller[i]} * {j} = {str(j * int(tabeller[i]))}')
        print()
