from datetime import date

def milloinPukkiTulee():
    vuosi = date.today().year
    jouluaatto = date(vuosi, 12, 24)
    tanaan = date.today()
    paivaa_jaljella = (jouluaatto - tanaan).days

    karkausvuosi = (vuosi % 4 == 0) and (vuosi % 100 != 0 or vuosi % 400 == 0)
    paivaa_vuodessa = 366 if karkausvuosi else 365
    if paivaa_jaljella < 0:
        paivaa_jaljella += paivaa_vuodessa

    if paivaa_jaljella == 0:
        tulos = "Joulupukki tulee tänään!"
    elif paivaa_jaljella == 1:
        tulos = "Joulupukki tulee huomenna"
    else:
        tulos = f"Joulupukki tulee {paivaa_jaljella} päivän kuluttua"
    return tulos

print(milloinPukkiTulee())
