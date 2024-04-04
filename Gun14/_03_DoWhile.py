# package Gun14;
#
# import java.util.Scanner;
#
# public class _03_DoWhile {
#     public static void main(String[] args) {
#         // Kullanıcı 0 değeri girene kadar sayı isteyiniz ve sayıları
#         // toplayınız , 0 girdiğinde toplamı yazınız
#
#         // döngünün içindekiler neler?
#         // sayı oku,  toplam=toplam+sayi,
#         // döngünü şartı sayı!=0
#         Scanner oku=new Scanner(System.in);
#         int toplam=0, sayi;
#
#         System.out.print("Sayi giriniz=");
#         sayi=oku.nextInt();
#         toplam=toplam+sayi;
#
#         while (sayi!=0){  // şartı kontrol et, sonra dön
#             System.out.print("Sayi giriniz=");
#             sayi=oku.nextInt();
#             toplam=toplam+sayi;
#         }
#         System.out.println("toplam = " + toplam);
#         toplam=0;
#         // kardeşi Do_While
#         // şartı kontrol etmeden 1 kez çalış, sonra kontrol ederk çalış
#         do{  // bu döngü şarta bağlı olmaksızı 1 kere çalışır,
#             System.out.print("2.döngü Sayi giriniz=");
#             sayi=oku.nextInt();
#             toplam=toplam+sayi;
#         }while (sayi!=0);
#
#         System.out.println("toplam = " + toplam);
#
#         // While : önce kontrol sonra döngü
#         // do_while : önce 1 kez çalış , sonra kontrol, sonra döngü
#
#         // kontrol önce ise WHİLE
#         // kontrol sonda ise DO_WHİLE
#     }
# }


# Kullanıcı 0 değeri girene kadar sayı isteyiniz ve sayıları toplayınız,
# 0 girdiğinde toplamı yazınız

# Döngünün içindekiler neler?
# sayı oku, toplam=toplam+sayi
# döngünün şartı sayı != 0

toplam = 0
sayi = int(input("Sayı giriniz="))
toplam += sayi

while sayi != 0:  # Şartı kontrol et, sonra dön
    sayi = int(input("Sayı giriniz="))
    toplam += sayi

print("toplam =", toplam)
toplam = 0

# Kardeşi Do_While
# Şartı kontrol etmeden 1 kez çalış, sonra kontrol ederek çalış
sayi = 1
while sayi != 0:
    sayi = int(input("2.döngü Sayı giriniz="))
    toplam += sayi

print("toplam =", toplam)

# While: Önce kontrol, sonra döngü
# Do_while: Önce 1 kez çalış, sonra kontrol, sonra döngü

# Kontrol önce ise WHILE
# Kontrol sonra ise DO_WHILE


# kullanıcıdan 0 değeri girilene kadar sayı istenir ve bu sayıların toplamı hesaplanır. İlk döngü while ile başlar ve döngü koşulu sayi != 0 olarak belirlenir. Döngü içinde kullanıcıdan sayı alınır ve toplam değişkenine eklenir. Döngü 0 girilene kadar devam eder ve toplam sonucu ekrana yazdırılır. Ardından, do-while döngüsüyle aynı işlem yapılır. Bu döngüde koşul while anahtar kelimesinden sonra gelir, bu nedenle döngü en az bir kez çalışır ve daha sonra koşul kontrol edilir.






