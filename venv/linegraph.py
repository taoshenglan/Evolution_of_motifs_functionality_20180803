import matplotlib.pyplot as plt
import os
import numpy as np
import seaborn as sns

path = "D:/For-F-drive/school/comp/research/Desktop/wiki/liner_d1D"
files = os.listdir(path)
# to get the range of x axes and the total number of each timeslot
path2 = "D:/For-F-drive/school/comp/research/Desktop/wiki/out_delta1D"
file2=os.listdir(path2)
count=0
totalnumber=[]
for file_tmp in file2:
    if not os.path.isdir(file_tmp):
        count = count+1
        f_t = open(path2+"/"+file_tmp)
        iter_f_t = iter(f_t)
        total=0
        for line_t in iter_f_t:
            sub = line_t.split(" ")

            for i in sub:
                i_num = int(i)
                total = total+i_num
        print(total)
        totalnumber.append(total)
# total_arr = np.array(totalnumber)
# test=open("C:/Users/cssltao/Desktop/Email_Eu/out_file/out_College_7.txt")
# lines=test.readlines()
# total=0
# for line in lines:
#     sub = line.split(" ")
#
#     for i in sub:
#         i_num = int(i)
#         total=i_num+total
# totalnumber.append(total)
total_arr = np.array(totalnumber)
print(total_arr)


#
#
#
j = 1
h = 0
a = []
for file in files:
    if not os.path.isdir(file):
        f = open(path+"/"+file)
        iter_f = iter(f)
        # tmp_name = f.name
        # print(tmp_name)
        y = []
        for line in iter_f:
            h = 0
            sub = line.split(" ")
            print("====sub=====")
            print(sub)
            for i in sub:
                if i != '':
                    i_num = int(i)
                    t = total_arr[h]
                    # print(str(i_num)+"/"+str(t))
                    if t==0:
                        i_num = 0
                    else:
                        i_num = i_num/t
                    y.append(i_num)
                    if h<(count-1):
                        h=h+1
            # print("---------------")
        y_arr = np.array(y)
        x = range(0,count)
        x_arr = np.array(x)
        color_ran = "#%06x"%np.random.randint(0,0xFFFFFF)
        string = "motif" + str(j)

        j = j + 1
        plt.plot(x_arr,y_arr,color=color_ran,label=string)


plt.xlabel('Time slot (30Days)')
plt.ylabel('ratio of motif in each time slot')
plt.title('The Trends of Mofits in wiki Dataset(delta=1Day)')
# box = plt.get_position()
# f, ax= plt.subplots()
# f = plt.gcf()
# f.set_size_inches(20,10)
ax = plt.gca()

box = ax.get_position()
print(box)
ax.set_position([box.x0, box.y0,box.x1*0.86, box.height]) # resize position
print(ax.get_position())
# Put a legend to the right side
ax.legend( loc='center left',bbox_to_anchor=(1, 0.5), ncol=2,)
# plt.legend(loc='left',ncol=3,)
plt.savefig("D:/For-F-drive/school/comp/research/Desktop/wiki/trend_for_cm(delta=1Day).png",dpi=100, bbox_inches='tight')
plt.show()



