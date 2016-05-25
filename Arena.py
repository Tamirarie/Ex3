
import numpy
from random import randint

class Arena:
    def __init__(self,ArenaSize):
        
        self.BlackPanel = -3
        self.GrayPanel = -2
        self.WhitePanel = -1
                
        self.ArenaPanel = []
        self.ArenaMat = numpy.full((ArenaSize,ArenaSize),self.WhitePanel,dtype=int)
        
        
        
        for i in range (ArenaSize):
            self.ArenaMat[0][i] = self.BlackPanel
            self.ArenaMat[i][0] = self.BlackPanel
            self.ArenaMat[ArenaSize-1][i] = self.BlackPanel
            self.ArenaMat[i][ArenaSize-1] = self.BlackPanel            
        
        
        for i in range(1,ArenaSize-1):
            rand = randint(1,ArenaSize-2)
            self.ArenaMat[i][rand] = self.GrayPanel
        
        print(self.ArenaMat)
        
        