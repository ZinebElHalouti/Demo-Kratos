# -*- coding: utf-8 -*-
"""
Created on Sat May 21 12:45:07 2022

@author: hossi
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from mip import Model, xsum, BINARY,INTEGER,minimize
import openpyxl

df = pd.read_excel(r'C:\Users\hossi\Desktop\Fiche des tâches 3.xlsx',  engine='openpyxl',sheet_name='Feuil2')

df['durée en j']=np.ceil(df['durée en j'])
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

S=[[0,1],[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[7,10],[7,11],[7,12],[7,13],[7,14],[7,15],[7,16],[7,17],[7,18],[7,19],[7,20],[7,21],[7,22],[7,23],[7,24],[7,25],[7,26],[7,27],[7,28],[7,29],[7,30],[7,31],[7,32],[9,33],[10,33],[11,33],[12,34],[13,34],[14,34],[15,35],[16,35],[17,35],[18,36],[19,36],[20,36],[21,37],[22,37],[23,37],[24,38],[25,38],[26,38],[27,39],[28,39],[29,39],[30,40],[31,40],[32,40],[8,41],[8,42],[8,43],[8,44],[8,45],[8,46],[8,47],[8,48],[8,49],[8,50],[8,51],[8,52],[8,53],[8,54],[8,55],[8,56],[8,57],[8,58],[8,59],[8,60],[8,61],[8,62],[8,63],[8,64],[41,65],[42,65],[43,65],[44,66],[45,66],[46,66],[47,67],[48,67],[49,67],[50,68],[51,68],[52,68],[53,69],[54,69],[55,69],[56,70],[57,70],[58,70],[59,71],[60,71],[61,71],[62,72],[63,72],[64,72],[33,73],[34,73],[35,73],[36,73],[37,73],[38,73],[39,73],[40,73],[73,74],[65,75],[66,75],[67,75],[68,75],[69,75],[70,75],[71,75],[72,75],[75,76],[74,77],[76,77]]

c = [n1,n2,n3,n4,n5,n6,n7,n8,n9]

(R, J, T) = (range(len(c)), range(len(p)), range(sum(p)))

model = Model(sense='MIN')

x = [[model.add_var(name="x({},{})".format(j, t),var_type=BINARY) for t in T] for j in J]

model.objective = xsum(t* x[n + 1][t] for t in T)

for j in J:
    model += (xsum(x[j][t] for t in T) == 1)

for (r, t) in product(R, T):
    model += xsum(u[j][r] * x[j][t2] for j in J for t2 in range(max(0, t - p[j] + 1), t + 1)) <= c[r]

for (j, s) in S:
    model += xsum(t * x[s][t] - t * x[j][t] for t in T) >= p[j]

#for ((i,j),t) in product(S, T):
#    model += (sum(x[j][t1] for t1 in range(1,t+p[i])) + sum(x[i][t2] for t2 in range(t,sum(p)))) <= 1

model.optimize()

print("Schedule: ")
print("Makespan = {}".format(model.objective_value))

for (j, t) in product(J, T):
    if x[j][t].x >= 0.99:
        print("Job {}: begins at t={} and finishes at t={}".format(j, t, t+p[j]))











