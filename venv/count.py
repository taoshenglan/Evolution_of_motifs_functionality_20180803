# -*- coding: utf-8 -*-
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# to get the range of x axes and the total number of each timeslot
path2 = "D:/For-F-drive/school/comp/research/Desktop/wiki/out_file"
file2=os.listdir(path2)
count=0
totalnumber=[]
# j = 9001
# for file in file2:
#     if not os.path.isdir(file):
#         f = path2+"/"+file
#         f_name=path2+"/"+"out_wiki_"+str(j)+".txt"
#         os.rename(f,f_name )
#         j = j+1

for file_tmp in file2:
    if not os.path.isdir(file_tmp):
        count = count+1
        f_t = open(path2+"/"+file_tmp)
        # print(path2+"/"+file_tmp)
        iter_f_t = iter(f_t)
        total=0
        for line_t in iter_f_t:
            sub = line_t.split(" ")
            for i in sub:
                i_num = int(i)
                total = total+i_num
        # print(total)
        totalnumber.append(total)

total_arr = np.array(totalnumber)
print(total_arr)
path="D:/For-F-drive/school/comp/research/Desktop/wiki/liner"

files = os.listdir(path)
j = 1
h = 0
a=[]
for file in files:
    if not os.path.isdir(file):
        # in a single file
        f = open(path+"/"+file)
        iter_f = iter(f)
        # print("===============")
        # h=0
        for line in iter_f:
            sub = line.split(" ")
            # print("===================")
            # print(sub)
            h = 0
            for i in sub:
                if i!='':
                    i_num = int(i)
                    t = total_arr[h]
                    # if t == 0:
                    #     i_num=0
                    # else:
                    #     # print(str(i_num)+"/"+str(t))
                    #     i_num = i_num/t

                    # a.append(lnum)

                    a.append(i_num)
                    if(h<count-1):
                        h = h+1
        # if(h<75):
        #     h = h+1
                # i_num = int(i)
                # a.append(i_num)

arr = np.array(a)
# print(len(arr))
arr = arr.reshape((36,count))
MaxValue = np.max(arr)

# print(arr)
# lines=file.readlines()
#
# a = []
# for line in lines:
#     sub = line.split(" ")
#     for i in sub:
#         i_num = int(i)
#         a.append(i_num)
#
# arr = np.array(a)
# arr = arr.reshape((6,6))
# print(arr)
#
#
#
df = pd.DataFrame(data=arr)
print(df)


f, ax= plt.subplots(figsize = (20,10))
# f,ax = plt.subplots()
# sns.heatmap(df,annot=True,fmt = '.3f',cmap='GnBu' ,linewidths='0.5',annot_kws={'size':7})
sns.heatmap(df,cmap='Blues' ,linewidths='0.5',vmax=MaxValue)
colorbar = ax.collections[0].colorbar
slot = MaxValue/5
colorbar.set_ticks([0,slot,slot*2,slot*3,slot*4,slot*5])
colorbar.set_ticklabels(['0', str(slot), str(slot*2),str(slot*3),str(slot*4),str(slot*5)])

# annot_kws={'horizontalalignment':'left'}
ax.set_title('Motifs in Each Timeslot in wiki(Number)')
# ax.set_title('Motifs in Each Timeslot in wiki(Ratio)')
ax.set_xlabel('Time Slot (30Days)')
ax.set_ylabel('The Type of Motif')
# ax.set_title('Correlation between features')
figname = "D:/For-F-drive/school/comp/research/Desktop/wiki/matrix_wiki_no_number.png"
f.savefig(figname, dpi=100, bbox_inches='tight')
plt.show()


