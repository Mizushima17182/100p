import json
import gzip
import re
jsond = "jawiki-country.json.gz"
def uk():
    with gzip.open(jsond,"rt",encoding="utf-8_sig")as jdata:
        jdict = {}
        udict = {}
        for line in jdata:
            jdict = json.loads(line)
            if jdict["title"] == "イギリス":
                return jdict["text"]


#re.MULTILINE + re.VERBOSE
pata = re.compile(r'^(.*\[\[Category\]\].*)$')
resu = pata.findall(uk())


print(resu)

