# package Gun17;
#
# import java.util.Scanner;
#
# public class _04_JavaSplitMetodu {
#     public static void main(String[] args) {
#         // Kullanıcının gireceği bir cumlede kaç kelime olduğunu bulunuz
#         // Bugun hava cok guzel -> 4
#
#         Scanner oku=new Scanner(System.in);
#         System.out.print("cümle=");
#         String cumle=oku.nextLine();
#
#         // 1.Yöntem
#         int boslukSayisi=0;
#         for (int i = 0; i < cumle.length(); i++) {
#               if (cumle.charAt(i)==' ')
#                   boslukSayisi++;  // burada bosluk sayısını buluyorum
#         }
#
#         System.out.println("kelimeSayisi = " + (boslukSayisi+1) );
#
#         //2.Yöntem
#         String[] kelimeler= cumle.split(" "); // bosluga göre bol ve elemanları dizi olarak ver
#         System.out.println("kelimeler = " + kelimeler.length);
#
#         for (int i = 0; i < kelimeler.length; i++) {
#             System.out.println("kelimeler = " + kelimeler[i]);
#         }
#
#         //3.Yöntem
#         System.out.println("kelimeler = " + cumle.split(" ").length);
#     }
# }


cumle = input("cümle=")

# 1. Yöntem
bosluk_sayisi = 0
for char in cumle:
    if char == ' ':
        bosluk_sayisi += 1
print("kelimeSayisi =", bosluk_sayisi + 1)

# 2. Yöntem
kelimeler = cumle.split(" ")
print("kelimeler =", len(kelimeler))
for kelime in kelimeler:
    print("kelimeler =", kelime)

# 3. Yöntem
print("kelimeler =", len(cumle.split(" ")))


#Bu Python kodu, kullanıcının girdiği cümledeki boşluk sayısını sayarak kelime sayısını bulur. Ayrıca split() yöntemini kullanarak cümleyi böler ve elde edilen kelimeleri dizi olarak alır. Daha sonra dizinin uzunluğunu, yani kaç kelime olduğunu belirler.






