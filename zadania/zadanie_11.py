# Zadanie 11

x = int(input("Podaj współrzędną x: "))
y = int(input("Podaj współrzędną y: "))

if x == 0 and y == 0:
    print(f"Punkt ({x}, {y}) jest początkiem układu współrzędnych")
elif x == 0:
    print(f"Punkt ({x}, {y}) znajduje się na osi OX")
elif y == 0:
    print(f"Punkt ({x}, {y}) znajduje się na osi OY")
elif x > 0 and y > 0:
    print(f"Punkt ({x}, {y}) znajduje się w I ćwiartce układu współrzędnych")
elif x < 0 and y > 0:
    print(f"Punkt ({x}, {y}) znajduje się w II ćwiartce układu współrzędnych")
elif x < 0 and y < 0:
    print(f"Punkt ({x}, {y}) znajduje się w III ćwiartce układu współrzędnych")
elif x > 0 and y < 0:
    print(f"Punkt ({x}, {y}) znajduje się w IV ćwiartce układu współrzędnych")
