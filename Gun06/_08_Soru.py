# // Scanner oku=new Scanner(System.in);
# // System.out.print("Cümle giriniz=");
# // String cumle=oku.nextLine();
# // int uzunluk = cumle.length();
# // char sonHarf= cumle.charAt(uzunluk-1);
# // System.out.println("sonHarf = " + sonHarf);
cumle = input("Cümle giriniz=")
uzunluk = len(cumle)
son_harf = cumle[uzunluk - 1]
print("sonHarf =", son_harf)
