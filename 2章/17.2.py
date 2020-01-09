'''17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）
を求めよ．確認にはsort, uniqコマンドを用いよ．'''
with open("hightemp.txt",mode='r',encoding="utf-8")as hight:
    iti = set()
    print(iti)
    resu = ""
    jdata = hight.readlines()
    for line in jdata:
        d = line.split()
        iti.add(d[0])
        #iti=iti+d[0] + "\n"
print(iti)