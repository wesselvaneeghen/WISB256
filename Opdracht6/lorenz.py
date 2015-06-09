import math
import scipy.integrate
from math import ceil

class Lorenz():
    
    def __init__(self,lijst,sigma=10,rho=28,beta=(8/3)):
        self.s = sigma
        self.r = rho
        self.b = beta
        self.x = lijst[0]
        self.y = lijst[1]
        self.z = lijst[2]
        
    def solve(self,T,dt):
        a = int(math.ceil(T/dt)) #het aantal benodigde stappen van grootte dt om T tijd doorlopen
        tijd = [0]*a
        for i in range(a):
            tijd[i] = i*dt
        return scipy.integrate.odeint(self.lorenz,[self.x,self.y,self.z],tijd)
        
    def lorenz(self,lijst,T) :
        x=lijst[0]
        y=lijst[1]
        z=lijst[2]
        x_dot = self.s*(y-x)
        y_dot = x*(self.r-z)-y
        z_dot = x*y - self.b*z
        return [x_dot, y_dot, z_dot]
        