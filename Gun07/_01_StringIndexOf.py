# // String cumle="Merhaba Dünya";
cumle = "Merhaba Dünya"

# // System.out.println("cumle.indexOf(M) = " + cumle.indexOf("M"));
# // System.out.println("cumle.indexOf(h) = " + cumle.indexOf("h"));
# // System.out.println("cumle.indexOf(a) = " + cumle.indexOf("a"));
# // System.out.println("cumle.indexOf(Dü) = " + cumle.indexOf("Dü"));
# // System.out.println("cumle.indexOf( ) = " + cumle.indexOf(" "));
# // System.out.println("cumle.indexOf(A) = " + cumle.indexOf("A"));
# // System.out.println("cumle.indexOf(z) = " + cumle.indexOf("z"));
# // System.out.println("cumle.indexOf(a,5) = " + cumle.indexOf("a",5));
# // System.out.println("cumle.indexOf(a,7) = " + cumle.indexOf("a", 7));
print(f"cumle.indexOf('M') = {cumle.find('M')}")
print(f"cumle.indexOf('h') = {cumle.find('h')}")
print(f"cumle.indexOf('a') = {cumle.find('a')}")
print(f"cumle.indexOf('Dü') = {cumle.find('Dü')}")
print(f"cumle.indexOf(' ') = {cumle.find(' ')}")
print(f"cumle.indexOf('A') = {cumle.find('A')}")
print(f"cumle.indexOf('z') = {cumle.find('z')}")
print(f"cumle.indexOf('a', 5) = {cumle.find('a', 5)}")
print(f"cumle.indexOf('a', 7) = {cumle.find('a', 7)}")


#Python'da find() metodu, Java'daki indexOf() metoduna benzer işlev görür ve bulamazsa -1 döndürür.