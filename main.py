import numpy as np
class math():
    def __init__(self):
        self.ModA = 3.0
        self.ModB = 4.0
        self.ModC = 2.0
        self.ModD = 1.0
        self.ValA = 3.0
        self.ValB = 3.0
        self.ValH = 2.0
        
    def steps(self):
        tmp = []
        i = self.ValA
        while(i<=self.ValB):
            tmp.append(i)
            i = i + self.ValH
        return np.asarray(tmp)
    
    def FX(self, x):
        return self.ModA * x * x * x + self.ModB * x * x + self.ModC * x + self.ModD  
    
    def MetodaTrapezow(self):
        lSteps = self.steps()
        try:
            result = self.FX(lSteps[0]) + self.FX(lSteps[len(lSteps)-1])
        except:
            print("Po za granicami")
            return None
        
        result = result/2
        
        i=1
        while (i < len(lSteps) - 1):
            result = result + self.FX(lSteps[i])
            i = i + 1
            
        result = result * self.ValH
        return result
    
    def MetodaSimsona(self):
        lSteps = self.steps()
        
        if(lSteps % 2 != 1):
            return -1
        try:
            result = self.FX(lSteps[0]) + self.FX(lSteps[len(lSteps) - 1])
        except:
            print("Po za granicami")
            return None
        
        i = 1
        while(i<len(lSteps) - 1):
            if(i % 2 !=0):
                result = result + self.FX(lSteps[i]) * 4
            else:
                result = result + self.FX(lSteps[i]) * 2
                
        return self.ValH / 3.0 * result
    
    
obj = math()
print(f"Simson: {obj.MetodaSimsona()}")
print(f"Trapezow: {obj.MetodaTrapezow()}")
