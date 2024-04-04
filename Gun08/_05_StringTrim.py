# Java kodunun Python'a dönüştürülmüş hali

# trim() : stringin başındaki ve sonundaki gereksiz boşlukları siler

text = "    İsmet temur   "

print("text = ->" + text + "<-")
print("text = ->" + text.strip() + "<-")


#Java'daki trim() metodu Python'daki strip() metodu ile aynı işlevi yerine getirir. Bu metodun kullanımı ve sonuçları Java ile aynıdır. Ancak, Python'da strip() metodu gereksiz boşlukları sadece dizinin başından ve sonundan kaldırır, ancak dizinin içindeki boşlukları kaldırmaz.