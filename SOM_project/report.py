
class Report():
	def __init__ (self):
		print("report")

	def savetofile(self,docPath,iters,rows,cols,clusterid,myColorMap):
		f=open("C:/Users/13345/Desktop/Bioinformatics program/my_project/SOM_project/resultsOut.txt",'w')

		f.write(docPath +"\r\n")
		f.write("SOM iteations" + str(iters) +"\r\n")
		f.write("rows:"+str(rows)+"cols:"+str(cols)+"\r\n")

		f.write("Cluster IDs:\r\n")
		for id in clusterid:
			f.write(str(id)+"\r\n")

		f.write("colorMap:"+"\r\n")
		for color in myColorMap:
			f.write(str(color)+"\r\n")

		f.close()
		


