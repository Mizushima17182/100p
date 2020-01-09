'''18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ
（注意: 各行の内容は変更せずに並び替えよ）
'''
import sys
#data = sys.argv
#print(data)

with open("hightemp.txt",mode='r',encoding="utf-8")as hight:
    data = hight.readlines()
    for line in data:
        line = line +" \n"
    print(line)
    print(data)
    sorted(data,key=lambda line: float(line.split("\t")[2]))
    print(data)