
class charClusterSingle():
	def __init__ (self,row,col,mycolors,clusterid,seqdate,ids):
		import numpy as np 
		import matplotlib.mathtext as mt 
		import matplotlib.pyplot as plt 
		import matplotlib

		self.mycolors=mycolors
		self.clusterid=clusterid
		self.seqdate=seqdate
		self.seqids=ids
		matplotlib.rc('image',origin='upper')
		parser=mt.MathTextParser('Bitmap')
		filename='sequence'+'row'+'col'+'.png'
		print(len(self.seqdate))
		h=10
		w=20
		fig=plt.figure(figsize=(w,h),facecolor='w')

		i=0
		line=0
		for seq in self.seqdate:
			if clusterid[i][0]==row and clusterid[i][1]==col:
				print(self.seqids[i])
				str=self.seqids[i]+' '
				for elem in seq:
					if elem != '-':
						str=str+elem

				c=self.getcolor(self.clusterid[i][0],self.clusterid[i][1])
				fsize=2
				rgba1, depth1 = parser.to_rgba(str, color=c, fontsize=fsize, dpi=300)
				x=10
				y=10+(10*line)
				fig.figimage(rgba1.astype(float)/255.,x,y)
				line+=1
			i+=1
		if line>0:
			print("save file")
			plt.savefig(filename,dpi=100)

	def getColor(self,row,col):
		for c in mapcolors:
			if c[0]==row and c[1]==col:
				return c[2]
				




		


