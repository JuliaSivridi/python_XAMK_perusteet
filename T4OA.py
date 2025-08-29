def tarkastaPostinumero(merkkijono):
    if not isinstance(merkkijono, str):
        return False
    return len(merkkijono) == 5 and merkkijono.isdigit()

testlist = ["50100", "00100", "123456", "K54-92", "8454", "1.223"]
for el in testlist:
    print(f"{el} - {tarkastaPostinumero(el)}")
