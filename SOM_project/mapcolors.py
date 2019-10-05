#调用色彩一般怎么调用
import math
class mapcolors() :
    #设定色彩度的集合
    def __init__ (self) :  
        
        self.colors1 = ['#FF3300', '#FF6600', '#FF9900', '#FFCC00',
                     '#FFFF00', '#CCFF00', '#99FF00', '#66FF00',
                     '#33FF00', '#00FF00', '#00FF33', '#00FF66']
        
        
        self.colors2 = ['#8B0A50','#473C8B', '#8A2BE2', '#483D8B', '#1874CD', '#53868B',
                      '#70DB93', '#20B2AA', '#7FFF00', '#FFF68F', '#FF7F00', '#FF4500']
        
        self.colors3 = ['#FF1199', '#FF0066', '#FF1133', '#FF0000',
                     '#FF3300', '#FF6600', '#FF9900', '#FFCC00',
                     '#FFFF00', '#CCFF00', '#99FF00', '#66FF00',
                     '#33FF00', '#00FF00', '#00FF33', '#00FF66',
                     '#00FF99', '#00FFCC', '#00FFFF', '#00CCFF',
                     '#0099FF', '#0066FF', '#0033FF', '#0000FF',
                     '#3300FF', '#6600FF', '#9900FF', '#FF00FF']
        
        
    #是怎样处理色彩的    
    def getColorMap(self, rows, cols):
        
        myColors = self.colors3#是一个color3的色彩集合
        numColors = len(myColors)#色彩个数为28个
        
        numUnits = rows*cols#图片的单元数
        
        #gap = numColors/numUnits#这是什么意思
        #print(gap)
        
        self.colormap = []
        colorid = 0
        #flag=0;
        #对图像进行色彩填充
        for i in range(0,rows):
            #print "row ", i
            for j in range(0, cols):
                if numColors>=numUnits:
                #print "col ", j
                #print "row", i, " col", j
                #print i, ",", j, " ", myColors[colorid]
                    #flag=1;
                    self.colormap.append([i, j, myColors[colorid]])           
                    colorid += 1#图像色彩填满，从最初的颜色号开始进行填充该怎样表达
                else:
                    f=numUnits/numColors
                    n=math.ceil(f)
                    
                    #if(flag==1):
                        #colorid=0;
                    self.colormap.append([i,j,myColors*n[colorid]])
                    colorid +=1
        
        return self.colormap
    
    
    def getColor(self, row, col):
        for c in self.colormap:
            print (c) 
            if c[0]== row and c[1]== col:#
                return c[2]
       
        
           
    
   

   

     
     
        