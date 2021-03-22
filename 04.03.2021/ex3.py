cena = int(input("\nWprowadz cene samochodu: "))
podatek = cena * 0.23  # procenty
rejestracja = cena * 0.5  # procenty
prowizja = 150
dostarczenie = 100
print("Calkowita cena za samochod: ", (podatek + rejestracja + prowizja + dostarczenie + cena))