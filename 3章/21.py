import json
import gzip
import re

jdata = "jawiki-country.json.gz"
def uk():
    with gzip.open(jdata,'rt',encoding= "utf-8") as gjdata:
        for line in gjdata:
            jdict = json.loads(line)
            if jdict['title'] == 'イギリス':
                return jdict['text']

pata = re.compile('.*\[\[Category:.*')
resu =pata.findall(uk())
#print(resu)
for line in resu:
    print(line)
'''
for line in jdict:
    jdict = json.loads(line)
    if jdict[] == 'イギリス':
        print(jdict["text"])
        break
'''
#r'.*\[\[Category.*\]\]$'