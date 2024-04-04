#Java'daki if koşullarını kullanarak yapılan karşılaştırmalar ve
# koşullar Python'da aynı şekilde ifade edilir.


# // int not = 75;
# // if (not >= 90) {
# //     System.out.println("Harf notunuz: A");
# // } else if (not >= 80) {
# //     System.out.println("Harf notunuz: B");
# // } else {
# //     System.out.println("Daha çok çalışmalısınız.");
# // }


notu = 75
if notu >= 90:
    print("Harf notunuz: A")
elif notu >= 80:
    print("Harf notunuz: B")
else:
    print("Daha çok çalışmalısınız.")
