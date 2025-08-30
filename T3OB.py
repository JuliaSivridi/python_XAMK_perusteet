class Valuutta:
    def __init__(self, valuuttakurssit):
        self.valuuttakurssit = valuuttakurssit

    def haeKurssi(self, koodi):
        return self.valuuttakurssit[koodi]

    def muunna(self, eurot, koodi):
        return eurot * self.valuuttakurssit[koodi]

valuuttakurssit = {"USD": 1.17, "GBP": 0.87, "SEK": 11.06, "NOK": 11.75, "JPY": 171.85}

valuuttalaskuri = Valuutta(valuuttakurssit)

print(f"1 EUR = {valuuttalaskuri.haeKurssi("USD")} USD")
print(f"200 EUR = {valuuttalaskuri.muunna(200, "USD")} USD")

print(f"1 EUR = {valuuttalaskuri.haeKurssi("GBP")} GBP")
print(f"123 EUR = {valuuttalaskuri.muunna(123, "GBP")} GBP")

print(f"300 EUR = {valuuttalaskuri.muunna(300, "SEK")} SEK")
print(f"400 EUR = {valuuttalaskuri.muunna(400, "NOK")} NOK")
print(f"50 EUR = {valuuttalaskuri.muunna(50, "JPY")} JPY")
