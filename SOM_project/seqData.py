#
# Takes in a DNA sequence and ...
#一个筛选序列的函数
#import Bio
import Bio.AlignIO
#from Bio import SeqIO#可以使用该模块操作fasta文件，通过seq_record获取序列，seq_record.id
#from Bio.Seq import Seq

class seqData() :
    
    def __init__ (self, infile=None) : #类属性函数 ，创建的实例直接具有该属性    
        
        if infile :
            #alignment = Bio.AlignIO.read( "C:/Users/13345/Desktop/Bioinformatics program/寻找老鼠内源基因转录病毒/SOMproject/psiBlast_ENV_against_Mouse.aln", "clustal" )
            #alignment = Bio.AlignIO.read( "env_complete_seqs.aln", "clustal" )
            alignment = Bio.AlignIO.read(infile, "clustal")#使用AlignIO，clustal模式处理文件则序列将生成id列与序列列
            
            print (alignment)
            #seq_record是指生成的alignment的每一行的信息
            #获取序列id
            self.ids = [seq_record.id for seq_record in alignment]#获取aln文件中的序列名称
            print (self.ids)
            #获取比对序列，且将比对序列列表化
            self.seqs = [list(str(seq_record.seq)) for seq_record in alignment]
   
    
    def encode(self):
        self.encoded = []
 
        # convert chars to integers
        for seq in self.seqs:
            tmp = []
            for elem in seq:
                n = ord(str(elem))#该函数以字符为参数返回该字符的unicode值
                #通过unicode值来获取匹配对象，如果是‘-’字符，则n值为0
                #为什么非要获取ASCII值，而不是直接通过if函数来直接选择
                if n == 45: n = 0 # set empty "-" to be zero, to reduce it's effect in map
                tmp.append(n)#筛选出某个基因吗？
            self.encoded.append(tmp)#将比对序列值ASCII化或者unicode化，到底是哪个？n=45，控制字符为“-”
            
        return self.encoded
        print(self.encoded)
    
    def getStrings(self):
        
        tmp =[]
        
        i = 0
        for id in self.ids:#循环比对序列名称
            st = id
            st = st + " "#在序列名称后面加上空格
            #这个char和elem的表达方式怎么判断？
            for char in self.seqs[i]:#从第一行开始 循环每一个元素，以i值控制序列行
                if char is not "-":#如果序列行中不含‘-’，则序列名字后加上序列元素
                    st = st + char #表达形式为 id+" "+char
                
            
            tmp.append(st)
            i +=1
            
        return tmp
            
            
        
             


   

     
     
        