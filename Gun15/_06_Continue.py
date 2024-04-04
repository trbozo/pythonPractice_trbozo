# Girilen bir stringin harflerini teker teker
# ekrana alt alta olacak şekilde yazdırınız, boşlukları yazmasın.

cumle = input("Bir cümle giriniz: ")

for harf in cumle:
    if harf == ' ':
        continue  # bir sonraki adıma geç
                  # boşlukları yazdırmaz
    print("harf =", harf)


# Dil Sözdizimi: Python'da kod blokları girinti kullanılarak belirtilirken, Java'da {} kullanılır.
# Döngü İfadesi: Python'da for harf in cumle: şeklinde döngü ifadesi kullanılırken, Java'da for(int i=0; i < cumle.length(); i++) şeklinde kullanılır.
# Kullanıcı Girişi Alma: Java'da kullanıcı girişi alma işlemi Scanner sınıfıyla yapılırken, Python'da input() fonksiyonu kullanılır.
# String Karakterlerini Almak: Python'da string karakterlerine doğrudan erişim sağlanabilirken, Java'da charAt() metodu kullanılır.
# Continue İfadesi: Python'da continue ifadesiyle döngüde bir sonraki adıma geçilirken, Java'da da aynı şekilde kullanılır.