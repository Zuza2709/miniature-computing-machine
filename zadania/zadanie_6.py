# Zadanie 6

import time
print("Dzień dobry, to jest prosty kalkulator")
time.sleep(2)
dzialanie = input("Jakie działanie chcesz wykonać? (Wpisz odpowiedni znak) + - * / ")
if dzialanie == "+" or "-" or "*" or "/":
    pierwszaLiczba = int(input("Podaj pierwszą liczbę: "))
    drugaLiczba = int(input("Podaj drugą liczbę: "))
    if dzialanie == "+":
        print(pierwszaLiczba+drugaLiczba)
    elif dzialanie == "-":
        print(pierwszaLiczba-drugaLiczba)
    elif dzialanie == "*":
        print(pierwszaLiczba*drugaLiczba)
    elif dzialanie == "/":
        if drugaLiczba == 0:
            print("Nie można dzielić przez 0 (chyba że mówimy o sferze Riemanna)")
        print(pierwszaLiczba/drugaLiczba)
else:
    print("Nie zrozumiałem, jakie działanie chcesz wykonać")