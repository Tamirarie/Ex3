
from random import randint
from Arena import *

class Robot:
    def __init__(self,ID,RobotType,x,y):
    
        self._x = x
        self._y = y
    
        self._ID = ID
        self._RobotType = RobotType 
        self._battery = 100
        self._historyMoves = []
    
        ###setting the near env of robot
        self._current = [x,y]
        right = [x+1,y]
        left = [x-1,y]
        up = [x,y+1]
        down = [x,y-1]
    
        self._env = [self._current,up,left,down,right]
        self._msgRec = ''
        self._MSGhistory = []
        self._robotsDist = []
        self._time = 0
        self._RobotData = []
    
    def makeMove(self,Arena):
        if(Arena.ArenaMat[self._x][self._y] == Arena.WhitePanel):
            print("I am alive")
        elif (Arena.ArenaMat[self._x][self._y] == Arena.GrayPanel):
            print("I am losing battery!")
            
        elif (Arena.ArenaMat[self._x][self._y] == Arena.BlackPanel):
            print("I am dead")
            
a = Arena(10)
r = Robot(1,True,8,1)
r.makeMove(a)            