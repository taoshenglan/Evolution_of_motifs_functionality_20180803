# -*- coding: utf-8 -*-
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.sparse as sci



def get_X_matrix_file(total_dir):
    file = os.listdir(total_dir)
    # timeslot_number = get_timeslot()
    a = []
    b = []
    c = []
    d = []
    e = []
    h = []
    g = []
    i= []
    j = []
    k = []
    l=[]
    m=[]
    n=[]
    o=[]
    p=[]
    q=[]
    r=[]
    s=[]
    for file_tmp in file:
        if not os.path.isdir(total_dir + "/" + file_tmp):
            path = total_dir + "/" + file_tmp
            with open(path, 'r', encoding='utf-8')as f:
                for line in f:
                    sub = line.split(" ")
                    for i in sub:
                        i_number = int(i)
                        if str(file_tmp).__contains__("90001"):
                            a.append(i_number)
                        elif str(file_tmp).__contains__("90002"):
                            b.append(i_number)
                        elif str(file_tmp).__contains__("90003"):
                            c.append(i_number)
                        elif str(file_tmp).__contains__("90004"):
                            d.append(i_number)
                        elif str(file_tmp).__contains__("90005"):
                            e.append(i_number)
                        elif str(file_tmp).__contains__("90006"):
                            h.append(i_number)
                        elif str(file_tmp).__contains__("90007"):
                            g.append(i_number)
                        elif str(file_tmp).__contains__("90008"):
                            i.append(i_number)
                        elif str(file_tmp).__contains__("90009"):
                            j.append(i_number)
                        elif str(file_tmp).__contains__("90010"):
                            k.append(i_number)
                        elif str(file_tmp).__contains__("90011"):
                            l.append(i_number)
                        elif str(file_tmp).__contains__("90012"):
                            m.append(i_number)
                        elif str(file_tmp).__contains__("90013"):
                            n.append(i_number)
                        elif str(file_tmp).__contains__("90014"):
                            o.append(i_number)
                        elif str(file_tmp).__contains__("90015"):
                            p.append(i_number)
                        elif str(file_tmp).__contains__("90016"):
                            q.append(i_number)
                        elif str(file_tmp).__contains__("90017"):
                            r.append(i_number)
                        elif str(file_tmp).__contains__("90018"):
                            s.append(i_number)



        else:
            file2 = os.listdir(total_dir + "/" + file_tmp)
            print(file2)
            for file_sub in file2:
                path = total_dir + "/" + file_tmp+"/"+file_sub
                f = open(path)
                # print(os.path.splitext(path))
                iter_f = iter(f)
                for line in iter_f:
                    if str(os.path.splitext(path)[0]).find("_90001") != -1:
                        a.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90002") != -1:
                        b.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90003") != -1:
                        c.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90004") != -1:
                        d.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90005") != -1:
                        e.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90006") != -1:
                        h.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90007") != -1:
                        g.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90008") != -1:
                        i.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90009") != -1:
                        j.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90010") != -1:
                        k.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90011") != -1:
                        l.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90012") != -1:
                        m.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90013") != -1:
                        n.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90014") != -1:
                        o.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90015") != -1:
                        p.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90016") != -1:
                        q.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90017") != -1:
                        r.append(line)
                    elif str(os.path.splitext(path)[0]).find("_90018") != -1:
                        s.append(line)
    path2 = "D:/For-F-drive/school/comp/research/Desktop/Email/Lasso_file/for_500perT"
    fname = path2 + "/" + "matrix_file_" + str(900001) + ".txt"
    fout = open(fname, 'w')
    for element in a:
        fout.write(element)
    fout.close()
    fname1 = path2 + "/" + "matrix_file_" + str(900002) + ".txt"
    fout1 = open(fname1, 'w')
    for element in b:
        fout1.write(element)
    fout1.close()
    fname2 = path2 + "/" + "matrix_file_" + str(900003) + ".txt"
    fout2 = open(fname2, 'w')
    for element in c:
        fout2.write(element)
    fout2.close()
    fname3 = path2 + "/" + "matrix_file_" + str(900004) + ".txt"
    fout3 = open(fname3, 'w')
    for element in d:
        fout3.write(element)
    fout3.close()
    fname4 = path2 + "/" + "matrix_file_" + str(900005) + ".txt"
    fout4 = open(fname4, 'w')
    for element in e:
        fout4.write(element)
    fout4.close()
    fname5 = path2 + "/" + "matrix_file_" + str(900006) + ".txt"
    fout5 = open(fname5, 'w')
    for element in h:
        fout5.write(element)
    fout5.close()
    fname6 = path2 + "/" + "matrix_file_" + str(900007) + ".txt"
    fout6 = open(fname6, 'w')
    for element in g:
        fout6.write(element)
    fout6.close()
    fname7 = path2 + "/" + "matrix_file_" + str(900008) + ".txt"
    fout7 = open(fname7, 'w')
    for element in i:
        fout7.write(element)
    fout7.close()
    fname8 = path2 + "/" + "matrix_file_" + str(900009) + ".txt"
    fout8 = open(fname8, 'w')
    for element in j:
        fout8.write(element)
    fout8.close()
    fname9 = path2 + "/" + "matrix_file_" + str(900010) + ".txt"
    fout9 = open(fname9, 'w')
    for element in k:
        fout9.write(element)
    fout9.close()
    fname10 = path2 + "/" + "matrix_file_" + str(900011) + ".txt"
    fout10 = open(fname10, 'w')
    for element in l:
        fout10.write(element)
    fout10.close()
    fname11 = path2 + "/" + "matrix_file_" + str(900012) + ".txt"
    fout11 = open(fname11, 'w')
    for element in m:
        fout11.write(element)
    fout11.close()
    fname12 = path2 + "/" + "matrix_file_" + str(900013) + ".txt"
    fout12 = open(fname12, 'w')
    for element in n:
        fout12.write(element)
    fout12.close()
    fname13 = path2 + "/" + "matrix_file_" + str(900014) + ".txt"
    fout13 = open(fname13, 'w')
    for element in o:
        fout13.write(element)
    fout13.close()
    fname14 = path2 + "/" + "matrix_file_" + str(900015) + ".txt"
    fout14 = open(fname14, 'w')
    for element in p:
        fout14.write(element)
    fout14.close()
    fname15 = path2 + "/" + "matrix_file_" + str(900016) + ".txt"
    fout15 = open(fname15, 'w')
    for element in q :
        fout15.write(element)
    fout15.close()
    fname16 = path2 + "/" + "matrix_file_" + str(900017) + ".txt"
    fout16 = open(fname16, 'w')
    for element in r:
        fout16.write(element)
    fout16.close()
    fname17 = path2 + "/" + "matrix_file_" + str(900018) + ".txt"
    fout17 = open(fname17, 'w')
    for element in s:
        fout17.write(element)
    fout17.close()

            # sub = line.split(" ")
                    # for i in sub:
                    #     i_number = int(i)
                    #     if str(os.path.splitext(path)[0]).find("_90001")!=-1:
                    #         a.append(i_number)
                    #     elif str(os.path.splitext(path)[0]).find("_90002")!=-1:
                    #         b.append(i_number)
                    #     elif str(os.path.splitext(path)[0]).find("_90003")!=-1:
                    #         c.append(i_number)
                    #     elif str(os.path.splitext(path)[0]).find("_90004")!=-1:
                    #         d.append(i_number)
                    #     elif str(os.path.splitext(path)[0]).find("_90005")!=-1:
                    #         e.append(i_number)
                    #     elif str(os.path.splitext(path)[0]).find("_90006")!=-1:
                    #         h.append(i_number)
                    #     elif str(os.path.splitext(path)[0]).find("_90007")!=-1:
                    #         g.append(i_number)

    # arr_a = np.array(a).reshape(-1,36)
    # arr_b = np.array(b).reshape(-1,36)
    # arr_c = np.array(c).reshape(-1,36)
    # arr_d = np.array(d).reshape(-1,36)
    # arr_e = np.array(e).reshape(-1,36)
    # arr_h = np.array(h).reshape(-1,36)
    # arr_g = np.array(g).reshape(-1,36)

    # print("======")
    # data = sci.csc_matrix((arr_a.T))
    # print(data)
    # return arr_a,arr_b,arr_c,arr_d,arr_e,arr_h,arr_g

# def get_timeslot():


if __name__=='__main__':
    get_X_matrix_file("D:/For-F-drive/school/comp/research/Desktop/Email/out_500perT")



