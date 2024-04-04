# public class Main {
#     public static void main(String[] args) {
#         int temperature = 25;
#         if (temperature > 30) {
#             System.out.println("Sıcak bir gündesiniz.");
#         } else if (temperature > 20) {
#             System.out.println("Ilık bir gündesiniz.");
#         } else if (temperature > 10) {
#             System.out.println("Serin bir gündesiniz.");
#         } else {
#             System.out.println("Soğuk bir gündesiniz.");
#         }
#     }
# }

temperature = 25
if temperature > 30:
    print("Sıcak bir gündesiniz.")
elif temperature > 20:
    print("Ilık bir gündesiniz.")
elif temperature > 10:
    print("Serin bir gündesiniz.")
else:
    print("Soğuk bir gündesiniz.")


##Java'daki if-else-if yapısı Python'da benzer şekilde uygulanmaktadır.
# Her iki dilde de koşullar sırayla değerlendirilir ve ilk doğru koşulun bloğu çalıştırılır.