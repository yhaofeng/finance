import numpy as np
import pandas as pd
from scipy import linalg

class MeanVariance(object):
    def __init__(self,retruns):
        """returns:收益率数据"""
        self.returns = retruns

    #定义最小化方差函数
    def minVar(self,goalRet):
        conv = np.array(self.returns.con()) #计算收益率协方差
        mean = np.array(self.returns.con()) #计算收益率均值
        L1 = np.append(np.append(conv.swapaxes(0,1),[mean],0),[np.ones(len(mean))],0).swapaxes(0,1)
        L2 = list(np.ones(len(mean)))
        L2.extend([0,0])
        L3 = list(mean)
        L3.extend([0, 0])
        L4 = np.array([L2,L3])
        L = np.append(L1,L4,0)
        result = linalg.solve(L,np.append(np.zeros(len(mean)),[1,goalRet],0))
        return np.array([list(self.returns.columns),result[:-2]])
