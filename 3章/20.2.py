import gzip,json,sys
#file = sys.argv

file = "jawiki-country.json.gz"

with gzip.open(file,'rt',encoding="utf-8")as gfile:
    for d in gfile:
        jd = json.loads(d)
        if jd["title"] == "イギリス":
           print(jd["text"])