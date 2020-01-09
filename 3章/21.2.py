import gzip,json,sys,re
#file = sys.argv

file = "jawiki-country.json.gz"
def Englanddata():
    with gzip.open(file,'rt',encoding="utf-8")as gfile:
        England = []
        for d in gfile:
            jd = json.loads(d)
            if jd["title"] == "イギリス":
                return jd["text"]
            #England.append(jd["text"])
            #return England
pata =re.compile(r'^(.*\[\[Category:.*\]\].*)$', re.MULTILINE + re.VERBOSE)
resu = pata.findall(Englanddata())
for line in resu:
    print(line)

