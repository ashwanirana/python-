import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib as mpl
cmap = plt.cm.jet

DATA=np.array([[ 0,  0,  0.18,  0.5],
       [ 0,  0 ,  0.18,  0.6],
       [ 0,  0 ,  0.2,  0.58],
       [ 0,  0,  0.41,  0.5],
       [ 0,  0,  0.73,  0.2]])

cNorm  = colors.Normalize(vmin=np.min(DATA[:,3])+.2, vmax=np.max(DATA[:,3]))

scalarMap = cmx.ScalarMappable(norm=cNorm,cmap=cmap)
names=np.array(["Woman","Man","Boy","Cat","Car"])

plt.subplots()
plt.figure(figsize=(9,6))
for idx in range(0,len(DATA[:,1])):
    colorVal = scalarMap.to_rgba(DATA[idx,3])
    plt.arrow(DATA[idx,0],  #x1
              DATA[idx,1],  # y1
              DATA[idx,2]-DATA[idx,0], # x2 - x1
              DATA[idx,3]-DATA[idx,1], # y2 - y1
              color=colorVal,head_width=0.012, head_length=0.02)
for i,names in enumerate (names):
    plt.annotate(names, (DATA[i][2],DATA[i][3]))
plt.annotate("HUMAN CLUSTER", (0.1,0.7),color='r')
plt.annotate("ANIMAL CLUSTER", (0.35,0.6),color='b')
plt.annotate("OBJECT CLUSTER", (0.7,0.3))
plt.title("WORD2VEC")
plt.show()

names=np.array(["Woman","Man","Boy","Cat","Car"])

print("KNN Similarity with Man")
for i in range(0,5):
    print(names[i],":",1-plt.mlab.dist(DATA[i],DATA[1]))
print("")

c=[]
for i in range(0,5):
    c.append(np.sqrt(DATA[i][2]**2+DATA[i][3]**2))

for i in range(0,5):
    print("Cosine Similarity with Man:",names[i],1-c[1]*((plt.mlab.dist(DATA[i],DATA[1])/c[i])))