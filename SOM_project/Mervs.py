import Bio.Cluster#聚类算法模块
import charclusterSingle
import clusterdata
import clusters
import drawcluster
import mapcolors
import plot1
import report
import seqData
import numpy as np
import math

if __name__ =='__main__':
	#该序列是老鼠保守序列在基因库中的比对文件，目的是在其他物种中寻找内源逆转录病毒
	docPath="C:/Users/13345/Desktop/Bioinformatics program/my_project/SOM_project/psiBlast_POL_against_Mouse.aln"
	docPath="C:/Users/13345/Desktop/Bioinformatics program/my_project/SOM_project/psiBlast_GAG_against_Mouse.aln"
	docPath="C:/Users/13345/Desktop/Bioinformatics program/my_project/SOM_project/psiBlast_ENV_against_Mouse.aln"

	seqdata=seqData.seqData(docPath) #该函数使用AliognIO模块对文件进行格式操作，函数获取了比对序列的id，与序列列表集合
	encoded=seqdata.encode()#将每一个序列中的氨基酸ASCII化，并以每一个序列的值为一个列表，然后所有序列列表生成一个二维数组
	data=np.array(encoded)#array（）将列表[ [],[],[] ]转化为矩阵（[],[],[]）矩阵可以对 行 列 进行操作
	numIter=1
	rows=5
	cols=5
	#tree = Bio.Cluster.treecluster(data=sequences, mask=None, weight=None, transpose=0, method='m', dist='e', distancematrix=None)
	#聚类操作 用于聚类的输入为一个 n x m 的Python 数值矩阵 data。mask缺失数据矩阵，默认为none，weight权重矩阵，none表示所有矩阵使用相同权重
	#transpose选择使用data中的行 (transpose==0), 或者列 (transpose==1)来计算距离，dist选择距离函数，默认为'e',Euclidean 距离
	#nxgrid, nygrid (默认: 2, 1) 当Self-Organizing Map计算的时候，矩形的网格所包含的横向和纵向的格子
	#inittau用于SOM算法的参数 τ 的初始值。默认的 inittau 是0.02。niter (默认: 1 )迭代运行的次数。
	clusterid, celldata = Bio.Cluster.somcluster(data, mask=None, weight=None, transpose=0, nxgrid=cols, nygrid=rows, inittau=0.02, niter=numIter, dist='e')
	print(clusterid)
	#print(celldata)
#函数返回一个元组 (clusterid, celldata)
#clusterid:一个二维数组，行数同待聚类的元素数目相同。每行的内容对应着该元素在矩形SOM方格内 x 和 y 的坐标。
#celldata:格式为一个矩阵，如果是对行聚类，内容为 ( nxgrid , nygrid , 列数)，如果是对列聚类， 
#那么内容为 ( nxgrid , nygrid , 行数) 。矩阵中，坐标 [ix][iy] 对应的是该坐标的网格里的 基因表达数据的聚类中心的一维向量。
	cl=clusters.Clusters()#获取clusters模块中Cluster类的属性，生成一个多列表

	id=0
	for cluster in clusterid:#対生成的坐标点位进行循环
		cl.addToCluster(cluster[0],cluster[1],id)#向列表中添加比对序列id
		print(cluster)
		id +=1

	mc=mapcolors.mapcolors()#调用mapcolors类
	colors=mc.colors3#获取其中的色彩列表值
	myColorMap=mc.getColorMap(rows,cols) #获取坐标点，以及对应的色彩值，组成多维列表[ [i,j,color3[id]],...]
	print(myColorMap)

	seqStrings=seqdata.getStrings()#将比对序列变成 id + 序列  且已经去掉'-'的格式
	print(seqStrings)

	for i in range(0,rows):
		for j in range(0,cols):
			ids=cl.getClusterSeqIds(i,j)#获取所有id值

			color=mc.getColor(i,j)#通过坐标id获取颜色值

			cdata=clusterdata.clusterdata(ids,color,seqStrings)#获取去除'-'的比对序列
			fn=len(cdata.clustSeqs)#获取序列的长度
			print("cluster count:")
			print(fn)
			if len(cdata.clustSeqs) > 0:
				print("print")
				drawcluster.drawCluster(i, j, color, cdata.clustSeqs)#将比对的序列作图

	myplot=plot1.plot1(rows,cols,myColorMap)

	report=report.Report()
	report.savetofile(docPath, numIter, rows, cols, clusterid, myColorMap)#比对序列的显示方式

