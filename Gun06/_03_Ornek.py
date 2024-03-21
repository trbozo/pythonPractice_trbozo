# // Scanner oku=new Scanner(System.in);
# // System.out.print("Kilonuzu giriniz(kg)=");
# // double kilo=oku.nextDouble();
# // System.out.print("Boyunuzu giriniz(m)=");
# // double boy=oku.nextDouble();
# // double kitleIndex= kilo / (boy*boy);
# // System.out.println("Boyunuz="+boy+", kilonuz="+kilo);
# // System.out.println("kitleIndex = " + kitleIndex);
kilo = float(input("Kilonuzu giriniz(kg)="))
boy = float(input("Boyunuzu giriniz(m)="))
kitle_indexi = kilo / (boy ** 2)
print(f"Boyunuz={boy}, kilonuz={kilo}")
print("kitleIndex =", kitle_indexi)
