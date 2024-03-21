# // int toplam=6700;
# // byte sayi=5;
toplam = 6700
sayi = 5

# // sayi=(byte)toplam;
sayi = int(toplam % 256 - 128)  # Python'da byte değeri hesaplamak için
print("sayi =", sayi)

# // double oran=3.7;
# // toplam = (int)oran;
oran = 3.7
toplam = int(oran)
print("toplam =", toplam)
