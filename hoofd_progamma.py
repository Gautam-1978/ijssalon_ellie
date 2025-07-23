from helper import onderstreep

# Genereer de onderstreepte koptekst
uitvoer = onderstreep("AANBIEDING")

# Voeg de productregels toe
uitvoer.append("Aardbeienijs, emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")

# Print een lege regel voor visuele ruimte
print()

# Print elke regel uit de lijst
for el in uitvoer:
    print(el)
