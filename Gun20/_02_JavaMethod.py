# package Gun20;
#
# public class _02_JavaMethod {
#     public static void main(String[] args) {
#
#         double rastgeleSayi= Math.random();  // veri almayan, ama geriye veri döndürüyor
#         int max = Math.max(5,6);   // veri alıyor, geriye veri döndürüyor
#         System.out.println(); // veri almıyor, geriye veri de döndürmüyor
#
#         System.out.println("Merhaba Dünya"); // veri alıyor, geriye dönüş yok
#         System.out.println("Merhaba Dünya");
#         System.out.println("Merhaba Dünya");
#
#         merhabaYaz();//veri almıyor, geri bir şey göndermiyor
#         merhabaYaz();
#         merhabaYaz();
#     }
#
#     public static void merhabaYaz(){
#         System.out.println("Merhaba Dünya_metod");
#     }
#
# }


import math
import random

def merhaba_yaz():
    print("Merhaba Dünya_metod")

def main():
    rastgele_sayi = random.random()  # Veri almayan, ama geriye veri döndüren Python fonksiyonu
    max_deger = max(5, 6)  # Veri alıp, geriye veri döndüren Python fonksiyonu
    print()  # Veri almıyor, geriye veri de döndürmüyor

    # "Merhaba Dünya" yazdırma işlemi
    print("Merhaba Dünya")  # Veri alıyor, geri dönüş yok
    print("Merhaba Dünya")
    print("Merhaba Dünya")

    # 'merhaba_yaz' fonksiyonunu çağırma
    merhaba_yaz()  # Veri almıyor, geri bir şey göndermiyor
    merhaba_yaz()
    merhaba_yaz()

if __name__ == "__main__":
    main()


#Python'da fonksiyonlar def anahtar kelimesi kullanılarak tanımlanır ve fonksiyonun gövdesi, işlenecek kod bloklarını içerir.
# main() fonksiyonu, programın ana giriş noktası olarak işlev görür ve diğer fonksiyonları çağırır.
# Bu yapı sayesinde, kodun daha modüler ve yeniden kullanılabilir olması sağlanır.

#Bu örnekte random.random() ve max() fonksiyonları, Java'daki Math.random() ve Math.max() metodlarının
# Python'daki karşılıkları olarak kullanılmıştır. print() fonksiyonu, hem Java'da hem de Python'da aynı amaçla kullanılır
# ve ekrana çıktı yazdırır.