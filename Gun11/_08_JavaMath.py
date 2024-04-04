# package Gun11;
#
# public class _08_JavaMath {
#     public static void main(String[] args) {
#         int a=12;
#         int b=4;
#
#         //2 değer için geçerli
#         System.out.println("a ve b den büyük olanı="+ Math.max(a,b)  );
#         System.out.println("a ve b den küçük olanı="+ Math.min(a,b)  );
#         System.out.println(" 2 nin 3. kuvvet ="+ Math.pow(2,3)  );
#         System.out.println("b nin karekökü="+ Math.sqrt(b)  );
#         System.out.println("round yuvarlama 3.1 = "+  Math.round(3.1));// 3
#         System.out.println("round yuvarlama 3.5 = "+  Math.round(3.5));// 4
#
#         System.out.println("ceil 3.1 = "+  Math.ceil(3.1)); // 4, bu rakamdan büyük en yakın tam sayı
#         System.out.println("ceil 3.9 = "+  Math.ceil(3.9)); //4, bu rakamdan büyük en yakın tam sayı
#
#         System.out.println("floor 3.1 = "+  Math.floor(3.1)); //3, bu rakamdan küçük en yakın tam sayı
#         System.out.println("floor 3.9 = "+  Math.floor(3.9)); //3, bu rakamdan küçük en yakın tam sayı
#     }
# }


import math

a = 12
b = 4

# 2 değer için geçerli
print("a ve b den büyük olanı =", max(a, b))
print("a ve b den küçük olanı =", min(a, b))
print("2 nin 3. kuvveti =", pow(2, 3))
print("b nin karekökü =", math.sqrt(b))
print("round yuvarlama 3.1 =", round(3.1))  # 3
print("round yuvarlama 3.5 =", round(3.5))  # 4

print("ceil 3.1 =", math.ceil(3.1))  # 4, bu rakamdan büyük en yakın tam sayı
print("ceil 3.9 =", math.ceil(3.9))  # 4, bu rakamdan büyük en yakın tam sayı

print("floor 3.1 =", math.floor(3.1))  # 3, bu rakamdan küçük en yakın tam sayı
print("floor 3.9 =", math.floor(3.9))  # 3, bu rakamdan küçük en yakın tam sayı
