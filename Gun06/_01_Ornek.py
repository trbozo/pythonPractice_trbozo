# // Scanner oku=new Scanner(System.in);
# // System.out.print("Uzun Kenarı giriniz=");
# // int uzunKenar = oku.nextInt();
# // System.out.print("Kısa Kenarı giriniz=");
# // int kisaKenar = oku.nextInt();
# // int cevre=uzunKenar+uzunKenar+kisaKenar+kisaKenar;
# // int alan = uzunKenar*kisaKenar;
# // System.out.println("Cevre = " + cevre);
# // System.out.println("alan = " + alan);
uzun_kenar = int(input("Uzun Kenarı giriniz="))
kisa_kenar = int(input("Kısa Kenarı giriniz="))
cevre = 2 * (uzun_kenar + kisa_kenar)
alan = uzun_kenar * kisa_kenar
print("Cevre =", cevre)
print("Alan =", alan)
