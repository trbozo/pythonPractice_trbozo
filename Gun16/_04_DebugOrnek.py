# package Gun16;
#
# public class _04_DebugOrnek {
#     public static void main(String[] args) {
#
#         for(int i = 0; i < 40; i++) {
#
#             if(i / 15 == 1) {
#                 continue;  // acaba i nin hangi değerleri için çalışacak
#             }
#
#             System.out.println( i );
#         }
#
#
#
#     }
# }


# Python'da continue ifadesi ile aynı mantığı sağlamak için geçişi kontrol ederek döngüyü yönlendirebiliriz.

for i in range(40):
    if i // 15 == 1:
        continue
    print(i)


# Bu Python kodu, 0'dan 39'a kadar olan sayıları yazdıracaktır. Ancak continue ifadesi, i değeri 15'e tam bölündüğünde döngüyü atlar, yani 15 ve 30'un yazdırılmasını engeller.
#
# Şimdi, bu Python kodunu adım adım çalıştıralım:

for i in range(40):
    if i // 15 == 1:  # 0 // 15 = 0, 1 // 15 = 0, ..., 14 // 15 = 0, 15 // 15 = 1
        continue
    print(i)


#Sonuç olarak, bu Python kodu 0'dan 39'a kadar olan tüm sayıları yazdıracak, ancak 15 ve 30'u atlayacak.


