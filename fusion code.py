# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:04:21 2022

@author: hossi
"""
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 12:45:07 2022

@author: hossi
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from mip import Model, xsum, BINARY,INTEGER,MINIMIZE,CBC,minimize
import openpyxl

df = pd.read_excel(r'C:\Users\hossi\Desktop\fusion.xlsx',  engine='openpyxl',sheet_name='Feuil1')

df['durée en j']=df['durée en j']*8
df['durée en j']=df['durée en j'].astype(int)
df
#n1,n2,n3,n4,n5,n6,n7,n8,n9=1,7,1,1,2,1,1,1,1
n1=int(input("Nombre chef de chantier est :")) # 1
n2=int(input("Nombre de boisseurs est : ")) # 7
n3=int(input("Nombre d'Electricien est : "))# 1
n4=int(input("Nombre de Grutiers est : "))# 1
n5=int(input("Nombre de manoeuvres est : "))# 2
n6=int(input("Nombre de Soudeur est : "))# 1
n7=int(input("Nombre de Topographes est : "))# 1
n8=int(input("Nombre de chef d'equipe est : "))# 1
n9=int(input("Nombre d'Animateur HSE est : "))# 1
n = len(df)

p=[0 for i in range(len(df)+2)]
p[0]=0
p[-1]=0
for i in range(1,len(df)+1):
  p[i]=df['durée en j'][i-1]
#print(p)

u=[0 for i in range(len(df)+2)]
u[0]=[0,0,0,0,0,0,0,0,0]
u[-1]=[0,0,0,0,0,0,0,0,0]
for i in range(1,len(df)+1):
  u[i]=[df['Chef de chantier'][i-1],df['Boiseurs'][i-1],df['Electricien'][i-1],df['Grutier'][i-1],df['Manœuvres'][i-1],df['Soudeur'][i-1],df['Topo'][i-1],df["Chef d'équipe"][i-1],df['Animateur HSE'][i-1]]
#print(u)

S=[[0,1],[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[9,10],[8,11],[11,12],[10,13],[13,14],[12,15],[15,16],[14,17],[16,17]]

c = [n1,n2,n3,n4,n5,n6,n7,n8,n9]

#B=max(sum(u[i][r]*p[i]/c[r] for i in range(len(p)))for r in range(len(c)))
#print(B)
#print(sum(p))
(R, J, T) = (range(len(c)), range(len(p)), range(sum(p)))

model = Model(sense=MINIMIZE, solver_name=CBC)

x = [[model.add_var(name="x({},{})".format(j, t),var_type=BINARY) for t in T] for j in J]

model.objective = minimize(xsum(t* x[n + 1][t] for t in T))

for j in J:
    model += (xsum(x[j][t] for t in T) == 1)

for (r, t) in product(R, T):
    model += xsum(u[j][r] * x[j][t2] for j in J for t2 in range(max(0, t - p[j] + 1), t + 1)) <= c[r]

for (j, s) in S:
    model += xsum(t * x[s][t] - t * x[j][t] for t in T) >= p[j]

#for ((i,j),t) in product(S, T):
#    model += (sum(x[j][t1] for t1 in range(1,t+p[i])) + sum(x[i][t2] for t2 in range(t,sum(p)))) <= 1

model.optimize(max_seconds=300)

print("Schedule: ")
print("Makespan = {}".format(model.objective_value))

for (j, t) in product(J, T):
    if x[j][t].x >= 0.99:
        print("Job {}: begins at t={} and finishes at t={}".format(j, t, t+p[j]))










