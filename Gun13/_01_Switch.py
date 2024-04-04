# package Gun13;
#
# import java.util.Scanner;
#
# public class _01_Switch {
#     public static void main(String[] args) {
#         // Girilen 2 tam sayıyı kullanıcıdan aldıktan sonra,
#         // Toplama için T, Çıkarma için Ç, çarpma için P, bölme için B
#         // harflerini yine kullanıcıdan alarak isteğe uygun olan
#         // işlemi yaptırıp sonucu yazdırınız.
#
#         Scanner okuInt=new Scanner(System.in);
#         Scanner okuStr=new Scanner(System.in);
#
#         System.out.print("1.Sayı = ");
#         int sayi1= okuInt.nextInt();  // 15
#
#         System.out.print("2.Sayı = ");
#         int sayi2= okuInt.nextInt();  // 3
#
#         System.out.println("Toplama için T");
#         System.out.println("Çıkarma için Ç");
#         System.out.println("Çarpma  için P");
#         System.out.println("Bölme   için B");
#         System.out.print("Seçiminiz=");
#         String seciminiz=okuStr.next().toUpperCase(); // T,Ç,P,B
#
#         switch (seciminiz){
#             case "T": System.out.println("toplam="+ (sayi1+sayi2) ); break;
#             case "Ç": System.out.println("Çıkarma="+ (sayi1-sayi2) );break;
#             case "P": System.out.println("Çarpma = "+ (sayi1*sayi2) );break;
#             case "B": System.out.println("Bölme = "+ ((double)sayi1/sayi2));break;
#             default : System.out.println("Hatalı giriş yaptını"); break;
#         }
#
#         // Çalışma mantığı: seciminiz T ye eşitse case de ki karşılığını yap ve çık(break)
#         // default : diğer şartlar gerçekleşmediyse, yukarıdaki tüm caselerin ELSE si gib
#     }
#
# }



# Girilen 2 tam sayıyı kullanıcıdan aldıktan sonra,
# Toplama için T, Çıkarma için Ç, çarpma için P, bölme için B
# harflerini yine kullanıcıdan alarak isteğe uygun olan
# işlemi yaptırıp sonucu yazdırın

sayi1 = int(input("1.Sayı = "))
sayi2 = int(input("2.Sayı = "))

print("Toplama için T")
print("Çıkarma için Ç")
print("Çarpma için P")
print("Bölme için B")
seciminiz = input("Seçiminiz= ").upper()  # T,Ç,P,B

# Switch case yapıları Python'da bulunmadığı için if-elif-else yapısı kullanılır
if seciminiz == "T":
    print("Toplam =", sayi1 + sayi2)
elif seciminiz == "Ç":
    print("Çıkarma =", sayi1 - sayi2)
elif seciminiz == "P":
    print("Çarpma =", sayi1 * sayi2)
elif seciminiz == "B":
    print("Bölme =", sayi1 / sayi2)
else:
    print("Hatalı giriş yaptınız")
