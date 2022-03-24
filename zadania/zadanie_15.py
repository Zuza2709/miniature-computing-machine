import random
mozliweWartosci = ["kamień", "papier", "nożyce"]
wylosowanaWartosc = random.choice(mozliweWartosci)
wartoscUzytkownika = input("kamień, papier czy nożyce? ")
punktyKomputera = 0
punktyUzytkownika = 0
while punktyUzytkownika < 3 and punktyKomputera < 3:
    if wartoscUzytkownika == wylosowanaWartosc:
        print("remis")
    elif wylosowanaWartosc == "kamień":
        if wartoscUzytkownika == "papier":
            print("tę rundę wygrałeś")
            punktyUzytkownika=punktyUzytkownika+1
        elif wartoscUzytkownika == "nożyce":
            print("tę rundę ja wygrałem")
            punktyKomputera=punktyKomputera+1
    elif wylosowanaWartosc == "papier":
        if wartoscUzytkownika == "nożyce":
            print("tę rundę wygrałeś")
            punktyUzytkownika=punktyUzytkownika+1
        elif wartoscUzytkownika == "kamień":
            print("tę rundę ja wygrałem")
            punktyKomputera=punktyKomputera+1
    elif wylosowanaWartosc == "nożyce":
        if wartoscUzytkownika == "kamień":
            print("tę rundę wygrałeś")
            punktyUzytkownika=punktyUzytkownika+1
        elif wartoscUzytkownika == "papier":
            print("tę rundę ja wygrałem")
            punktyKomputera=punktyKomputera+1
    if punktyUzytkownika < 3 and punktyKomputera < 3:
        wylosowanaWartosc = random.choice(mozliweWartosci)
        wartoscUzytkownika = input("kamień, papier czy nożyce? ")
    else:
        break

print("koniec gry")
if punktyUzytkownika == 3:
    print("wygrałeś")
elif punktyKomputera == 3:
    print("ja wygrałem")
