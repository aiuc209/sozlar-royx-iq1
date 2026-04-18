sozlar = ["olma", "anor", "shaftoli", "apelsin", "banan", "mandarin"]
uzunliklar = [len(soz) for soz in sozlar]
natija = []
for i in range(len(uzunliklar)):
    if uzunliklar[i] <= 3:
        natija.append("Qisqa")
    elif 3 < uzunliklar[i] <= 6:
        natija.append("O‘rta")
    else:
        natija.append("Uzun")
for i in range(len(sozlar)):
    print(f"So'z: {sozlar[i]}, Uzunligi: {uzunliklar[i]}, Tur: {natija[i]}")
