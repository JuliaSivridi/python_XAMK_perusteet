euValtiot = [
    {
        "nimi": "Alankomaat",
        "asukkaita": 17082000,
        "pintaAla": 41543,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Belgia",
        "asukkaita": 11203992,
        "pintaAla": 30528,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Bulgaria",
        "asukkaita": 7245677,
        "pintaAla": 110994,
        "euroalue": False,
        "schengenAlue": False,
    },
    {
        "nimi": "Espanja",
        "asukkaita": 46507760,
        "pintaAla": 504030,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Irlanti",
        "asukkaita": 4604029,
        "pintaAla": 70273,
        "euroalue": True,
        "schengenAlue": False,
    },
    {
        "nimi": "Italia",
        "asukkaita": 61152798,
        "pintaAla": 301338,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Itävalta",
        "asukkaita": 8511000,
        "pintaAla": 83855,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Kreikka",
        "asukkaita": 10992783,
        "pintaAla": 131990,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Kroatia",
        "asukkaita": 4246809,
        "pintaAla": 56594,
        "euroalue": False,
        "schengenAlue": False,
    },
    {
        "nimi": "Kypros",
        "asukkaita": 858000,
        "pintaAla": 9251,
        "euroalue": True,
        "schengenAlue": False,
    },
    {
        "nimi": "Latvia",
        "asukkaita": 2001468,
        "pintaAla": 64589,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Liettua",
        "asukkaita": 2943472,
        "pintaAla": 65200,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Luxemburg",
        "asukkaita": 549680,
        "pintaAla": 2586.4,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Malta",
        "asukkaita": 425384,
        "pintaAla": 316,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Puola",
        "asukkaita": 38018000,
        "pintaAla": 312685,
        "euroalue": False,
        "schengenAlue": True,
    },
    {
        "nimi": "Portugali",
        "asukkaita": 10427301,
        "pintaAla": 92390,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Ranska",
        "asukkaita": 66076909,
        "pintaAla": 674843,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Romania",
        "asukkaita": 19942642,
        "pintaAla": 238391,
        "euroalue": False,
        "schengenAlue": False,
    },
    {
        "nimi": "Ruotsi",
        "asukkaita": 9644864,
        "pintaAla": 449964,
        "euroalue": False,
        "schengenAlue": True,
    },
    {
        "nimi": "Saksa",
        "asukkaita": 80704691,
        "pintaAla": 357021,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Slovakia",
        "asukkaita": 5400598,
        "pintaAla": 49035,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Slovenia",
        "asukkaita": 2061085,
        "pintaAla": 20273,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Suomi",
        "asukkaita": 5451270,
        "pintaAla": 338424,
        "euroalue": True,
        "schengenAlue": True,
    },
    {
        "nimi": "Tanska",
        "asukkaita": 5621607,
        "pintaAla": 43075,
        "euroalue": False,
        "schengenAlue": True,
    },
    {
        "nimi": "Tšekki",
        "asukkaita": 10398697,
        "pintaAla": 78866,
        "euroalue": False,
        "schengenAlue": True,
    },
    {
        "nimi": "Unkari",
        "asukkaita": 9877365,
        "pintaAla": 93030,
        "euroalue": False,
        "schengenAlue": True,
    },
    {
        "nimi": "Viro",
        "asukkaita": 1315819,
        "pintaAla": 45227,
        "euroalue": True,
        "schengenAlue": True,
    },
]

euAsukkaita = []
for x in euValtiot:
    euAsukkaita.append(x["asukkaita"])
euAsukkaita5Suurinta = sorted(euAsukkaita, reverse=True)[0:5]
print("Viisi suurinta EU-jäsenvaltiota asukasluvun mukaan:")
for x in euValtiot:
    if x["asukkaita"] in euAsukkaita5Suurinta:
        print(x["nimi"])
print("Yhteenlaskettu asukasmäärä:", sum(euAsukkaita5Suurinta), "\n")

euroalueAsukkaita = []
for x in euValtiot:
    if x["euroalue"]:
        euroalueAsukkaita.append(x["asukkaita"])
print(f"Euroalueella asuvien prosentuaalinen määrä koko EU:n asukasmäärästä: "
      f"{(sum(euroalueAsukkaita) / sum(euAsukkaita) * 100):.2f}% \n")

euPintaAla = []
schengenPintaAla = []
for x in euValtiot:
    euPintaAla.append(x["pintaAla"])
    if x["schengenAlue"]:
        schengenPintaAla.append(x["pintaAla"])
print(f"Schengen-alueeseen kuuluvien EU-jäsenvaltioiden pinta-alan osuus koko EU:n pinta-alasta: "
      f"{(sum(schengenPintaAla) / sum(euPintaAla)):.2f} \n")

euroalue_ja_schengen = []
for x in euValtiot:
    if x["euroalue"] and x["schengenAlue"]:
        euroalue_ja_schengen.append(x["nimi"])
print(f"Sekä euro- että shengen-alueeseen kuuluvien EU-jäsenvaltioiden "
      f"prosentuaalinen osuus kaikista EU-jäsenvaltioista: "
      f"{(len(euroalue_ja_schengen) / len(euValtiot) * 100):.2f}% \n")
