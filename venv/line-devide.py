# -*- coding: utf-8 -*-
import os
import numpy as np

path = "D:/For-F-drive/school/comp/research/Desktop/CollegeMsg/out_delta1D"
files = os.listdir(path)
s = []
a = []

filenames = []
j = 9001
while j<9037:
    filename_tmp = "linediv_cm_M"+str(j)+".txt"
    filenames.append(filename_tmp)

    j = j+1



for file in files:
    if not os.path.isdir(file):
        f = open(path+"/"+file)
        iter_f = iter(f);
        string=""
        a = []
        for line in iter_f:

            sub = line.split(" ")
            for i in sub:
                i_num = int(i)
                a.append(i_num)


        # print("=======================arr=================")
        arr = np.array(a)
        arr = arr.reshape((6,6))
        # print(arr)
        k = 0
        path2 = "D:/For-F-drive/school/comp/research/Desktop/CollegeMsg/liner_d1D"
        for element in arr.flat:

            fname = path2+"/"+filenames[k]
            fout = open(fname, "a")
            str_a = str(element)
            fout.write(str_a+" ")
            fout.close()
            k = k + 1


