# Zadanie 5

a = int(input("Podaj długość boku a: "))
b = int(input("Podaj długość boku b: "))
c = int(input("Podaj długość boku c: "))
if a > 0 and b > 0 and c > 0:
    if a+b>c and b+c>a and a+c>b:
        print("Można zbudować trójkąt")
    else:
        print("Nie można zbudować trójkąta")
else:
    print("Trójkąt nie może mieć ujemnych długości boków")