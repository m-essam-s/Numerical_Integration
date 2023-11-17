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
        val1, val2,Times  = 0, 0, 100000
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
    
    def __str__(self):
        I0=str(Numerical_Integration.Integrat_0(self))
        I1=str(Numerical_Integration.Integrat_1(self))
        T1=str(abs(((float(I0)-float(I1))/float(I0))*100))
        I2=str(Numerical_Integration.Integrat_2(self))
        T2=str(abs(((float(I0)-float(I2))/float(I0))*100))
        I3=str(Numerical_Integration.Integrat_3(self))
        T3=str(abs(((float(I0)-float(I3))/float(I0))*100))
        I4=str(Numerical_Integration.Integrat_4(self))
        T4=str(abs(((float(I0)-float(I4))/float(I0))*100))
        I5=str(Numerical_Integration.Integrat_5(self))
        T5=str(abs(((float(I0)-float(I5))/float(I0))*100))
        
        Result={"True Value                  |": I0,
                "Trapezoidal Rule            |": I1,
                "Simpson's 1/3 Rule          |": I2,
                "Simpson's 3/8 Rule          |": I3,
                "Compination 1/3 & 3/8 Rule  |": I4,
                "1/3 & 3/8 & 1/3 & 3/8 Rule  |": I5}
        T_V=   {"True Value                  |": f"0 %",
                "Trapezoidal Rule            |": f"{T1} %",
                "Simpson's 1/3 Rule          |": f"{T2} %",
                "Simpson's 3/8 Rule          |": f"{T3} %",
                "Compination 1/3 & 3/8 Rule  |": f"{T4} %",
                "1/3 & 3/8 & 1/3 & 3/8 Rule  |": f"{T5} %"}
        Table = pd.DataFrame({'Result            ': Result,
                                '|εₜ|                 ': T_V})
    
        return f"{Table}"
    
    def Graph(self):
        xAxisPoints=np.linspace(floor(self.LowerBound)-1,ceil(self.UpperBound)+1,100000)
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
    