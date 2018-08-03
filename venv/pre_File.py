# -*- coding: utf-8 -*-
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import random
import math

a = []

def loadin_data(path):
    file = open(path)
    lines = file.readlines()
    for line in lines:
        sub=line.split(" ")
        str_num = int(sub[0])
        end_num=int(sub[1])
        a.append(str_num)
        a.append(end_num)
    arr = np.array(a).reshape(-1,2)
    return arr
    # minvalue = np.min(arr)
    # maxvalue = np.max(arr)
    # difference = maxvalue-minvalue+1
    # return difference
# for line in lines:
#     sub = line.split(" ")
#     start_num = int(sub[0])
#     end_num = int(sub[1])
#     a.append(start_num)
#     a.append(end_num)
def get_difference(arr):
    minvalue = np.min(arr)
    maxvalue = np.max(arr)
    difference = maxvalue - minvalue + 1;
    return difference

def draw_graph(arr):
    minvalue = np.min(arr)
    maxvalue = np.max(arr)
    difference = maxvalue - minvalue + 1;
    graph = np.zeros(shape=(difference,difference))
    for row in arr:
        x_aix = row[0]-minvalue
        y_aix = row[1]-minvalue
        graph[x_aix][y_aix]+=1
    return graph
# arr = np.array(a).reshape(-1,2)
# matrix = np.zeros(shape=(difference,difference))
# 建立transition matrix(static)（每个timeslot一个）
# for row in arr:
#     x_aix = row[0]-minvalue
#     y_aix = row[1]-minvalue
#     matrix[x_aix][y_aix]=1

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
        if x0+actualstep>diff:
            n_x = (x0+actualstep-diff)%diff
            x0 = n_x
        else:
            x0 = x0+actualstep
    elif direction == 'l':
        if x0-actualstep<0:
            step = (actualstep-x0)%diff
            x0 = diff-step
        else:
            x0 = x0 - actualstep
    elif direction == 'u':
        if y0-actualstep<0:
            step = (actualstep-x0)%diff
            y0 = diff-step
        else:
            y0=y0-actualstep
    else:
        if y0+actualstep>diff:
            step = (y0+actualstep-diff)%diff
            y0 = step
        else:
            y0 = y0+actualstep

    position = str(x0)+";"+str(y0)
    print(position)
    return position

def each_walk(position,matrix,diff):
    sub = position.split(";")
    x =int(sub[0])
    y = int(sub[1])
    nodelist=[]
    # print("ori")
    # print(matrix)
    if(isEmpty(matrix)):
        print("node in each walk:" + nodelist)
        nodelist.append("0;0")
        return nodelist
    else:
        matrix[x][y] = matrix[x][y] - 1
        # print("============")
        # print(matrix)
        nodelist.append(position)
        dire = get_direction(x, y, diff)
        # print("direction:" + dire)

        return nodelist



def each_patterns(mat,diff):
    nodelist = []

    while len(nodelist) < 3:
        x0 = np.random.randint(0, diff)
        y0 = np.random.randint(0, diff)
        while mat[x0][y0] <= 0:
            x0 = np.random.randint(0, diff)
            y0 = np.random.randint(0, diff)
        po = str(x0) + ";" + str(y0)
        print("po" + po)
        node = each_walk(po, mat, diff)
        nodelist.append(node)
    return nodelist

def isEmpty(mat):
    isempty = False
    for index,value in enumerate(mat):
        if(mat.all()>0):
            isempty = True
            break
    return isempty

def choose_from_graph(path,list,out):
    file_in = open(path)
    for line in file_in.readlines():
        sub = line.split(" ")
# sub[0]:start point;sub[1]:end point
# list has 3 nodes a -->b-->c so we need find edge:ab ba ac ca bc cb
#         if(sub[0] = )

# main to call the functions
path = "D:/For-F-drive/school/comp/research/snap/examples/temporalmotifs/example-temporal-graph.txt"
arr_tmp = loadin_data(path)
# mat = draw_graph(arr_tmp)
diff = get_difference(arr_tmp)
node_list=[]
# Get the patterns
i = 0
while(i<3):
    mat = draw_graph(arr_tmp)
    # print(mat)
    list = each_patterns(mat,diff)
    node_list.append(list)
    i = i + 1
    print(list)

