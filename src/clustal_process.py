#!/usr/bin/env python3
"""
@author: Shichao Yang
@date: 09.18.2019
"""
import Bio.AlignIO#用于操作aln文件读写的模块
import operator

def _clustal_process(inputfile):
	star_info=inputfile._star_info#比对序列的所有比对结果 包括. : *
	#print(star_info)
	record_one=str(inputfile._records[0].seq)#比对序列中第一个序列的所有序列信息
	#print(record_one)
	middle_entry_index = int(len( inputfile._records ) / 2 )#比对序列长度的一半
	common_sequence= []
	for x,character in enumerate( star_info ):#将一个可遍历的对象组合为一个索引序列，（0，star_info[0]）,(1,star_info[1])
		if character== '*':#如果是*号，则氨基酸完全一样，取谁的都无所谓，取中间更合理吗？
			common_sequence.append(inputfile._records[middle_entry_index].seq[x])#取中间比对序列的氨基酸
		elif character== ' ':#没有匹配到任何信息
			continue
		elif (character== '.') or (character == ':'):#对该列进行氨基酸数目统计，取数目最多的那个氨基酸
			char_count={} #该列氨基酸的一个统计字典，{氨基酸名字：数目}
			#print(char_count)
			for record in inputfile._records:#比对序列的循环
				if record.seq[x] in char_count:#寻找所有列中符合条件的氨基酸
					char_count[record.seq[x]] = char_count[record.seq[x]] + 1 
				else:
					char_count[record.seq[x]] = 1 #Initialize count
			#此时里面的key是一个函数，用于获取操作对象的值key（参数），则获取参数的索引为1的值
			#整体函数的意思是按照整体items的第二个索引值取最大值
			key = max( char_count.items(), key = operator.itemgetter( 1 ) )[0] #Hackery to get the highest value key from list
            common_sequence.append( key ) #None are going to agree, default to record_two 
            
        else:
            print( "Unknown character at point " + str( x ) + " in sequence." )
            print( "Character ASCII representation: " + str( ord( character ) ) )	

    print ( "Final common sequence: " )
    str_common_sequence = ''.join( common_sequence )
    print( str_common_sequence )
    print( "Sequence Length: " + str( len( str_common_sequence ) ) )

    return str_common_sequence

clustal_align_pol = Bio.AlignIO.read( "C:/Users/13345/Desktop/Bioinformatics program/my_project/clustalw/archival/withoutMoloney/pol_complete_woMoloney_seqs.aln", "clustal" )
clustal_align_env = Bio.AlignIO.read( "C:/Users/13345/Desktop/Bioinformatics program/my_project/clustalw/archival/withoutMoloney/env_complete_woMoloney_seqs.aln", "clustal" )
clustal_align_gag = Bio.AlignIO.read( "C:/Users/13345/Desktop/Bioinformatics program/my_project/clustalw/archival/withoutMoloney/gag_complete_woMoloney_seqs.aln", "clustal" )


outData = _clustal_process(clustal_align_pol)
f = open( "C:/Users/13345/Desktop/Bioinformatics program/my_project/src/common_protein_seq_POL.fasta", 'w' )
f.write( outData )
f.close()

outData = _clustal_process(clustal_align_gag)
f = open( "C:/Users/13345/Desktop/Bioinformatics program/my_project/src/common_protein_seq_GAG.fasta", 'w' )
f.write( outData )
f.close()

outData = _clustal_process(clustal_align_env)
f = open( "C:/Users/13345/Desktop/Bioinformatics program/my_project/src/common_protein_seq_ENV.fasta", 'w' )
f.write( outData )
f.close()



