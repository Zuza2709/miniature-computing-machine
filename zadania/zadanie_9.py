# Zadanie 9

import time
print("Witamy w programie obliczającym współczynnik BMI")
time.sleep(2)
masa = float(input("Podaj masę [kg]: "))
wzrost = float(input("Podaj wzrost [m]: "))
bmi = masa/wzrost**2
if bmi < 20:
    print("Niedowaga")
elif bmi >= 20 and bmi < 25:
    print("Prawidłowa waga")
elif bmi >= 25 and bmi <30:
    print("Nadwaga")
elif bmi > 30:
    print("Otyłość")
