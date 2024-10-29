def dosyaOku(dosyaAdi):
    with open(dosyaAdi, "r", encoding="utf-8") as dosya:
        return dosya.read().strip()

def karakterKoordinatlariniBul(dosya1Icerigi, dosya2Icerigi):
    dosya1Koordinatlari = {}
    dosya2Koordinatlari = {}

    for indeks, karakter in enumerate(dosya1Icerigi):
        if karakter not in dosya1Koordinatlari:
            dosya1Koordinatlari[karakter] = []  
        dosya1Koordinatlari[karakter].append(indeks)

    for indeks, karakter in enumerate(dosya2Icerigi):
        if karakter not in dosya2Koordinatlari:
            dosya2Koordinatlari[karakter] = []  
        dosya2Koordinatlari[karakter].append(indeks)

    ortakKoordinatlar = {}
    for karakter in dosya1Koordinatlari:
        if karakter in dosya2Koordinatlari:
            ortakKoordinatlar[karakter] = {
                "dosya1 Koordinatlari": dosya1Koordinatlari[karakter],
                "dosya2 Koordinatlari": dosya2Koordinatlari[karakter]
            }
    return ortakKoordinatlar

def anaFonksiyon():
    dosya1 = "Dosya1.txt"
    dosya2 = "Dosya2.txt"
    dosya1Icerigi = dosyaOku(dosya1)
    dosya2Icerigi = dosyaOku(dosya2)
    ortakKoordinatlar = karakterKoordinatlariniBul(dosya1Icerigi, dosya2Icerigi)

    if ortakKoordinatlar:
        print("Ortak Koordinatlar")
        for karakter, koordinat in ortakKoordinatlar.items():
            print("Karakter:", karakter)
            print(f"Dosya1 Konumları: {koordinat['dosya1 Koordinatlari']}")
            print(f"Dosya2 Konumları: {koordinat['dosya2 Koordinatlari']}")

if __name__ == "__main__":
    anaFonksiyon()
