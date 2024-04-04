# Kullanıcıdan x girilene kadar ekrana "Program çalışıyor" yazan
# ve x girildiğinde ise "Program bitti" yazan programı yazınız.

# Döngünün içerisinde neler olacak?
# Okuma işlemi var, eğer x'den farklı ise yazma işlemi var
# Şart: Girilen x'den farklı olduğu sürece dönecek

girilen = ""

while girilen.lower() != "x":
    girilen = input("ifade giriniz=")

    if girilen.lower() != "x":
        print("program çalışıyor")

print("program bitti")
