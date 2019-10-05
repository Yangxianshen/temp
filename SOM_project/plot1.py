import matplotlib as mpl 
import matplotlib.pyplot as plt 

class plot1():

	def __init__(self,rows,cols,mapcolors):
		w=10
		h=10
		self.mapcolors=mapcolors
		fig=plt.figure(figsize=(w,h),facecolor='w')
		xStart=0.05
		yStart=0.05
		dy=h/rows*0.09
		dx=w/cols*0.09

		rowlist=[]
		i=rows
		while i>0:
			rowlist.append(i-1)
			i-=1

		collist=[]
		i=cols
		while i>0:
			collist.append(i-1)
			i-=1

		numUnits=rows*cols

		colorid=0
		for col in collist:
			for row in rowlist:
				x=xStart+(col*dx)
				y=yStart+(row*dy)
				rect=[x,y,dx,dy]
				color=self.getColor(row,col,rows,cols)#获取颜色值
				#ax1=fig.add_axes(rect, xticklabels='', yticklabels='')#新增子图axisbg=color,
				ax1=fig.add_axes(rect,xticklabels='', yticklabels='')#子图的大小，如何添加一个加入颜色的函数

		fig.savefig("C:/Users/13345/Desktop/Bioinformatics program/my_project/SOM_project/mapcolor.png",dpi=300)
		plt.show()

	def colorPlot(self):
		return self.dataColors

	def getColor(self,row,col,rows,cols):
		for c in self.mapcolors:
			if c[0]==row and c[1]==col:
				return c[2]

		



		