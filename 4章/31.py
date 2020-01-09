import re

# 動詞の表層形をすべて抽出せよ．
# 表層形　基本形(原型)　品詞　品詞細分類
# lisdic{'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞'}

path_neko = "nekolist.txt"
surfacelist = []
cou = 0
with open(path_neko, "rt", encoding="utf-8")as nekolisttxt:  # テキストの読み込み
    nekolist = nekolisttxt.read()
    nekolist = nekolist.strip("[]")
   # print(nekolist)
    nekolist = list(nekolisttxt)  # リストに変換
   # print(type(nekolist))
    #　print(nekolist)


    for lisdic in nekolist: # 辞書を一つずつ読み込み
        print(lisdic)
        if lisdic == "動詞":
            surfacelist.append()
            cou = cou + 1
            if cou == 1:
                break
