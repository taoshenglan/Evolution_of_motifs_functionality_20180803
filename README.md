# Evolution_of_motifs_functionality_20180803
Evolution_of_motifs_functionality_20180803
=======Evolution of Network Functionality========
examp.py: To divide the original dataset into sub-datasets based on the time slot we choose. In this function, you can input the filename and the length of the time slot.



Choose_from_file.py: To call the Temperalmotifsmain.c function of snap. In this function, the user needs to provide the path of the temperalmotifsmain.c function, the input filenames(the paths of files that need to be analyzed), delta(time window) value and output filenames(to store the results of analysis). If the input file is empty, the Choose_from_file function will output the result with all value equals to 0, otherwise, the output value should be given by the temperalmotifsmain.c function.

line-devided.py: To select all the data in each time slot datasets of each motif, record them as files. Each motif has one file. In this function, the user needs to provide the input filenames(the paths of analyzed files) and output filename (for each motif).

linergraph.py: To drow the linear graph for each dataset based on the line-divided files. Each line presents the trends of proportion that each motif has over time. In this function, the user needs to provide the input filenames(the paths of files that contains the data of each motif), the filenames that contains the number of motifs in each time slot(to get the total number of motifs) and the output information of the figure(filename, title, name of y-label and position of legend if needed).  


count.py: To draw the heatmaps of the time slot datasets. The user needs to provide the input filenames(the paths of linear-divided files that need to be analyzed, and the filenames of sub-datasets files to get the number of elements in the heatmap), output information of figure(filename, title, x_label, and y_label).

pre-processing_2.py: To randomly select the 3-nodes patterns and drag the data of these pattern in each time slot. Each pattern has a directory in which it contains the data of this pattern in each time slot datasets. In this function, the user needs to provide the input filenames(the paths of files that contain the original data) and output filenames.
	sub functions:
	- loadin_data(path): to divide the original data into a temporary array(2 columns-start point and end point) without the information about the timestamps for each edge. The temporary array should be returned. The user needs to provide the path of original data.
	-get_difference(arr): to get the size of the adjacency matrix. 
	-draw_graph(arr): to build the adjacency matrix and return it.
	-get_direction(x0,y0,graphsize):to decide a direction of selection of the next node based on the start position (x0,y0) in the adjacency matrix. This function should return the direction as a string.
	-Single_walk(direction,x0,y0,mat,diff):to get the next node based on the position(x0,y0) in the direction that the user provided. The new position should be returned.
	-each_walk(position,matrix,diff): to start a selection of a node. The position of the node should be returned.
	-each_patterns(mat, diff):to get the 3-nodes pattern. A node list that contains positions of 3 nodes should be returned.
	-choose_from-graph(path,list,outID,arr):to start the whole selection and decoument these into output files. In this function, the user needs to provide the directory that contains the sub-datasets of each time slot and the output filenames.

tes_2.py: To get the motif matrix file of each pattern for each time slot. The user needs to provide the input filename(the path of files that contains each patterns motif results in each time slot), output filenames(each time slot has one output file) (The number of temporary arrays and output filenames could be changed).

test.py: To get the transition matrix and draw the heatmap and network graph of the transition matrix based on the output file that gave by tes_2.py. In this function, the user needs to provide the input file directory (which contains the output files in tes_2.py) and the output information(the path of heatmap and network figures). The number of the temporary matrix should be changed depends on the number of time slots the dataset has. 


===========================The way to run the program=======================
1. Download the datasets from http://snap.stanford.edu/data.
2. Use examp.py to divide the original datasets into sub-datasets based on the time slots. 
3. Use Choose_from_file.py to analyze each sub-datasets and get the results. These results will be decumented as out-files.
4. Use line-devided.py to deal with the results get from step3 and store them as linear-divided files.
5. Use linegraph.py and count.py to get the heatmaps of motifs in each time slot in the datasets and linear graphs of tendency of motifs.(the input files should be linear-divided files and the out-files should be used as the files to get total number of motifs in each time slot in count.py).
6. Use pre-processing_2.py to randomly choose patterns for further analysis. The input files should be original dataset and the sub-datasets of different time slots. The output files contains the data information of each pattern in different time slots, we called pattern files.
7. Use Choose_from_file.py to analyze each file in pattern files and get the output results as patter_matrix files.
8. Use tes_2.py to deal with the pattern_matrix files, then get the output files named pattern_matrix_timeslot files.
9. Use test.py to get the transition matrix based on the pattern_matrix_timeslot files, then you will get the network and heatmap figures.   

