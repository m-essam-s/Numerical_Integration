import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import *

class Numerical_Integration:
    def __init__(self, F, LB, UB):
        self.Function = F
        self.LowerBound = LB
        self.UpperBound = UB
        self.StepSize = UB - LB

    def f(self, x):
        return eval(self.Function, {'x': x, 'np': np})
        
    def Integrat_0(self): #---> Exact Solution
        val1, val2,Times  = 0, 0, 10000
        for n in range(1, Times + 1):
            val1 += self.f(self.LowerBound + ((n - 1/2) * ((self.StepSize) / Times)))
        val2 = ((self.StepSize) / Times) * val1
        return val2
    
    def Integrat_1(self): #---> Trapezoidal Rule
        I=(1/2)*(self.StepSize)*(self.f(self.LowerBound)+self.f(self.UpperBound))
        return I
    
    def Integrat_2(self): #---> Simpson's 1/3 Rule
        I=(1/6)*(self.StepSize)*(self.f(self.LowerBound)+4*self.f((self.StepSize)/2)+self.f(self.UpperBound))
        return I
    
    def Integrat_3(self): #---> Simpson's 3/8 Rule
        I=(1/8)*(self.StepSize)*(self.f(self.LowerBound)+3*self.f((self.StepSize/3))+3*self.f(2*(self.StepSize/3))+self.f(self.UpperBound))
        return I
    
    def Integrat_4(self): #---> Compination Simpson's 1/3 Rule & 3/8 Rule
        I1=((1/6)*((2*(self.StepSize/5))-self.LowerBound)*(self.f(self.LowerBound)+4*self.f(self.StepSize/5)+self.f(2*(self.StepSize/5))))
        I2=((1/8)*(self.UpperBound-(2*(self.StepSize/5)))*(self.f(2*(self.StepSize/5))+3*self.f(3*(self.StepSize/5))+3*self.f(4*(self.StepSize/5))+self.f(self.UpperBound)))
        T=I1+I2
        return T
    
    def Integrat_5(self): #---> Simpson's 1/3 Rule & 3/8 Rule & 1/3 Rule & 3/8 Rule     
        I1=((1/6)*((2*(self.StepSize/10))-self.LowerBound)*(self.f(self.LowerBound)+4*self.f(1*(self.StepSize/10))+self.f(2*(self.StepSize/10))))
        I2=((1/8)*((5*(self.StepSize/10))-(2*(self.StepSize/10)))*(self.f(2*(self.StepSize/10))+3*self.f(3*(self.StepSize/10))+3*self.f(4*(self.StepSize/10))+self.f(5*(self.StepSize/10))))
        I3=((1/6)*((7*(self.StepSize/10))-(5*(self.StepSize/10)))*(self.f(5*(self.StepSize/10))+4*self.f(6*(self.StepSize/10))+self.f(7*(self.StepSize/10))))
        I4=((1/8)*((self.UpperBound)-(7*(self.StepSize/10)))*(self.f(7*(self.StepSize/10))+3*self.f(9*(self.StepSize/10))+3*self.f(8*(self.StepSize/10))+self.f((self.UpperBound))))
        T=I1+I2+I3+I4
        return T
    def err (self, x):    #---> Error Percentage
        T = str(abs(((float(str(self.Integrat_0()))-float(x))/float(str(self.Integrat_0())))*100))
        return T
    
    def __str__(self):
        Result={"True Value                  |": str(self.Integrat_0()),
                "Trapezoidal Rule            |": str(self.Integrat_1()),
                "Simpson's 1/3 Rule          |": str(self.Integrat_2()),
                "Simpson's 3/8 Rule          |": str(self.Integrat_3()),
                "Compination 1/3 & 3/8 Rule  |": str(self.Integrat_4()),
                "1/3 & 3/8 & 1/3 & 3/8 Rule  |": str(self.Integrat_5())}
        T_V=   {"True Value                  |": f"0 %",
                "Trapezoidal Rule            |": f"{self.err(self.Integrat_1())} %",
                "Simpson's 1/3 Rule          |": f"{self.err(self.Integrat_2())} %",
                "Simpson's 3/8 Rule          |": f"{self.err(self.Integrat_3())} %",
                "Compination 1/3 & 3/8 Rule  |": f"{self.err(self.Integrat_4())} %",
                "1/3 & 3/8 & 1/3 & 3/8 Rule  |": f"{self.err(self.Integrat_5())} %"}
        Table = pd.DataFrame({'Results ': Result,'|εₜ| ': T_V})
    
        return f"{Table}"
    
    def Graph(self):
        xAxisPoints=np.linspace(floor(self.LowerBound),ceil(self.UpperBound),10000)
        yAxisPoints=self.f(xAxisPoints)
        ax = plt.gca()
        section = np.arange(self.LowerBound,self.UpperBound, 1/1000.)
        ax.plot(xAxisPoints, yAxisPoints)
        plt.style.use('ggplot')
        plt.title('Graph Representation')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.fill_between(section,self.f(section),color="cyan")
        plt.show()
        
    '''"test (0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5)))", 0.2, 0.8'''    
if __name__=='__main__':
    Function=input("F(X) =  ")
    LowerBound=eval(input("Lower bound = "))
    UpperBound=eval(input("Upper bound = "))
    Calc = Numerical_Integration(Function, LowerBound, UpperBound)
    print(Calc)
    Calc.Graph()
    