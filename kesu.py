import matplotlib.pyplot as plt,numpy as np

left = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #横軸の数値
label = ["a","b","c","d","e","f","g","h","i","j"] #横軸のラベル
height = np.array([1,2,3,4,5,6,7,8,9,10])
plt.bar(left, height,tick_label=label,align="center")
plt.show()