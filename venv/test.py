# -*- coding: utf-8 -*-
import seaborn as sns
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os
import scipy.sparse as sci
from sklearn import linear_model, discriminant_analysis, cross_validation,preprocessing

def load_data(*data):
    X_data,Y_data = data
    x_data=[]
    y_data=[]
    for single_arr in X_data:
        for row in single_arr:
            x_data.append(row)
    for single in Y_data:
        for row in single:
            y_data.append(row)

    X_train, X_test, y_train, y_test = cross_validation.train_test_split(x_data, y_data, test_size=0.25, random_state=0)
    print(pd.DataFrame(data=X_train))
    # norm = preprocessing.Normalizer().fit(X_train)
    # X_train = norm.transform(X_train)
    # print(pd.DataFrame(data=X_train))
    X_train = preprocessing.normalize(X_train,norm='l1')
    print("================Normalized X_train==========================")
    print(pd.DataFrame(data=X_train))
    X_test = preprocessing.normalize(X_test,norm='l1')
    print("================Normalized X_test==========================")
    print(pd.DataFrame(data=X_test))

    y_train = preprocessing.normalize(y_train,norm='l1')
    print("================Normalized y_train==========================")
    print(pd.DataFrame(data=y_train))

    y_test = preprocessing.normalize(y_test,norm='l1')
    print("================Normalized y_test==========================")
    print(pd.DataFrame(data=y_test))
    return X_train, X_test, y_train, y_test

def test_lasso(*data):
    X_train, X_test, y_train, y_test = data


    lassoRegression = linear_model.Lasso(alpha=0.000000000025,tol = 0.0001,positive=True)
    lassoRegression.fit(X_train, y_train)
    printted_Data = pd.DataFrame(data=lassoRegression.coef_)
    pd.set_option('display.width',1000)
    pd.set_option('precision', 5)
    pd.set_option('display.max_columns',None)
    pd.set_option('display.max_rows', None)  # 设置显示最大行
    print(printted_Data)
    # print(pd.DataFrame(data=lassoRegression.intercept_))
    # print("权重向量:%s, b的值为:%.2f" % (lassoRegression.coef_, lassoRegression.intercept_))

    print("预测性能得分: %.15f" % lassoRegression.score(X_test, y_test))
    return lassoRegression.coef_


#测试不同的α值对预测性能的影响
def test_lasso_alpha(*data):
    X_train, X_test, y_train, y_test = data
    alphas = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    scores = []
    for i, alpha in enumerate(alphas):
        lassoRegression = linear_model.MultiTaskLasso(alpha=alpha)
        lassoRegression.fit(X_train, y_train)
        scores.append(lassoRegression.score(X_test, y_test))
    return alphas, scores

def show_plot(alphas, scores):
    figure = plt.figure()
    ax = figure.add_subplot(1, 1, 1)
    ax.plot(alphas, scores)
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel(r"score")
    ax.set_xscale("log")
    ax.set_title("Ridge")
    plt.show()

def get_X_matrix(total_dir):
    file = os.listdir(total_dir)
    # timeslot_number = get_timeslot()
    a = []
    b = []
    c = []
    d = []
    e = []
    h = []
    g = []
    i = []
    j = []
    k = []
    l = []
    m = []
    n = []
    o = []
    p = []
    q = []
    r = []
    s = []
    for file_tmp in file:
        if not os.path.isdir( file_tmp):
            path = total_dir + "/" + file_tmp
            with open(path, 'r', encoding='utf-8')as f:
                for line in f:
                    sub = line.split(" ")
                    for z in sub:
                        z_number = int(z)
                        if str(os.path.splitext(path)[0]).find("_900001")!=-1:
                            a.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900002")!=-1:
                            b.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900003")!=-1:
                            c.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900004")!=-1:
                            d.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900005")!=-1:
                            e.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900006")!=-1:
                            h.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900007")!=-1:
                            g.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900008") != -1:
                            i.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900009") != -1:
                            j.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900010") != -1:
                            k.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900011") != -1:
                            l.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900012") != -1:
                            m.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900013") != -1:
                            n.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900014") != -1:
                            o.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900015") != -1:
                            p.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900016") != -1:
                            q.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900017") != -1:
                            r.append(z_number)
                        elif str(os.path.splitext(path)[0]).find("_900018") != -1:
                            s.append(z_number)

        # else:
        #     file2 = os.listdir(total_dir + "/" + file_tmp)
        #     print(file2)
        #     for file_sub in file2:
        #         path = total_dir + "/" + file_tmp+"/"+file_sub
        #         f = open(path)
        #         # print(os.path.splitext(path))
        #         iter_f = iter(f)
        #         for line in iter_f:
        #             sub = line.split(" ")
        #             for i in sub:
        #                 z_number = int(i)
        #                 if str(os.path.splitext(path)[0]).find("_90001")!=-1:
        #                     a.append(z_number)
        #                 elif str(os.path.splitext(path)[0]).find("_90002")!=-1:
        #                     b.append(z_number)
        #                 elif str(os.path.splitext(path)[0]).find("_90003")!=-1:
        #                     c.append(z_number)
        #                 elif str(os.path.splitext(path)[0]).find("_90004")!=-1:
        #                     d.append(z_number)
        #                 elif str(os.path.splitext(path)[0]).find("_90005")!=-1:
        #                     e.append(z_number)
        #                 elif str(os.path.splitext(path)[0]).find("_90006")!=-1:
        #                     h.append(z_number)
        #                 elif str(os.path.splitext(path)[0]).find("_90007")!=-1:
        #                     g.append(z_number)

    arr_a = np.array(a).reshape(-1,36)
    arr_b = np.array(b).reshape(-1,36)
    arr_c = np.array(c).reshape(-1,36)
    arr_d = np.array(d).reshape(-1,36)
    arr_e = np.array(e).reshape(-1,36)
    arr_h = np.array(h).reshape(-1,36)
    arr_g = np.array(g).reshape(-1,36)
    arr_i = np.array(i).reshape(-1, 36)
    arr_j = np.array(j).reshape(-1, 36)
    arr_k = np.array(k).reshape(-1, 36)
    arr_l = np.array(l).reshape(-1, 36)
    arr_m = np.array(m).reshape(-1, 36)
    arr_n = np.array(n).reshape(-1, 36)
    arr_o = np.array(o).reshape(-1, 36)
    arr_p = np.array(p).reshape(-1, 36)
    arr_q = np.array(q).reshape(-1, 36)
    arr_r = np.array(r).reshape(-1, 36)
    arr_s = np.array(s).reshape(-1,36)

    data_0 = pd.DataFrame(data=a)
    data_1 = pd.DataFrame(data=b)
    data_2 = pd.DataFrame(data=c)
    data_3 = pd.DataFrame(data=d)
    data_4 = pd.DataFrame(data=e)
    data_5 = pd.DataFrame(data=h)
    data_6 = pd.DataFrame(data=g)
    data_7 = pd.DataFrame(data=i)
    data_8 = pd.DataFrame(data=j)
    data_9 = pd.DataFrame(data=k)
    data_10 = pd.DataFrame(data=l)
    data_11 = pd.DataFrame(data=m)
    data_12 = pd.DataFrame(data=n)
    data_13= pd.DataFrame(data=o)
    data_14= pd.DataFrame(data=p)
    data_15 = pd.DataFrame(data=q)
    data_16 = pd.DataFrame(data=r)
    data_17 = pd.DataFrame(data=s)
    print(data_0)
    print("---------------------------------")
    print(data_1)
    print("---------------------------------")
    print(data_2)
    print("---------------------------------")
    print(data_3)
    print("---------------------------------")
    print(data_4)
    print("---------------------------------")
    print(data_5)
    print("---------------------------------")
    print(data_6)
    print("---------------------------------")
    print(data_7)
    print("---------------------------------")
    print(data_8)
    print("---------------------------------")
    print(data_9)
    print("---------------------------------")
    print(data_10)
    print("---------------------------------")
    print(data_11)
    print("---------------------------------")
    print(data_12)
    print("---------------------------------")
    print(data_13)
    print("---------------------------------")
    print(data_14)
    print("---------------------------------")
    print(data_15)
    print("---------------------------------")
    print(data_16)
    print("---------------------------------")
    print(data_17)








    # print("======")
    # data = sci.csc_matrix((arr_a.T))
    # print(data)
    return arr_a,arr_b,arr_c,arr_d,arr_e,arr_h,arr_g,arr_i,arr_j,arr_k,arr_l,arr_m,arr_n,arr_o,arr_p,arr_q,arr_r,arr_s
def show_net(g_matrix):
    G = nx.DiGraph()
    count = 0
    for i in range(len(g_matrix)):
        for j in range(len(g_matrix)):
            if g_matrix[i][j]>0.1:
                number = g_matrix[i][j]
                # G.add_edge([i,j,number])
                count+=1
                G.add_weighted_edges_from([(j, i, number)])

    nx.draw(G, pos=nx.spring_layout(G),node_color = 'b', edge_color = 'r',alpha = 0.5, with_labels = True,font_size = 15,
            node_size = 50,width = 0.5)
    in_degree = nx.in_degree_centrality(G)
    out_degree = nx.out_degree_centrality(G)
    i=0
    arr = np.zeros(shape=(36,3))
    while i<36:
        arr[i][0]=i
        if in_degree.__contains__(i):
            arr[i][1] = in_degree.get(i)
        else:
            arr[i][1] = 0.0
        if out_degree.__contains__(i):
            arr[i][2] = out_degree.get(i)
        else:
            arr[i][2] = 0.0
        i = i+1
    data = pd.DataFrame(data=arr,columns=['Motif ID','In-degree','Out-degree'])
    print(data)
    figname = "D:/For-F-drive/school/comp/research/Desktop/Email/Lasso_file/figure/trans_matrix_alpha-11_reduced_arrow.png"
    plt.savefig(figname, dpi=100, bbox_inches='tight')
    plt.show()
    return count
def show_heatmap(g_matrix):
    df = pd.DataFrame(data=g_matrix)
    f, ax = plt.subplots(figsize=(20, 10))
    # f,ax = plt.subplots()
    sns.heatmap(df,annot=True,fmt = '.4f',cmap='Blues' ,linewidths='0.5',annot_kws={'size':6})
    ax.set_title('Transition matrix')
    # ax.set_title('Motifs in Each Timeslot in wiki(Ratio)')
    # ax.set_title('Correlation between features')
    figname = "D:/For-F-drive/school/comp/research/Desktop/Email/Lasso_file/figure/heatmap_a_-11.png"
    f.savefig(figname, dpi=100, bbox_inches='tight')
    plt.show()


if __name__=='__main__':
    arr_timeslot1,arr_timeslot2,arr_timeslot3,arr_timeslot4,arr_timeslot5,arr_timeslot6,arr_timeslot7 ,arr_timeslot8,arr_timeslot9,arr_timeslot10,arr_timeslot11,arr_timeslot12,arr_timeslot13,arr_timeslot14,arr_timeslot15,arr_timeslot16,arr_timeslot17,arr_timeslot18= get_X_matrix("D:/For-F-drive/school/comp/research/Desktop/Email/Lasso_file/for_500perT")
    X_data = []
    X_data.append(arr_timeslot1)
    X_data.append(arr_timeslot2)
    X_data.append(arr_timeslot3)
    X_data.append(arr_timeslot4)
    X_data.append(arr_timeslot5)
    X_data.append(arr_timeslot6)
    X_data.append(arr_timeslot7)
    X_data.append(arr_timeslot8)
    X_data.append(arr_timeslot9)
    X_data.append(arr_timeslot10)
    X_data.append(arr_timeslot11)
    X_data.append(arr_timeslot12)
    X_data.append(arr_timeslot13)
    X_data.append(arr_timeslot14)
    X_data.append(arr_timeslot15)
    X_data.append(arr_timeslot16)
    X_data.append(arr_timeslot17)
    Y_data=[]
    Y_data.append(arr_timeslot2)
    Y_data.append(arr_timeslot3)
    Y_data.append(arr_timeslot4)
    Y_data.append(arr_timeslot5)
    Y_data.append(arr_timeslot6)
    Y_data.append(arr_timeslot7)
    Y_data.append(arr_timeslot8)
    Y_data.append(arr_timeslot9)
    Y_data.append(arr_timeslot10)
    Y_data.append(arr_timeslot11)
    Y_data.append(arr_timeslot12)
    Y_data.append(arr_timeslot13)
    Y_data.append(arr_timeslot14)
    Y_data.append(arr_timeslot15)
    Y_data.append(arr_timeslot16)
    Y_data.append(arr_timeslot17)
    Y_data.append(arr_timeslot18)

    X_train, X_test, y_train, y_test = load_data(X_data,Y_data)
    trans_matrix = test_lasso(X_train, X_test, y_train, y_test)
    show_heatmap(trans_matrix)
    count = show_net(trans_matrix)
    print(count)


