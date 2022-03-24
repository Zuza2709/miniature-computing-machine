import time
import random
wylosowanaLiczba = str(random.randint(1, 20))
print("Wylosowałem dla ciebie liczbę od 1 do 20.")
time.sleep(1)
print(wylosowanaLiczba)
odpowiedziUzytkownika = []
odpowiedzUzytkownika = input("Zgadnij jaka to liczba ")
odpowiedziUzytkownika.append(odpowiedzUzytkownika)
if odpowiedzUzytkownika == wylosowanaLiczba:
    print("Trafiłeś za 1 razem")
else:
    while odpowiedzUzytkownika != wylosowanaLiczba:
        odpowiedziUzytkownika.append(odpowiedzUzytkownika)
        print("Spróbuj jeszcze raz")
        odpowiedzUzytkownika = input("Zgadnij jaka to liczba ")
        if odpowiedzUzytkownika == wylosowanaLiczba:
            print(f"Trafiłeś za {len(odpowiedziUzytkownika)} razem")