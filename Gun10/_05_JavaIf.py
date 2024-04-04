# package Gun10;
#
# import java.util.Scanner;
#
# public class _05_JavaIf {
#     public static void main(String[] args) {
#         // Kullanıcının 2 kez gireceği şifresinin aynı olduğunu
#         // AYNI veya DEĞİL şeklinde cevaplayınız.  (confirm new password)
#
#         Scanner oku=new Scanner(System.in);
#
#         System.out.print("Şifre = ");
#         String sifre=oku.nextLine();
#
#         System.out.print("Şifre Tekrar= ");
#         String sifreTekrar=oku.nextLine();
#
#         boolean esitMi = sifre.equals(sifreTekrar);
#
#         if (esitMi)
#             System.out.println("Eşit");
#
#         if (!esitMi)
#             System.out.println("Değil");
#     }
# }

sifre = input("Şifre = ")
sifre_tekrar = input("Şifre Tekrar= ")

esit_mi = sifre == sifre_tekrar

if esit_mi:
    print("Eşit")
else:
    print("Değil")


##Bu Python kodu, kullanıcının girdiği iki şifrenin aynı olup olmadığını kontrol eder ve "Eşit" veya "Değil" olarak sonucu ekrana yazdırır. Java'da String.equals() metodu kullanılırken, Python'da doğrudan == operatörü ile string karşılaştırması yapılır. Kullanıcıdan veri almak için Python'da input() fonksiyonu kullanılır.