# Java kodunun Python'a dönüştürülmüş hali

# Substring  : string den parça alır
#         012345678901234567
s1 = "Merhaba Java yı sevenler derneği üyeleri"

parca1 = s1[3:9]  # 3 den başla 9 a kadar al
# 3 parametrede index, 3 den 9 a kadar al, 9 dahil değil
print("parca1 =", parca1)  # haba J

print("s1[8:15] =", s1[8:15])  # Java yı

print("s1[8:] =", s1[8:])  # verilneden SONA kadar parçayı alır


#Python'da substring metodunun karşılığı olarak dilin dilimleme (slicing) özelliği kullanılır. Bu özellikte, [başlangıç_index:bitiş_index] şeklinde belirtilen aralık, başlangıç indexini (dahil) alırken, bitiş indexini (hariç) alır. Eğer başlangıç indexi belirtilmezse, stringin başlangıcından başlar. Eğer bitiş indexi belirtilmezse, stringin sonuna kadar alır.






