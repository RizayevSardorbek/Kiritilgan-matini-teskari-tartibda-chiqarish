t = input("Ixtiyoriy matin kiriting : ")
s = ''
b = []
for i in t:
    b.append(i)
b.reverse()
for n in b:
    s = s + n
print("Siz kiritgan matn : ", t)
print("Siz kiritgan matning teskari tartibdagi ko'rinishi : ", s)
