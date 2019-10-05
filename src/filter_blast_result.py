#!/usr/bin/env python3
"""
@author: Shichao Yang
@date: 09.18.2019

Filter and reduce the BLAST results for ClustalW
"""

from Bio.Blast import NCBIXML#处理XML文件中的blast结果
import logging
#import sys 该模块也可以进行输将输出存入文件

def filter_results(records):#主要是从xml文件中获取想要的所有信息，然后列表化
	filblast_alignments=[]
	for index in records.alignments:#alignment获取的是hit_id,hit_def,hit-length三个信息（使用print(index)只打印出这三个信息）,以及hsp的信息
	#alignments 下面有三个信息： title、 length、 hsps，分别对应数据库中匹配上的序列的标题、匹配的长度
    #其中 hsps 是 list 格式的对象，里面储存了 query 和数据库中序列匹配的具体信息，包括匹配得分、 gap 等信息，
		print(index)
		actionStr=index.hit_def.lower()#将标题输出小写化，这样在检索时可以不用区分大小写。
		if "predicted" in actionStr:#预测
			logging.debug("Filter items:"+actionStr)
		elif "unnamed" in actionStr:#未命名
			logging.debug("Filter items:"+actionStr)
		elif "novel" in actionStr:#与众不同
			logging.debug("Filter items:"+actionStr)
		elif "unknown" in actionStr:#未知
			logging.debug("Filter items:"+actionStr)
		else :
			filblast_alignments.append(index)#过去到匹配的alignment信息
	logging.info("Blast records remaining:"+str(len(filblast_alignments)))
	return filblast_alignments


def parse_alignment(outfile,records):#将获取到的信息，选择性的存入到fasta格式的文件中，并指定输出内容
	i=0
	for item in records:#函数已经生成了列表化的数据，对列表信息进行遍历
		logging.info("squence="+str(i)+"is")
		logging.info(item)
		title=item.hit_def[:]
		print('>'+item.hit_id+title+str(i),file=outfile)
		matchsquence=item.hsps[0]#hsps[0]是所在item存储信息的整体
		print(matchsquence.sbjct[:],file=outfile)#sbjct表示blast后的序列，query是指提交的序列，依然是从xml文件中获得
		i=i+1
	return
#filename指定日志的输出文件名 filemode指定日志文件的打开模式，只有指定filename后才有效 level：指定日志级别。degug为最高级别 format：配置日志输出格式 datefmt：配置输出时间格式
logging.basicConfig( filename = "process_blast_results.log", filemode = 'w', level = logging.DEBUG, format = '%(asctime)s %(levelname)-8s %(message)s', datefmt = '%Y-%m-%d %H:%M:%S', )

handleXML=open("C:/Users/13345/Desktop/Bioinformatics program/my_project/blast_result/ENV_against_Mouse_DXMPZXG801N-Alignment.xml")
blast_records=NCBIXML.read(handleXML)
logging.info("Blast records read")

local_alignments=filter_results(blast_records)
#sys.stdout=
clustalw_dump=open( "C:/Users/13345/Desktop/Bioinformatics program/my_project/clustalw/psiBlast_ENV_against_Mouse.fasta", 'w')
parse_alignment(clustalw_dump,local_alignments)
clustalw_dump.close()

handleXML=open("C:/Users/13345/Desktop/Bioinformatics program/my_project/blast_result/GAG_against_Mouse_DXN1H0HK01S-Alignment.xml")
blast_records=NCBIXML.read(handleXML)
logging.info("Blast records read")

local_alignments=filter_results(blast_records)
clustalw_dump=open( "C:/Users/13345/Desktop/Bioinformatics program/my_project/clustalw/psiBlast_GAG_against_Mouse.fasta", 'w')
parse_alignment(clustalw_dump,local_alignments)
clustalw_dump.close()

handleXML=open("C:/Users/13345/Desktop/Bioinformatics program/my_project/blast_result/POL_against_Mouse_DXNAPD5101N-Alignment.xml")
blast_records=NCBIXML.read(handleXML)
logging.info("Blast records read")

local_alignments=filter_results(blast_records)
clustalw_dump=open( "C:/Users/13345/Desktop/Bioinformatics program/my_project/clustalw/psiBlast_POL_against_Mouse.fasta", 'w')
parse_alignment(clustalw_dump,local_alignments)
clustalw_dump.close()