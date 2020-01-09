#カテゴリ名抽出
import gzip
import json
jdata = "jawiki-country.json.gz"
with gzip.open(jdata,"rt",encoding="utf-8")as data:
    jdata = []
    for line in data:
        jdict =json.loads(line)
        if jdict["title"] == "イギリス":
            jdata.append(jdict)
    for kate in jdict:
        if kate in :
            print(kate)