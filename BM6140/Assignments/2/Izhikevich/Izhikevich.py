# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 00:19:23 2020

@author: sachin
"""

import numpy as np
from matplotlib import pyplot as plt

class Izhikevich():
    
    parameters={'RS' : [0.02, 0.20, -65, 8.00],
                'IB' : [0.02, 0.20, -55, 4.00],
                'CH' : [0.02, 0.20, -50, 2.00],
                'FS' : [0.10, 0.20, -65, 2.00],
                'TC' : [0.02, 0.50, -65, 0.05],
                'RZ' : [0.10, 0.26, -65, 2.00],
                'LTS': [0.02, 0.25, -65, 2.00]}
    
    def __init__(self, spiking_class):
        self.a = self.parameters[spiking_class][0]
        self.b = self.parameters[spiking_class][1]
        self.c = self.parameters[spiking_class][2]
        self.d = self.parameters[spiking_class][3]

    def dv(self, u, v, I, dt):
        return dt*((0.04*v+5)*v + 140 - u + I)
    
    def du(self, u, v, I, dt):
        return self.a * (self.b*v - u) * dt
    
    def simulate(self, v0, Tstop, dt, Iapp):
        self.Iapp= Iapp
        V = np.array([v0])
        U = np.array([self.b*v0])
        T = np.arange(0, Tstop+dt, dt)
        freq=0
        for t in T[1:]:
            V = np.append(V, V[-1] + self.dv(U[-1], V[-1], Iapp, dt))
            U = np.append(U, U[-1] + self.du(U[-1], V[-2], Iapp, dt))
            if V[-1]>30:
                freq += 1
                V[-1] = self.c
                U[-1] += self.d
        return V, T, freq*1000 / Tstop
    
spiking_classes = ['RS','IB','CH','FS','TC','RZ']

for i in range(6):
    model = Izhikevich(spiking_classes[i])
    V,T,freq = model.simulate(-65, 200, 0.1, 5) # voltage vs Time simulation
    fig, a = plt.subplots(1,2, figsize=(19.20, 10.80))
    a[0].plot(T,V)
    a[0].set_xlabel('Time (ms)')
    a[0].set_ylabel('Membrane Potential (mV)')
    a[0].set_title("Spiking Class: {}".format(spiking_classes[i]))
    freqs=[]
    currents = [c for c in range(1, 50)]
    for iapp in currents:
        V,T,freq = model.simulate(-65,100,0.1, iapp)
        freqs.append(freq)
    a[1].plot(currents, freqs)
    a[1].set_xlabel('Applied Current(\u03BCA)')
    a[1].set_ylabel('Frequency (spikes/sec)')
    a[1].set_title('Firing Rate')
    plt.tight_layout()
    plt.savefig('{}.png'.format(spiking_classes[i]))
    
    
    
    
    
    
    
    
    
    