def anna_teksti(arvosana):
    match arvosana:
        case 0:
            return "hylätty"
        case 1 | 2:
            return "tyydyttävä"
        case 3 | 4:
            return "hyvä"
        case 5:
            return "kiitettävä"

def tulosta_arvosana(pisteet, arvosana):
    sana_piste = "piste" if pisteet == 1 else "pistettä"
    print(f"{pisteet} {sana_piste}. Arvosana {arvosana} ({anna_teksti(arvosana)}).")

pisteet = int(input("Anna luku (0-30): "))
if pisteet >=0 and pisteet < 16:
    tulosta_arvosana(pisteet, 0)
elif pisteet >= 16 and pisteet <= 20:
    tulosta_arvosana(pisteet, 1)
elif pisteet >= 21 and pisteet <= 25:
    tulosta_arvosana(pisteet, 2)
elif pisteet >= 26 and pisteet <= 30:
    tulosta_arvosana(pisteet, 3)
elif pisteet >= 31 and pisteet <= 35:
    tulosta_arvosana(pisteet, 4)
elif pisteet >= 36:
    tulosta_arvosana(pisteet, 5)
else:
    print("Virheellinen kokonaisluku")
    quit()
