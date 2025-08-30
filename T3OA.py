def laskePintaAla(pituus, leveys, muoto):
    pinta_ala = pituus * leveys
    if muoto == 2:
        return pinta_ala / 100
    elif muoto == 3:
        return pinta_ala / 10000
    else:
        return pinta_ala

p = float(input("Anna tontin pituus (m): "))
l = float(input("Anna tontin leveys (m): "))
m = int(input("Anna muoto (1 - neliömetrit, 2 - aarit, 3 - hehtaarit): "))

if p > 0 and l > 0 and m in [1, 2, 3]:
    pinta_ala = laskePintaAla(p, l, m)
    match m:
        case 1:
            muototexti = "neliömetriä"
        case 2:
            muototexti = "aaria"
        case 3:
            muototexti = "hehtaaria"
    print(f"Tontin pinta-ala on {pinta_ala:.2f} {muototexti}")
