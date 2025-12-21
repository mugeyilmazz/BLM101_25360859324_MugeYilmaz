

#Kullanıcıdan bilgiler alınır.
ad = input("Adınız nedir? ")
bolum = input("Bölümünüz nedir? ")
dersler = input("Aldığınız dersleri virgülle ayırarak yazınız: ")
biyografi = input("Kısa biyografinizi yazınız: ")


ders_listesi = dersler.split(",")

#HTML sayfasını hazırlar.
html_icerik = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Kişisel Web Sayfam</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            padding: 20px;
        }}
        h1 {{
            color: #2c3e50;
        }}
        h2 {{
            color: #34495e;
        }}
        ul {{
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
        }}
    </style>
</head>
<body>

    <h1>{ad}</h1>
    <h2>{bolum}</h2>

    <h3>Aldığım Dersler</h3>
    <ul>
"""

#Dersleri HTML listesine ekler.
for ders in ders_listesi:
    html_icerik += f"<li>{ders.strip()}</li>"


html_icerik += f"""
    </ul>

    <h3>Hakkımda</h3>
    <p>{biyografi}</p>

</body>
</html>
"""

#HTML dosyasını yazar.
with open("index.html", "w", encoding="utf-8") as dosya:
    dosya.write(html_icerik)

print("index.html dosyası başarıyla oluşturuldu!")
