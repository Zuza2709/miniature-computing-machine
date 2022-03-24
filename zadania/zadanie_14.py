import random
wylosowaneLiczby = []
liczbyUzytkownika = []
for i in range (6):
    a=random.randint(1,50)
    wylosowaneLiczby.append(a)
    b=int(input(f"Podaj liczbę {i+1} z 6: "))
    while b>50 or b<1:
        print("Podaj liczbę z zakresu od 1 do 50.")
        b=int(input(f"Podaj liczbę {i+1} z 6: "))
    liczbyUzytkownika.append(b)
    
print("Wylosowane liczby: ")
print(*wylosowaneLiczby, sep=', ')
print("Twoje liczby: ")
print(*liczbyUzytkownika, sep=', ')

trafione=set(wylosowaneLiczby)&set(liczbyUzytkownika)

if len(trafione)>0:
    print(f"Trafiłeś {len(trafione)} z 6 liczb. Czyli: {trafione}")
else:
    print("Nie trafiłeś żadnej liczby.")