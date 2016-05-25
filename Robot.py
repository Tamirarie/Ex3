
from random import randint

class Robot:
    def __init__(self,ID,RobotType,x,y):
    
        self._x = randint(0,1000)
        self._y = randint(0,1000)
    
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
    
    def makeMove(self):
        if(self._current == arena._PanelGRAY):
            