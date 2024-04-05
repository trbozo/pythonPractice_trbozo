# package Gun20;
#
# public class _08_JavaMethod {
#     public static void main(String[] args) {
#         System.out.println("Merhaba Dünya");
#         System.out.println("Merhaba Dünya");
#
#         merhabaYaz();  // veri almıyor, veri döndürmüyor
#         toplamYaz(4,5); // veri alıyor, veri döndürmüyor
#         enbuyukYaz(4,5); // veri alıyor, veri döndürmüyor
#
#         int enb=Math.max(4,5); // veri alıyor, veri döndürüyor
#
#         int enb2=enBuyukVer(4,5); // veri alsın, veri döndürsün
#         System.out.println(enb2);
#     }
#
#     public static int enBuyukVer(int s1, int s2){ // static den sonra dönenin tipi yazılır
#         int enBuyuk=0;
#
#         if (s1>s2)
#             enBuyuk=s1;
#         else
#             enBuyuk=s2;
#
#         return enBuyuk;
#     }
#
#     public static void merhabaYaz(){ // void : return yok, veri döndürmüyor
#         System.out.println("Merhaba Dünya");
#     }
#
#     public static void toplamYaz(int s1, int s2){
#         System.out.println("Toplam="+ (s1+s2));
#     }
#
#     public static void enbuyukYaz(int s1, int s2){
#         if (s1 > s2)
#             System.out.println(s1+" büyük");
#         else
#             System.out.println(s2+" büyük");
#     }
# }


def en_buyuk_ver(s1, s2):
    # İki sayıdan en büyüğünü döndürür
    return max(s1, s2)

def merhaba_yaz():
    # "Merhaba Dünya" mesajını yazdırır
    print("Merhaba Dünya")

def toplam_yaz(s1, s2):
    # İki sayının toplamını yazdırır
    print("Toplam =", s1 + s2)

def en_buyuk_yaz(s1, s2):
    # İki sayıdan en büyüğünü yazdırır
    if s1 > s2:
        print(f"{s1} büyük")
    else:
        print(f"{s2} büyük")

def main():
    # Fonksiyonların kullanımı
    print("Merhaba Dünya")
    print("Merhaba Dünya")

    merhaba_yaz()  # Veri almıyor, veri döndürmüyor
    toplam_yaz(4, 5)  # Veri alıyor, veri döndürmüyor
    en_buyuk_yaz(4, 5)  # Veri alıyor, veri döndürmüyor

    enb = max(4, 5)  # Veri alıyor, veri döndürüyor
    enb2 = en_buyuk_ver(4, 5)  # Veri alıyor, veri döndürüyor
    print(enb2)

if __name__ == "__main__":
    main()
