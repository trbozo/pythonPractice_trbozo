# int i = 0;
# while(i < 5) {
#     int j = 0;
#     while(j < i) {
#         System.out.print("*");
#         j++;
#     }
#     System.out.println();
#     i++;
# }


i = 0
while i < 5:
    j = 0
    while j < i:
        print("*", end="")
        j += 1
    print()  # Yeni bir satıra geçmek için
    i += 1


# print() fonksiyonunun end parametresi ile aynı satırda birden fazla değer basılabilir