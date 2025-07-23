# boekhouding.py

from helper import *           # Importeer alles uit helper.py
from presentatie import *      # Importeer alles uit presentatie.py
import csv                     # Voor het opslaan in een CSV-bestand

# 1. Maak een dictionary met inkomsten
inkomsten = {
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}

# 2. Bereken het totaal via som()
totaal_inkomsten = som(inkomsten)

# 3. Print het netjes via presenteer()
presenteer(inkomsten, totaal_inkomsten)

# 4. Sla de info op in een CSV-bestand
with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')   # Schrijver voor CSV met ; als scheiding
    for naam, bedrag in inkomsten.items():        # Loop door alle producten en bedragen
        writer.writerow([naam, bedrag])           # Schrijf elk product en bedrag op een rij
