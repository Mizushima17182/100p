import json, gzip, re

jsondata = 'jawiki-country.json.gz'


def uk():
    with gzip.open(jsondata, 'rt', encoding="utf-8")as gdata:
        for gline in gdata:
            linej = json.loads(gline)
            if linej['title'] == 'イギリス':
                return linej['text']


# print( uk())
# 正規表現　基礎情報抜き出し

pattern = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}$', re.MULTILINE + re.VERBOSE + re.DOTALL)
resu1 = pattern.findall(uk())
# (.+?)(?:(?=\n\|)| (?=\n$))
pattern2 = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)| (?=\n$))', re.MULTILINE + re.VERBOSE + re.DOTALL)
resu2 = pattern2.findall(resu1[0])
dicre = {}
for dicdata in resu2:
    dicre[dicdata[0]] = dicdata[1]
# print(resu1)
print(resu2)
#print(dicre)
for dicline in dicre.items():
    print(dicline)