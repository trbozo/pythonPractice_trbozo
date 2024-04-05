# package Gun20;
#
# public class _04_JavaMethod {
#     public static void main(String[] args) {
#         // bir sayının tek mi çift mi olduğunu yazdırınız.
#         int sayi=55;
#
#         // 1.Yöntem
#         if (sayi%2 == 0)
#             System.out.println("Çift");
#         else
#             System.out.println("Tek");
#
#         //2.Yöntem
#         tekMiCiftMiYaz(60);
#         tekMiCiftMiYaz(55);
#         tekMiCiftMiYaz(46);
#     }
#
#     public static void tekMiCiftMiYaz(int sayi){
#         if (sayi%2 == 0)
#             System.out.println(sayi+" : Çift");
#         else
#             System.out.println(sayi+" : Tek");
#     }
# }


def tek_mi_cift_mi_yaz(sayi):
    if sayi % 2 == 0:
        print(f"{sayi} : Çift")
    else:
        print(f"{sayi} : Tek")

def main():
    # Bir sayının tek mi çift mi olduğunu yazdırınız.
    sayi = 55

    # 1.Yöntem
    if sayi % 2 == 0:
        print("Çift")
    else:
        print("Tek")

    # 2.Yöntem
    tek_mi_cift_mi_yaz(60)
    tek_mi_cift_mi_yaz(55)
    tek_mi_cift_mi_yaz(46)

if __name__ == "__main__":
    main()

#Python'da if __name__ == "__main__": ifadesi, bir Python dosyasının doğrudan çalıştırılıp çalıştırılmadığını kontrol eder.
# Bu, özellikle Python dosyalarını hem bağımsız bir script olarak çalıştırmak hem de başka bir dosyadan modül olarak içe aktarmak
# için kullanışlıdır.

#__name__ bir Python dosyasının içinde özel bir değişkendir. Bir dosya doğrudan çalıştırıldığında,
# Python yorumlayıcısı bu dosyanın __name__ değişkenini "__main__" olarak ayarlar.
#Eğer dosya başka bir Python dosyasından import edilirse (yani bir modül olarak kullanılırsa),
# __name__ değişkeni o dosyanın adı (uzantısız) olur.
#Bu yapıyı kullanarak, bazı kod bloklarının sadece dosya doğrudan çalıştırıldığında çalışmasını sağlayabilirsiniz,
# ancak dosya bir modül olarak import edildiğinde bu bloklar çalışmaz.
# Bu, genellikle bir Python dosyasının testlerini yazarken veya bir script'in ana fonksiyonunu tanımlarken kullanılır.


#Bu kod, öncelikle bir sayının tek veya çift olup olmadığını kontrol eden tek_mi_cift_mi_yaz(sayi) fonksiyonunu tanımlar.
# Ardından, main() fonksiyonu içinde hem doğrudan kontrol yaparak hem de tek_mi_cift_mi_yaz(sayi) fonksiyonunu çağırarak
# farklı sayılar için tek mi çift mi olduklarını ekrana yazdırır. Python'da fonksiyonlar def anahtar kelimesiyle tanımlanır
# ve fonksiyonlara parametre olarak verilen değerler üzerinde işlemler gerçekleştirilebilir.
# main() fonksiyonu, programın ana giriş noktası olarak işlev görür.