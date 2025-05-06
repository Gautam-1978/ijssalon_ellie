prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}
# Stap 2: Variabele 'aanbieding' berekenen
aanbieding = prijzen["aardbei"] * 0.8

# Stap 3: Formatteer de reclame-tekst
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter slechts € {aanbieding}"

print(reclame_tekst)  # Eerste print-opdracht
reclame_tekst2 = reclame_tekst[:reclame_tekst.index('0')]

print(reclame_tekst2)
reclame_tekst3 = reclame_tekst2.upper()

print(reclame_tekst3)
reclame_tekst4 = reclame_tekst3.split()

print(reclame_tekst4)

for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())