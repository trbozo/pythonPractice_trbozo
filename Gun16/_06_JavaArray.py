# Kullanıcıdan 10 elemanlı bir dizinin değerlerini alıp yazdıran program

# Kullanıcıdan girişleri okumak için Scanner sınıfının Python'daki karşılığı yoktur.
# Bu nedenle, Python'da input() fonksiyonu kullanılabilir.

# Boş bir liste oluşturuyoruz.
dizi = []

# Kullanıcıdan 10 adet değer alıyoruz ve listeye ekliyoruz.
for i in range(10):
    deger = int(input(f"dizinin {i}. elemanı="))
    dizi.append(deger)

# Dizideki elemanları yazdırıyoruz.
for i in range(10):
    print(f"dizi[{i}] = {dizi[i]}")
