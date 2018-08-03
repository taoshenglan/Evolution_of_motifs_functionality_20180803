# -*- coding: utf-8 -*-

import math
file = open("wiki-talk-temporal.txt")
timeslot = 60*60*24*30
print("============timeslot: "+str(timeslot)+"=============")
lasttime = 0;
group1 = ""
# group2=""
# group3=""
i = 1
lines = file.readlines()
# to get time lasttime and decided how many subgraph should have
firstline = lines[0]
lastline = lines[-1]
tmp_f = firstline.split(" ")
tmp=lastline.split(" ")
firsttime = int(tmp_f[2])
lasttime = int(tmp[2])
print("start at: "+str(firsttime))
print("end at: "+str(lasttime))
num_sub=math.ceil((lasttime-firsttime)/timeslot)
print("# of timeslots groups: "+str(num_sub))
# to get groups of sub-text file
while i < num_sub+1:
    group1 = ""
    for line in lines:

        sub = line.split(" ")
        time = int(sub[2])
        if i<=1:
            if time < timeslot*i+firsttime:
                group1 += line
            else:
                break
        else:
            if time >= timeslot*(i-1)+firsttime and time < timeslot*i+firsttime:
                group1 += line

    # print("=======group "+str(i)+"=================")
    # print(group1)
    filename = "wiki_output_file"+str(i)+".txt"
    print(filename)
    fout = open(filename,"w")
    fout.write(group1)
    fout.close()

    i = i+1

file2 = open("")
