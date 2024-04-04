# package Gun09;
#
# import java.util.Scanner;
#
# public class _05_Soru {
#     public static void main(String[] args) {
#         // kullanıcının gireceği 2 sayının birbirine
#         // eşit mi olup olmadığını yazdırınız
#
#         Scanner  oku=new Scanner(System.in);
#
#         System.out.print("Sayi1=");
#         int sayi1=oku.nextInt();
#
#         System.out.print("Sayi2=");
#         int sayi2=oku.nextInt();
#
#         System.out.println("Eşit Mi = " + (sayi1==sayi2)); // 1.yöntem
#
#         boolean esitMi= (sayi1==sayi2);
#         System.out.println("esitMi = " + esitMi);  //2.yöntem
#     }
# }

sayi1 = int(input("Sayi1="))
sayi2 = int(input("Sayi2="))

# 1.yöntem
print("Eşit Mi =", sayi1 == sayi2)

# 2.yöntem
esit_mi = sayi1 == sayi2
print("esitMi =", esit_mi)


#Bu Python kodu, kullanıcıdan iki sayı alır ve bu sayıların birbirine eşit olup olmadığını kontrol eder.
# Java kodundaki iki yöntem de Python'da uygulanmıştır: İlk yöntemde, doğrudan print fonksiyonu içinde karşılaştırma yapılırken;
# ikinci yöntemde, karşılaştırmanın sonucu bir değişkene atanır ve bu değişken daha sonra yazdırılır. Python'da,
# Java'daki Scanner sınıfına benzer bir yapı yoktur; bunun yerine input() fonksiyonu kullanılarak kullanıcı girdisi alınır.