import re
import json
import gzip

jdata = "jawiki-country.json.gz"

with gzip.open(jdata,'rt',encoding= "utf-8") as gjdata:
    for line in gjdata:
        jdict = json.loads(line)
        print(jdict)
        if jdict['title'] == 'イギリス':
            print(jdict["text"])
            break

'''エラーまとめ
open時に'rt'入れ忘れ テキストとして読み込む場合はrt
読むだけならrのみか無しでおｋ
'''