class Block():
    def __init__(self,logo=0):
        self.logo=logo
        self.x=0
        self.y=0
        self.type=False#行人类型  向左走 向右走
        self.state=False#行人状态--暂定
        self.isInGrend=False #行人是否位于gauss影响范围内
        self.outGrend=False #离开gauss影响范围 的默认方向
        self.allInComeBySort={} #排序后的总收益
        self.allInCome={1:0.0,2:0.0,3:0.0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}#排序前的总收益
        self.nextNull={1:0.0,2:0.0,3:0.0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}#判断下一点是否为空 收益
        self.defineDirectionIncome={1:0.0,2:0.0,3:0.0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}#默认方向收益
        self.randomIncome= {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0}#随机方向收益
        self.wallIncome={1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0}#墙壁收益
        self.grendIncome={1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0}#梯度收益
