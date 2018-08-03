# -*- coding: utf-8 -*-
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import random
import math
import threading


def loadin_data(path):
    a = []
    with open(path,'r',encoding='utf-8')as f:
        for line in f:
            sub = line.split(" ")
            str_num = int(sub[0])
            end_num = int(sub[1])
            a.append(str_num)
            a.append(end_num)
    arr = np.array(a).reshape(-1,2)
    return arr

def get_difference(arr):
    minvalue = np.min(arr)
    maxvalue = np.max(arr)
    difference = maxvalue - minvalue + 1;
    return difference

def draw_graph(arr):
    minvalue = np.min(arr)
    maxvalue = np.max(arr)
    difference = maxvalue - minvalue + 1;
    # print("min:" + str(minvalue) + " max: " + str(maxvalue))
    graph = np.zeros(shape=(difference,difference))
    for row in arr:
        x_aix = row[0]-minvalue
        y_aix = row[1]-minvalue
        graph[x_aix][y_aix]+=1
    return graph

# 建立transition matrix(static)（每个timeslot一个）

def get_direction(x0,y0,graphsize):
    # u-->up, d-->down, r-->right, l-->left
    move = ["u","d","r","l"]
    # move_x0--> 0,1 为x=0 y=max的情况， 1,2为x=0 y=0的情况
    move_x0 = ["r","d","l"]
    move_x_max = ["r","u","l"]
    move_y0 = ["r","u","d"]
    move_ymax = ["l","u","d"]
    direction = ""
    if x0 == 0:
        if y0 == 0:
            direction = move_x0[np.random.randint(0,1)]
        elif y0 == graphsize:
            direction = move_x0[np.random.randint(1,2)]
        else:
            direction = move_x0[np.random.randint(0,2)]
    elif x0 == graphsize:
        if y0 == 0:
            direction = move_x_max[np.random.randint(0,1)]
        elif y0 == graphsize:
            direction = move_x_max[np.random.randint(1,2)]
        else:
            direction = move_x_max[np.random.randint(0,2)]
    elif y0 == 0:
        direction = move_y0[np.random.randint(0,2)]
    elif y0 == graphsize:
        direction = move_ymax[np.random.randint(0,2)]
    else:
        direction = move[np.random.randint(0,3)]
    return direction

# request value of 1. direction of the nodes 2. x0, 3.y0 and 4. count matrix of the graph(row-->x, Col-->y) 5. graphsize
# and
def Single_walk(direction,x0,y0,mat,diff):
    actualstep = np.random.randint(0,1000)
    step = 0
    # get actual step of the x0 should or y0 should do
    if direction == 'r':
        if (x0+actualstep)>(diff-1):
            n_x = (x0+actualstep-diff)%diff
            x0 = n_x
        else:
            x0 = x0+actualstep-1
    elif direction == 'l':
        if x0-actualstep<0:
            step = (actualstep-x0)%diff
            x0 = diff-1-step
        else:
            x0 = x0 - actualstep
    elif direction == 'u':
        if y0-actualstep<0:
            step = (actualstep-x0)%diff
            y0 = diff-step-1
        else:
            y0=y0-actualstep
    else:
        if y0+actualstep>(diff-1):
            step = (y0+actualstep-diff)%diff
            y0 = step
        else:
            y0 = y0+actualstep-1

    position = str(x0)+";"+str(y0)
    # print(position)
    return position

def each_walk(position,matrix,diff):
    sub = position.split(";")
    x =int(sub[0])
    y = int(sub[1])

    # print("ori")
    # print(matrix)
    dire = get_direction(x, y, diff)
    node = Single_walk(dire, x, y, matrix, diff)
    node_sub = node.split(";")
    x_node = int(node_sub[0])
    y_node = int(node_sub[1])
    while matrix[x_node][y_node] <= 0:
        node = Single_walk(dire, x, y, matrix, diff)
        node_sub = node.split(";")
        x_node = int(node_sub[0])
        y_node = int(node_sub[1])
    # print("node: "+node+" and value: "+str(matrix[x_node][y_node]))
    return node





def each_patterns(mat,diff):
    nodelist = []

    x0 = np.random.randint(0, diff-1)
    y0 = np.random.randint(0, diff-1)
    while mat[x0][y0] <= 0:
        x0 = np.random.randint(0, diff-1)
        y0 = np.random.randint(0, diff-1)
    po = str(x0) + ";" + str(y0)
    # print("po " + po+" value = "+str(mat[x0][y0]))
    node0 = each_walk(po, mat, diff)
    # print("node0:" + node0)

    sub0 = node0.split(";")
    nodelist.append(str(x0))
    nodelist.append(str(y0))
    if sub0[0]==str(x0) :
        nodelist.append(sub0[1])
    else:
        nodelist.append(sub0[0])

    # print(nodelist)
    return nodelist

#for each pattern, choose their data from the whole dataset
def choose_from_graph(path, list, outID, arr):
        # Open the following timeslot dataset
        # each list has 3 nodes, a,b,c. so we need to find out all possible edges ab,ba,ac,ca,bc,cb
        minvalue = np.min(arr)
        maxvalue = np.max(arr)
        a = int(list[0]) + minvalue
        b = int(list[1]) + minvalue
        c = int(list[2]) + minvalue
        print("A:" + str(a) + " B:" + str(b) + " C:" + str(c))
        files = os.listdir(path)
        # each pattern should has its own folder
        out_dir = "C:/Users/cssltao/Desktop/CollegeMsg/sub-graph/test/pattern" + str(outID)
        if os.path.exists(out_dir) == False:
            os.mkdir(out_dir)
        k = 90001
        # for each file in the timeslot sub-datasets
        for file in files:
            if not os.path.isdir(file):
                f = open(path + "/" + file)
                iter_f = iter(f);
                string = ""
                count = 0

                # check whether the it has such a node
                # record the edge information that satisfy the requret
                fname = out_dir + "/" + "cm_Pattern" + str(outID) + "_" + str(k) + ".txt"
                fout = open(fname, 'a')
                for line in iter_f:
                    # sub[0]-->start point, sub[1]-->destinatin point; sub and list are string list
                    sub = line.split(" ")
                    # print(sub)
                    sp = int(sub[0])
                    ep = int(sub[1])
                    if sp == a:
                        if ep == b:
                            # print("a-->b:"+line)
                            count += 1
                            fout.write(line)
                        elif ep == c:
                            # print("a-->c:"+line)
                            count += 1
                            fout.write(line)
                    elif sp == b:
                        if ep == a:
                            count += 1
                            # print("b-->a:"+line)
                            fout.write(line)
                        elif ep == c:
                            count += 1
                            # print("B-->c:"+line)
                            fout.write(line)
                    elif sp == c:
                        if ep == a:
                            count += 1
                            # print("c-->a:"+line)
                            fout.write(line)
                        elif ep == b:
                            count += 1
                            # print("c-->b:"+line)
                            fout.write(line)


                k = k + 1
                print("count:" + str(count))
                fout.close()
                # print("file "+fname+" has completed!")







# sub[0]:start point;sub[1]:end point
# list has 3 nodes a -->b-->c so we need find edge:ab ba ac ca bc cb
#         if(sub[0] = )

# main to call the functions
def thread_method(tname,i_start,i_end,t_path):
    print("creating thread "+tname+"!")
    # path = "C:/Users/cssltao/Desktop/CollegeMsg/input_file/CollegeMsg_output_file1.txt"
    path = t_path
    path_dir = "C:/Users/cssltao/Desktop/CollegeMsg/Input_file"
    # path_dir = path
    arr_tmp = loadin_data(path)
    # print(arr_tmp)
    isEnd = False
    mat = draw_graph(arr_tmp)
    # print(mat)
    diff = get_difference(arr_tmp)
    node_list = []
    # Get the patterns
    i = i_start

    k=90001
    while (i < i_end):
        thread_name = "sub_thread"+str(i)
        # mat = draw_graph(arr_tmp)
        subthread = mysubThread(thread_name,mat,diff,path_dir)
        subthread.start()
        subthread.join()
        list = subthread.get_node()
        # # df = pd.DataFrame(data=mat)
        # # print(df)
        #
        node_list.append(list)
        i=i+1
        k = 900000+i
        choose_from_graph(path_dir,list,k,arr_tmp)
    # print(node_list)
    print("Thread "+tname+" end!")
    isEnd=True
    return isEnd

class mysubThread(threading.Thread):
    def __init__(self,name,mat,diff,path_dir):
        threading.Thread.__init__(self)
        self.name = name
        self.mat = mat
        self.diff = diff
        self.path_dir = path_dir

    def run(self):
        print("=========="+self.name+"===========")
        self.list = each_patterns(self.mat, self.diff)

    def get_node(self):
        return self.list

class myThread(threading.Thread):
    def __init__(self,name,i_start,i_end,t_path):
        threading.Thread.__init__(self)
        self.name = name
        self.i_start = i_start
        self.i_end = i_end
        self.t_path = t_path
    def run(self):
        self.isEnd = thread_method(self.name,self.i_start,self.i_end,self.t_path)
    def getResult(self):
        return self.isEnd


thread0 = myThread("thread0",0,10,"C:/Users/cssltao/Desktop/CollegeMsg/input_file/CollegeMsg_output_file1.txt")
thread1 = myThread("thread1",10,20,"C:/Users/cssltao/Desktop/CollegeMsg/input_file/CollegeMsg_output_file1.txt")
thread2 = myThread("thread2",20,30,"C:/Users/cssltao/Desktop/CollegeMsg/input_file/CollegeMsg_output_file1.txt")
# thread3 = myThread("thread3",900,1200,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9004.txt")
# thread4 = myThread("thread4",1200,1500,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9005.txt")
# thread5 = myThread("thread5",1500,1800,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9006.txt")
# thread6 = myThread("thread6",1800,2100,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9007.txt")
# thread7 = myThread("thread7",2100,2400,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9008.txt")
# thread8 = myThread("thread8",2400,2700,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9009.txt")
# thread9 = myThread("thread9",2700,3000,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9010.txt")
# thread10 = myThread("thread10",3300,3600,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9011.txt")
# thread11 = myThread("thread11",3600,3900,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9012.txt")
# thread12 = myThread("thread12",3900,4200,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9013.txt")
# thread13 = myThread("thread13",4200,4500,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9014.txt")
# thread14 = myThread("thread14",4500,4800,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9015.txt")
# thread15 = myThread("thread15",5100,5400,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9016.txt")
# thread16 = myThread("thread16",5700,6000,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9017.txt")
# thread17 = myThread("thread17",6000,6300,"C:/Users/cssltao/Desktop/Email_Eu/Input_file/sample_output_file9018.txt")
# #
# path_input ="C:/Users/cssltao/Desktop/CollegeMsg/input_file"
# file_dir=os.listdir(path_input)
# h = 90001
# for file_tmp in file_dir:
#     if not os.path.isdir(file_tmp):
#         f = path_input + "/" + file_tmp
#         thread_h = myThread("thread"+str(h),0,500, f)
#         thread_h.start()
#         thread_h.join()
thread0.start()
thread1.start()
thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()
# thread8.start()
# thread9.start()
# thread10.start()
# thread11.start()
# thread12.start()
# thread13.start()
# thread14.start()
# thread15.start()
# thread16.start()
# thread17.start()

thread0.join()
thread1.join()
thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()
# thread6.join()
# thread7.join()
# thread8.join()
# thread9.join()
# thread10.join()
# thread11.join()
# thread12.join()
# thread13.join()
# thread14.join()
# thread15.join()
# thread16.join()
# thread17.join()
