import Data
class PeopleMove():
    def moveExit(self):
        pass
    def moveLeft(self,p):
        p.x=p.x-1
    def moveRight(self,p):
        p.x=p.x+1

def PeopleMove(p,direction):
    if direction==1:
        p.x=p.x-1
        p.y=p.y+1
    elif direction==2:
        p.y=p.y+1
    elif direction==3:
        p.x=p.x+1
        p.y=p.y+1
    elif direction==4:
        p.x=p.x-1
    elif direction==5:
        p.x=p.x
    elif direction==6:
        p.x=p.x+1
    elif direction==7:
        p.x=p.x-1
        p.y=p.y-1
    elif direction==8:
        p.y=p.y-1
    elif direction==9:
        p.x=p.x+1
        p.y=p.y-1


def chickOverAround(p,allPeople):
    if p.x<=0 or p.x>=Data.ROOM_M:
        # p.logo=Data.BasicData.LOGO_NULL
        allPeople.remove(p)


