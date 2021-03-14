# Zadanie 1
pierwszy = input("Wprowadz nazwe pierwszego przysmaku: ")
drugi = input("Wprowadz nazwe drugiego przysmaku: ")
print("Nowy przysmak: " + pierwszy + drugi)

# ======================================================================================================================
# Zadanie 2
print("\nLicze napiwek")
kwota = float(input("Podaj kwote: "))
print("Napiwek 15%: ", (kwota * 0.15))
print("Napiwek 20%: ", (kwota * 0.20))

# ======================================================================================================================
# Zadanie 3
cena = int(input("\nWprowadz cene samochodu: "))
podatek = cena * 0.23  # procenty
rejestracja = cena * 0.5  # procenty
prowizja = 150
dostarczenie = 100
print("Calkowita cena za samochod: ", (podatek + rejestracja + prowizja + dostarczenie + cena))
