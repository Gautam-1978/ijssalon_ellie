# Dictionary met de prijzen van verschillende smaken ijs
prijzen = {"aardbei" : 3,      # Prijs van aardbei-ijs is €3
           "vanille" : 4,      # Prijs van vanille-ijs is €4
           "chocolade" : 5     # Prijs van chocolade-ijs is €5
 }

# Berekening van de aanbieding: aardbei-ijs met 20% korting
aanbieding = prijzen["aardbei"] * 0,8 # 3 * 0,8 = 2,40

# Opstellen van een reclamebericht met de aanbieding
reclame_tekst = f"Vandaag in de aanbieding: aarbei-ijs, 1 liter - slechts € {aanbieding}"

# Beperkt de lengte van de tekst tot de eerste 63 tekens
reclame_tekst2 = reclame_tekst[:63]

# Zet de tekst om naar hoofdletters
reclame_tekst3 = reclame_tekst2.upper()



# Loopt door elk woord in de lijst
for el in reclame_tekst3:
    # Controleert of het woord langer is dan 4 tekens
    if len(el) > 4:
        print(el.upper())  # Print het woord in hoofdletters 
    else:
        print(el.lower())  # Print het woord in kleine letters