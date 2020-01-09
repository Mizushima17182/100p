with open("hightemp.txt",mode='r',encoding="utf-8")as hight:
    data = hight.read()
    for line in data:
        x = line,split()