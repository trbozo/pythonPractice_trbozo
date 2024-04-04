# package Gun13;
#
# import java.util.Scanner;
#
# public class _04_Switch {
#     public static void main(String[] args) {
#         // Girilen bir Ay numarasına göre ayın gün sayısını yazdırınız.
#
#         Scanner oku=new Scanner(System.in);
#         System.out.print("Ay no=");
#         int ayNo=oku.nextInt();
#
#         switch (ayNo){
#             case 1: System.out.println(31); break;
#             case 2 : System.out.println(28);break;
#             case 3 : System.out.println(31);break;
#             case 4 : System.out.println(30);break;
#             case 5 : System.out.println(31);break;
#             case 6 : System.out.println(30);break;
#             case 7 : System.out.println(31);break;
#             case 8 : System.out.println(31);break;
#             case 9 : System.out.println(30);break;
#             case 10 : System.out.println(31);break;
#             case 11 : System.out.println(30);break;
#             case 12 : System.out.println(31);break;
#             default : System.out.println("Hatalı Ay No");
#         }
#
#         //2.Yol
#         switch (ayNo){
#             case 2 : System.out.println(28);break;
#
#             case 3 :
#             case 1 :
#             case 5 :
#             case 7 :
#             case 8 :
#             case 10 :
#             case 12 : System.out.println(31);break;
#
#             case 4 :
#             case 6 :
#             case 9 :
#             case 11 : System.out.println(30);break;
#
#             default : System.out.println("Hatalı Ay No");
#         }
#
#
#
#
#     }
# }


# Girilen bir Ay numarasına göre ayın gün sayısını yazdırın

ay_no = int(input("Ay no="))

# 1. Yol: Her ayın gün sayısını ayrı ayrı belirtmek
if ay_no == 1:
    print(31)
elif ay_no == 2:
    print(28)
elif ay_no == 3:
    print(31)
elif ay_no == 4:
    print(30)
elif ay_no == 5:
    print(31)
elif ay_no == 6:
    print(30)
elif ay_no == 7:
    print(31)
elif ay_no == 8:
    print(31)
elif ay_no == 9:
    print(30)
elif ay_no == 10:
    print(31)
elif ay_no == 11:
    print(30)
elif ay_no == 12:
    print(31)
else:
    print("Hatalı Ay No")

# 2. Yol: Bazı ayların gün sayısını tek bir case altında birleştirmek
# Bu yöntem, kodu daha kısa tutar ve bakımı daha kolay hale getirir
# Örneğin, 28 gün olan Şubat ayı için ayrı bir case kullanılabilir

# Şubat ayı
if ay_no == 2:
    print(28)
# 31 gün olan aylar
elif ay_no in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
# 30 gün olan aylar
elif ay_no in [4, 6, 9, 11]:
    print(30)
else:
    print("Hatalı Ay No")
