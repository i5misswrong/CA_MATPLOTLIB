class Block():
    def __init__(self,logo=0):
        self.logo=logo
        self.x=0
        self.y=0
        self.type=False#行人类型  向左走 向右走 true left   false right
        self.state=False#行人状态--暂定
        self.isInGrend=0 #行人是否位于gauss影响范围内
        self.isSeeGauss=False # pedestrian see guass feil
        self.isNewDefine=0 #见过gauss后 沿梯度下降离开gauss后 沿着直线移动的默认方向
        self.allInComeBySort={} #排序后的总收益
        self.allInCome={1:0.0,2:0.0,3:0.0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}#排序前的总收益
        self.nextNull={1:0.0,2:0.0,3:0.0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}#判断下一点是否为空 收益
        self.defineDirectionIncome={1:0.0,2:0.0,3:0.0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}#默认方向收益
        self.newDefineDirectionIncome = {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0}#新的默认方向收益
        self.randomIncome= {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0}#随机方向收益
        self.wallIncome={1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0}#墙壁收益
        self.grendIncome={1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0}#梯度收益

        self.force=0#行人影响力
        self.obParameter=0#f(F/s^2)
        self.isObChange=False#f(F/s^2)-m'/m if>0.2 设为Ture

        self.debug=0#debug标记行人