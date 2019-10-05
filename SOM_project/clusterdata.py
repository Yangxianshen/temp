#放入一个序列，并进行处理

class clusterdata():
	def __init__ (self,ids,color,seqStrings):
		self.ids=ids
		self.clustSeqs=self.getStrings(seqStrings)#获取字符串操作模块

	def getStrings(self, seqStrings):
		clustSeqs=[]
		for id in self.ids:
			clustSeqs.append(seqStrings[id])
		return clustSeqs
    

