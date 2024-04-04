# Girilen 2 tam sayıyı kullanıcıdan aldıktan sonra,
# Toplama için T, Çıkarma için Ç, çarpma için P, bölme için B
# harflerini yine kullanıcıdan alarak isteğe uygun olan
# işlemi yaptırıp sonucu yazdırınız.

sayi1 = int(input("1.Sayı = "))
sayi2 = int(input("2.Sayı = "))

print("Toplama için T")
print("Çıkarma için Ç")
print("Çarpma için P")
print("Bölme için B")
seciminiz = input("Seçiminiz= ").upper()  # T,Ç,P,B

if seciminiz == "T":
    print("Toplam =", sayi1 + sayi2)
elif seciminiz == "Ç":
    print("Çıkarma =", sayi1 - sayi2)
elif seciminiz == "P":
    print("Çarpma =", sayi1 * sayi2)
elif seciminiz == "B":
    print("Bölme =", sayi1 / sayi2)
