# package Gun09;
#
# import java.util.Scanner;
#
# public class _06_Soru {
#     public static void main(String[] args) {
#         // girilen bir sayının tek sayı olup olmadığını yazdırınız.
#         // true veya false
#
#         Scanner oku=new Scanner(System.in);
#         System.out.print("Sayi=");
#         int sayi=oku.nextInt();
#
#         int kalan= sayi%2; // modül hep kalanı verir
#
#         System.out.println("Tek Mi ? "+ (kalan==1) );  // 1.yöntem
#
#         boolean tekMi= (kalan==1);
#         System.out.println("tekMi = " + tekMi);  // 2.Yöntem
#     }
# }

sayi = int(input("Sayi="))

kalan = sayi % 2  # modül hep kalanı verir

# 1.yöntem
print("Tek Mi ?", kalan == 1)

# 2.Yöntem
tek_mi = kalan == 1
print("tekMi =", tek_mi)


#Bu Python kodu, girilen bir sayının tek sayı olup olmadığını kontrol eder ve sonucu ekrana yazdırır.
# Java'daki gibi, mod operatörü (%) kullanılarak sayının 2'ye bölümünden kalan hesaplanır ve
# bu kalanın 1 olup olmadığına bakılarak sayının tek olup olmadığı belirlenir. Python'da,
# Java'daki Scanner sınıfına benzer bir yapı yoktur; kullanıcıdan veri almak için input() fonksiyonu kullanılır.