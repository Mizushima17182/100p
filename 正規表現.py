import re
a1 = "[[記事名]]"
a2 = "[[記事名|表示文字]]"
a3 = "[[記事名#節名|表示文字]]"

b = re.compile(r"\[\[(.*)\]\]")

resu = b.findall(a1)
resu2 = b.findall(a2)
resu3 =b.findall(a3)

print(resu,resu2,resu3)
