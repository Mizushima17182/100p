with open("hightemp.txt", mode='r', encoding="utf-8")as hight:
    lines = hight.readlines()
lines.sort(key = lambda line: float(line.split('\t')[2]))
#lines.sort(key = lamda line: float(line.split('\t'[2])) )
for line in lines:
    print(line,end = '')
