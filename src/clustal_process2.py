#!/usr/bin/env python3
"""
@author: Shichao Yang
@date: 09.18.2019
"""
#生成的dnd文件是树状图文件，可以通过biopython中子库读取

import Bio.AlignIO#用于操作aln文件读写的模块
import operator
#对aln格式是怎样处理的
def _clustal_process( inputFile ):#对比对序列aln格式的处理,内部属性函数
    star_info = inputFile._star_info#比对的所有符号信息，包括  . : *                       
    #print(star_info)
    record_one = str( inputFile._records[0].seq ) #比对序列中第一个序列的所有序列信息
    #print(record_one)
    middle_entry_index = int( len( inputFile._records ) / 2 )#比对序列个数的一半
    common_sequence = []
    for x, character in enumerate( star_info ):#将一个可遍历的对象组合为一个索引序列（0，star_info[0]）,(1,star_info[1])
        if character == '*':#如果是*号，则氨基酸完全一样，取谁的都无所谓，取中间更合理吗？
            common_sequence.append( inputFile._records[middle_entry_index].seq[x] )#这个感觉取哪个都一样，为什么非要取中间的呢
        elif character == ' ': continue #Nothing matching properly
        elif ( character == '.' ) or ( character == ':' ):#对该列进行氨基酸数目统计，取数目最多的那个氨基酸
            char_count = {}#该列氨基酸的一个统计字典，{氨基酸名字：数目}
            for record in ( inputFile._records ):
                if record.seq[x] in char_count:#寻找所有列中符合条件的氨基酸
                    char_count[record.seq[x]] = char_count[record.seq[x]] + 1 #Increment count
                else:
                    char_count[record.seq[x]] = 1 #Initialize count
            #python2中还是用iteritems（）python3中直接使用items（）
            #Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组
            #此时里面的key是一个函数，用于获取操作对象的值key（参数），则获取参数的索引为1的值
            #整体函数的意思是按照整体items的第二个索引值取最大值
            #print(char_count)
            #itemgetter获取对象位置数据，它是一个函数，比较数值列的数值，然后获取数量最多的那个氨基酸
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

#对aln文件的读取.要考虑模块对文件是进行的什么格式的处理
clustal_align_pol = Bio.AlignIO.read( "C:/Users/13345/Desktop/Bioinformatics program/my_project/clustalw/archival/withoutMoloney/pol_complete_woMoloney_seqs.aln", "clustal" )
clustal_align_env = Bio.AlignIO.read( "C:/Users/13345/Desktop/Bioinformatics program/my_project/clustalw/archival/withoutMoloney/env_complete_woMoloney_seqs.aln", "clustal" )
clustal_align_gag = Bio.AlignIO.read( "C:/Users/13345/Desktop/Bioinformatics program/my_project/clustalw/archival/withoutMoloney/gag_complete_woMoloney_seqs.aln", "clustal" )


#对比对的aln文件进行处理之后转换为fasta格式
#为什么要把aln格式转换为fasta格式，并对aln格式进行处理？
#将氨基酸序列拿到
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
