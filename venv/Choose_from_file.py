# -*- coding: utf-8 -*-

import subprocess
import unittest
import os

def callThe_Exe_file(param_i,param_o):
    exe_name = "C:\\TAO_motifs\\snap\\examples\\temporalmotifs\\temporalmotifsmain.exe"
# param_i = "C:\\\\TAO_motifs\\\\snap\\\\examples\\\\temporalmotifs\\\\example-temporal-graph.txt"
    param_delta=3600*24
    # param_o = "C:\\\\TAO_motifs\\\\snap\\\\examples\\\\temporalmotifs\\\\test_output.txt"
    print("----------------------------------")
    param = exe_name+" -i:"+param_i+" -delta:"+str(param_delta)+" -o:"+param_o

    print(param_i)
    try:
        subprocess.Popen(param)
    except Exception as e:
        print(e)

def Through_file(total_dir):
    file = os.listdir(total_dir)
    outID=900000
    for file_tmp in file:
        if not os.path.isdir(total_dir + "\\" + file_tmp):
            path = total_dir + "\\" + file_tmp
            out_dir = "C:\\Users\\cssltao\\Desktop\\CollegeMsg\\sub-graph\\out_test"
            if os.path.exists(out_dir) == False:
                os.mkdir(out_dir)
            filelength = open(path).read()

            if len(filelength)==0:
            #     建立一个全为0的文件
                print("=============")
                fout = open(out_dir+"\\"+file_tmp, 'w')
                fout.write("0 0 0 0 0 0\n"+
                           "0 0 0 0 0 0\n"+
                           "0 0 0 0 0 0\n"+
                           "0 0 0 0 0 0\n"+
                           "0 0 0 0 0 0\n"+
                           "0 0 0 0 0 0\n" )
                fout.close()
            else:
                param_o = param_o = out_dir+"\\"+file_tmp
                callThe_Exe_file(path, param_o)

        else:
            outID +=1
            file2 = os.listdir(total_dir + "\\" + file_tmp)
            k = 90001
            # built new direction
            out_dir = "C:\\Users\\cssltao\\Desktop\\CollegeMsg\\sub-graph\\out_test\\"+file_tmp
            if os.path.exists(out_dir) == False:
                os.mkdir(out_dir)
            for file_sub in file2:

                param_i = total_dir + "\\" + file_tmp+"\\"+file_sub
                param_o = out_dir + "\\" + file_sub
                filelength = open(param_i).read()
                if len(filelength)==0:
                    fout = open(param_o, 'w')
                    fout.write("0 0 0 0 0 0\n" +
                               "0 0 0 0 0 0\n" +
                               "0 0 0 0 0 0\n" +
                               "0 0 0 0 0 0\n" +
                               "0 0 0 0 0 0\n" +
                               "0 0 0 0 0 0\n")
                    fout.close()
                else:
                    callThe_Exe_file(param_i,param_o)



if __name__ == '__main__':
    # exe_name = "C:\\\\TAO_motifs\\\\snap\\\\examples\\\\temporalmotifs\\\\temporalmotifsmain.exe"
    # param_i = "C:\\\\TAO_motifs\\\\snap\\\\examples\\\\temporalmotifs\\\\example-temporal-graph.txt"
    # param_o = "C:\\\\TAO_motifs\\\\snap\\\\examples\\\\temporalmotifs\\\\test_output.txt"
    dir = "C:\\Users\\cssltao\\Desktop\\CollegeMsg\\sub-graph\\test"
    Through_file(dir)