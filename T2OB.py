arvosanat = [
    {
        "opiskelijanumero" : "1111",
        "kurssikoodi": "100",
        "arvosana": 4
    },
    {
        "opiskelijanumero" : "2222",
        "kurssikoodi": "100",
        "arvosana": 3
    },
    {
        "opiskelijanumero" : "1111",
        "kurssikoodi": "200",
        "arvosana": 5
    },
    {
        "opiskelijanumero" : "1111",
        "kurssikoodi": "300",
        "arvosana": 3
    },
    {
        "opiskelijanumero" : "2222",
        "kurssikoodi": "300",
        "arvosana": 1
    }
]

opiskelijanro = "1111"

def laske_keskiarvon(arvosanat, opiskelijanro):
    sum = num = 0
    for a in arvosanat:
        if a["opiskelijanumero"] == opiskelijanro:
            sum += a["arvosana"]
            num += 1
    return sum / num if num > 0 else 0

print(f"Opiskelijan {opiskelijanro} keskiarvo: {laske_keskiarvon(arvosanat, opiskelijanro)}")

print("Lisätään uusi arvosana")
arvosanat.append({
    "opiskelijanumero": "1111",
    "kurssikoodi": "400",
    "arvosana": 2
})

print(f"Opiskelijan {opiskelijanro} keskiarvo: {laske_keskiarvon(arvosanat, opiskelijanro)}")
