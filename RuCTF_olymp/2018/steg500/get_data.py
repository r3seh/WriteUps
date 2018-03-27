from PIL import Image
import numpy as np
img = Image.open("fiv_l.png")
arr = np.array(img)

s_f = []
s_s = []
s_t = []
s_4 = []
for i in arr:
    for j in i:
        s_f += [255 - j[0]]
        s_s += [255 - j[1]]
        s_t += [255 - j[2]]
        s_4 += [255 - j[3]]

f = open("res", mode="wb")
cont = s_f + s_s + s_t + s_4
f.write(bytes(cont))
f.close()

