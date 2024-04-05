# package Gun20;
#
# import java.util.Scanner;
#
# public class _05_JavaMethod {
#     public static void main(String[] args) {
#         // girilen 2 sayıdan büyük olanını yazdırınız.
#
#         enBuyukYaz();  // hem okuyacak, hem de yazacak
#         enBuyukYaz();
#
#         enBuyukYaz(56,70); // birden fazla parametre kullanımı
#     }
#
#     public static void enBuyukYaz(int s1, int s2){
#         if (s1>s2)
#             System.out.println(s1+ " büyük");
#         else
#         if (s2>s1)
#             System.out.println(s2+ " büyük");
#         else
#             System.out.println("eşit");
#     }
#
#
#     public static void enBuyukYaz(){
#         Scanner oku=new Scanner(System.in);
#         System.out.print("1.Sayı giriniz=");
#         int s1=oku.nextInt();
#         System.out.print("2.Sayı giriniz=");
#         int s2=oku.nextInt();
#
# //        if (s1>s2)
# //            System.out.println(s1+ " büyük");
# //        else
# //            if (s2>s1)
# //                System.out.println(s2+ " büyük");
# //            else
# //                System.out.println("eşit");
#
#         enBuyukYaz(s1,s2);
#     }
#
#
# }

def en_buyuk_yaz(s1, s2):
    if s1 > s2:
        print(f"{s1} büyük")
    elif s2 > s1:
        print(f"{s2} büyük")
    else:
        print("eşit")

def en_buyuk_yaz_kullanici_girisli():
    s1 = int(input("1. Sayıyı giriniz: "))
    s2 = int(input("2. Sayıyı giriniz: "))
    en_buyuk_yaz(s1, s2)

def main():
    en_buyuk_yaz_kullanici_girisli()  # Hem okuyacak, hem de yazacak
    en_buyuk_yaz_kullanici_girisli()

    en_buyuk_yaz(56, 70)  # Birden fazla parametre kullanımı

if __name__ == "__main__":
    main()


# Bu kodda, en_buyuk_yaz(s1, s2) fonksiyonu iki sayıyı parametre olarak alır ve büyük olanı yazdırır.
# Eğer sayılar eşitse, "eşit" mesajı yazdırılır.
#
# en_buyuk_yaz_kullanici_girisli() fonksiyonu, kullanıcıdan iki sayı alır ve bu sayıları en_buyuk_yaz(s1, s2)
# fonksiyonuna gönderir. Böylece, kullanıcıdan alınan sayılar için büyük olanı bulma işlemi gerçekleştirilir.
# 
# main() fonksiyonu, programın ana giriş noktasıdır ve diğer fonksiyonları uygun sırayla çağırır.
# Bu yapı, kodun modüler ve okunabilir olmasını sağlar.