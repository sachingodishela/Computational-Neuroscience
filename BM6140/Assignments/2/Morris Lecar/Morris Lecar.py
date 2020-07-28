# -*- coding: utf-8 -*-
"""
Spyder Editor
@author : Sachin Godishela
This is a temporary script file.
"""

import numpy as np
from matplotlib import pyplot as plt

## Parameters
class MorrisLecar:
    def __init__(self, bif):
        if(bif == 'Hopf'):
            self.phi = 0.04
            self.gCa = 4.4
            self.V3 = 2.0
            self.V4 = 30.0
            self.ECa = 120.0
        elif(bif == 'SNLC'):
            self.phi = 0.0067
            self.gCa = 4.0
            self.V3 = 12.0
            self.V4 = 17.4
            self.ECa = 120.0
        elif(bif=='Homoclinic'):
            self.phi = 0.23
            self.gCa = 4.0
            self.V3 = 12.0
            self.V4 = 17.4
            self.ECa = 120.
        else:
            raise "Not a bifurcation"
        self.EK = -84.0
        self.EL = -60.0
        self.gK = 8.0
        self.gL = 2.0
        self.V1 = -1.2
        self.V2 = 18.0
        self.CM = 20.0
    def simulate(self, V0, Tstop, Iapp, dt):
        self.Iapp = Iapp
        Vm = np.array([V0])
        T = np.arange(0, Tstop+dt, step=dt, dtype=float)
        N = np.array([self.nInf(V0)])
        count = 0
        for t in T[1:]:
            Vm_new = Vm[-1] + self.dV(Vm[-1], N[-1], dt)
            
            if(Vm_new >= 50 and Vm[-1]<50):
                count += 1
            Vm = np.append(Vm, Vm_new)
            N_new = N[-1] + self.dn(Vm[-2], N[-1], dt)
            N = np.append(N, N_new)
        return Vm, T, N, 1000*count/Tstop
        
    def mInf(self, V):
        return 0.5 * (1+np.tanh((V - self.V1)/self.V2))
    
    def tauN(self, V):
        return 1 /  np.cosh((V-self.V3)/(2*self.V4))
    
    def nInf(self, V):
        return 0.5 * (1 + np.tanh((V - self.V3)/self.V4))
        
    def dn(self, V, n, dt):
        return ((self.nInf(V) - n) / self.tauN(V)) * dt * self.phi
    
    def dV(self, V, n, dt):
        return dt * self.CM * (self.Iapp - self.gL*(V - self.EL) - n * self.gK * (V - self.EK) - self.gCa * self.mInf(V) * (V - self.ECa))

  
hopf_model = MorrisLecar('Hopf')
snlc_model = MorrisLecar('SNLC')

hopf_freqs= []
snlc_freqs=[]
iss = np.arange(30,120,1)
for i in iss:
    V, T, N, freq1 = hopf_model.simulate(-10, 100, i, 0.02)
    V, T, N, freq2 = snlc_model.simulate(-10, 100, i, 0.02)
    hopf_freqs.append(freq1)
    snlc_freqs.append(freq2)

plt.figure(figsize=(19.2, 10.8))
plt.plot(iss, hopf_freqs, 'r.', label='Hopf')
plt.title('Morris Lecar Model')
plt.xlabel('Applied Current')
plt.ylabel('Frequency')
plt.plot(iss, snlc_freqs, 'b.', label='SNLC')
plt.legend()
plt.savefig('MorrisLecar.png')
    

        
        
        
        
        
        
        
        