#25. テンプレートの抽出
#記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
#基礎情報
import json,gzip,re

jdata = "jawiki-country.json.gz"
string = ""
def uk():
    with gzip.open(jdata,'rt',encoding= "utf-8") as gjdata:
        for line in gjdata:
            jdict = json.loads(line)
            if jdict['title'] == 'イギリス':
                return jdict['text']
text = uk()
#print(text)
def basic(text):

    m1 =re.compile(r'{{基礎情報 国.*',re.MULTILINE + re.VERBOSE)
    a = re.match(text)
    #{{.*}} ??
    #m2 = re.search(r'(.*)\n}}\n',string[m1.end():])
    return m1
                #return string[m1.end():m2.end()+1]
print(basic(text))


