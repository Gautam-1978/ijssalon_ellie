# presentatie.py

def presenteer(dictionary, totaal):
    for sleutel, waarde in dictionary.items():        # Loop door elk product en bedrag
        print(f"{sleutel} : {waarde} euro")           # Print het product en de prijs

    print("=" * 25)                                    # Print een onderstreep van 27 = tekens
    print(f"Totaal : {totaal} euro")                  # Print het totaalbedrag
