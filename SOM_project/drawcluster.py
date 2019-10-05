import numpy as np 
import matplotlib.mathtext as mt 
import matplotlib.pyplot as plt 
import matplotlib as mpl 

class drawCluster():
	def __init__ (self,row,col,mycolor,seqStrings=None):#类属性参数，在类中传入参数

		print("draw cluster",row,col,mycolor)
		print(seqStrings)
		filename="sequence"+str(row)+str(col)+".png"
		mpl.rc('image',origin='upper')#利用关键字参数对数值进行修改,生成图像的位置。
		parse=mt.MathTextParser('Bitmap')

		h=10
		w=20
		fig=plt.figure(figsize=(w,h),facecolor='w')#facecolor为背景颜色，w=white
		mydpi=200
		line=0
		for seq in seqStrings:
			print(seq)
			fsize=8
			rgba1,depth1=parse.to_rgba(seq,color=mycolor,fontsize=fsize,dpi=mydpi)#to_rgba用于16进制颜色之间转换
			x=10
			y=10+(22*line)
			fig.figimage(rgba1.astype(float)/255.,x,y)
			line+=1
		plt.savefig(filename,dpi=mydpi)



