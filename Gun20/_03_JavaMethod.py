# package Gun20;
#
# public class _03_JavaMethod {
#
#     public static void main(String[] args) {
#          merhabaYaz();  // veri almayan, veri döndürmeyen
#          merhabaYaz();
#
#          merhabaYazIsme("ismet"); //veri alıyor, veri döndürmüyor
#          merhabaYazCok(5);//veri alıyor, veri döndürmüyor
#     }
#
#     public static void merhabaYaz(){
#         System.out.println("Merhaba Dünya");
#     }
#
#     public static void merhabaYazIsme(String ad){
#         System.out.println("Merhaba "+ad);
#     }
#
#     public static void merhabaYazCok(int miktar){ // başla
#         for (int i = 0; i < miktar; i++) {
#             System.out.println("Merhaba");
#         }
#     }//dur
#
# }


def merhaba_yaz():
    print("Merhaba Dünya")

def merhaba_yaz_isme(ad):
    print(f"Merhaba {ad}")

def merhaba_yaz_cok(miktar):
    for i in range(miktar):
        print("Merhaba")

def main():
    merhaba_yaz()  # Veri almayan, veri döndürmeyen
    merhaba_yaz()

    merhaba_yaz_isme("ismet")  # Veri alıyor, veri döndürmüyor
    merhaba_yaz_cok(5)  # Veri alıyor, veri döndürmüyor

if __name__ == "__main__":
    main()


##Python'da def anahtar kelimesiyle fonksiyon tanımlamanın nasıl yapıldığını gösterir.
# Fonksiyonlar, belirli bir işlemi gerçekleştiren, adlandırılmış kod bloklarıdır.
# merhaba_yaz() fonksiyonu hiçbir parametre almaz ve sadece "Merhaba Dünya" mesajını yazdırır.
# merhaba_yaz_isme(ad) fonksiyonu bir ad alır ve bu adı mesajda kullanır. merhaba_yaz_cok(miktar) fonksiyonu,
# verilen miktar kadar "Merhaba" mesajını yazdırır. main() fonksiyonu ise,
# programın giriş noktasıdır ve diğer fonksiyonları uygun sırayla çağırır.
# Bu yapı, kodun modüler ve okunabilir olmasını sağlar.