# -*- coding: utf-8 -*-
"""RCSP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bS8RavOnq5HtKMf05K_E2ynU-uF7MW-h
"""

pip install mip

pip install pulp

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.ExcelFile('/content/Fiche des tâches 3.xlsx')
df = pd.read_excel(data, 'Feuil2')

df['durée en j']=df['durée en j']*8*6
df['durée en j']=df['durée en j'].astype(int)

21from itertools import product
from mip import Model, xsum, BINARY,INTEGER,minimize
#n1,n2,n3,n4,n5,n6,n7,n8,n9=1,7,1,1,2,1,1,1,1
n1=int(input("Nombre chef de chantier est :")) # 1
n2=int(input("Nombre de boisseurs est : ")) # 7
n3=int(input("Nombre d'Electricien est : "))# 1
n4=int(input("Nombre de Grutiers est :"))# 1
n5=int(input("Nombre de manoeuvres est :"))# 2
n6=int(input("Nombre de Soudeur est :"))# 1
n7=int(input("Nombre de Topographes est :"))# 1
n8=int(input("Nombre de chef d'equipe est :"))# 1
n9=int(input("Nombre d'Animateur HSE est :"))# 1
n = len(df)

p=[0 for i in range(len(df)+2)]
p[0]=0
p[-1]=0
for i in range(1,len(df)+1):
  p[i]=df['durée en j'][i-1]
print(p)

u=[0 for i in range(len(df)+2)]
u[0]=[0,0,0,0,0,0,0,0,0]
u[-1]=[0,0,0,0,0,0,0,0,0]
for i in range(1,len(df)+1):
  u[i]=[df['Chef de chantier'][i-1],df['Boiseurs'][i-1],df['Electricien'][i-1],df['Grutier'][i-1],df['Manœuvres'][i-1],df['Soudeur'][i-1],df['Topo'][i-1],df["Chef d'équipe"][i-1],df['Animateur HSE'][i-1]]
print(u)

S=[[0,1],[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[7,10],[7,11],[7,12],[7,13],[7,14],[7,15],[7,16],[7,17],[7,18],[7,19],[7,20],[7,21],[7,22],[7,23],[7,24],[7,25],[7,26],[7,27],[7,28],[7,29],[7,30],[7,31],[7,32],[9,33],[10,33],[11,33],[12,34],[13,34],[14,34],[15,35],[16,35],[17,35],[18,36],[19,36],[20,36],[21,37],[22,37],[23,37],[24,38],[25,38],[26,38],[27,39],[28,39],[29,39],[30,40],[31,40],[32,40],[8,41],[8,42],[8,43],[8,44],[8,45],[8,46],[8,47],[8,48],[8,49],[8,50],[8,51],[8,52],[8,53],[8,54],[8,55],[8,56],[8,57],[8,58],[8,59],[8,60],[8,61],[8,62],[8,63],[8,64],[41,65],[42,65],[43,65],[44,66],[45,66],[46,66],[47,67],[48,67],[49,67],[50,68],[51,68],[52,68],[53,69],[54,69],[55,69],[56,70],[57,70],[58,70],[59,71],[60,71],[61,71],[62,72],[63,72],[64,72],[33,73],[34,73],[35,73],[36,73],[37,73],[38,73],[39,73],[40,73],[73,74],[65,75],[66,75],[67,75],[68,75],[69,75],[70,75],[71,75],[72,75],[75,76],[74,77],[76,77]]

c = [n1,n2,n3,n4,n5,n6,n7,n8,n9]

R, J, T = range(len(c)), range(len(p)), range(sum(p))

model = Model()

x = [[model.add_var(name="x({},{})".format(j, t),var_type=BINARY) for t in T] for j in J]

model.objective = minimize(xsum(t * x[n + 1][t] for t in T))

for j in J:
    model += (xsum(x[j][t] for t in T) == 1)

for (r, t) in product(R, T):
    model += xsum(u[j][r] * x[j][t2] for j in J for t2 in range(max(0, t - p[j] + 1), t + 1)) <= c[r]

for (j, s) in S:
    model += xsum(t * x[s][t] - t * x[j][t] for t in T) >= p[j]

model.optimize()

print("Schedule: ")
print("Makespan = {}".format(model.objective_value))
for (j, t) in product(J, T):
    if x[j][t].x >= 0.99:
        print("Job {}: begins at t={} and finishes at t={}".format(j, t, t+p[j]))

#S=[[0,1],[0,2],[1,3],[2,4],[1,5],[3,5],[2,6],[4,6],[1,7],[3,7],[5,7],[2,8],[4,8],[6,8],[1,9],[3,9],[5,9],[7,9],[1,10],[3,10],[5,10],[7,10],[1,11],[3,11],[5,11],[7,11],[1,12],[3,12],[5,12],[7,12],[1,13],[3,13],[5,13],[7,13],[1,14],[3,14],[5,14],[7,14],[1,15],[3,15],[5,15],[7,15],[1,16],[3,16],[5,16],[7,16],[1,17],[3,17],[5,17],[7,17],[1,18],[3,18],[5,18],[7,18],[1,19],[3,19],[5,19],[7,19],[1,20],[3,20],[5,20],[7,20],[1,21],[3,21],[5,21],[7,21],[1,22],[3,22],[5,22],[7,22],[1,23],[3,23],[5,23],[7,23],[1,24],[3,24],[5,24],[7,24],[1,25],[3,25],[5,25],[7,25],[1,26],[3,26],[5,26],[7,26],[1,27],[3,27],[5,27],[7,27],[1,28],[3,28],[5,28],[7,28],[1,29],[3,29],[5,29],[7,29],[1,30],[3,30],[5,30],[7,30],[1,31],[3,31],[5,31],[7,31],[1,32],[3,32],[5,32],[7,32],[9,33],[10,33],[11,33],[12,34],[13,34],[14,34],[15,35],[16,35],[17,35],[18,36],[19,36],[20,36],[21,37],[22,37],[23,37],[24,38],[25,38],[26,38],[27,39],[28,39],[29,39],[30,40],[31,40],[32,40],[2,41],[4,41],[6,41],[8,41],[2,42],[4,42],[6,42],[8,42],[2,43],[4,43],[6,43],[8,43],[2,44],[4,44],[6,44],[8,44],[2,45],[4,45],[6,45],[8,45],[2,46],[4,46],[6,46],[8,46],[2,47],[4,47],[6,47],[8,47],[2,48],[4,48],[6,48],[8,48],[2,49],[4,49],[6,49],[8,49],[2,50],[4,50],[6,50],[8,50],[2,51],[4,51],[6,51],[8,51],[2,52],[4,52],[6,52],[8,52],[2,53],[4,53],[6,53],[8,53],[2,54],[4,54],[6,54],[8,54],[2,55],[4,55],[6,55],[8,55],[2,56],[4,56],[6,56],[8,56],[2,57],[4,57],[6,57],[8,57],[2,58],[4,58],[6,58],[8,58],[2,59],[4,59],[6,59],[8,59],[2,60],[4,60],[6,60],[8,60],[2,61],[4,61],[6,61],[8,61],[2,62],[4,62],[6,62],[8,62],[2,63],[4,63],[6,63],[8,63],[2,64],[4,64],[6,64],[8,64],[41,65],[42,65],[43,65],[44,66],[45,66],[46,66],[47,67],[48,67],[49,67],[50,68],[51,68],[52,68],[53,69],[54,69],[55,69],[56,70],[57,70],[58,70],[59,71],[60,71],[61,71],[62,72],[63,72],[64,72],[33,73],[34,73],[35,73],[36,73],[37,73],[38,73],[39,73],[40,73],[73,74],[65,75],[66,75],[67,75],[68,75],[69,75],[70,75],[71,75],[72,75],[75,76],[74,77],[76,77]]

#S=[["START","A"],["START","B"],["A","C"],["B","D"],["A","E"],["C","E"],["B","F"],["D","F"],["A","G"],["C","G"],["E","G"],["B","H"],["D","H"],["F","H"],["A","I"],["C","I"],["E","I"],["G","I"],["A","J"],["C","J"],["E","J"],["G","J"],["A","K"],["C","K"],["E","K"],["G","K"],["A","L"],["C","L"],["E","L"],["G","L"],["A","M"],["C","M"],["E","M"],["G","M"],["A","N"],["C","N"],["E","N"],["G","N"],["A","O"],["C","O"],["E","O"],["G","O"],["A","P"],["C","P"],["E","P"],["G","P"],["A","Q"],["C","Q"],["E","Q"],["G","Q"],["A","R"],["C","R"],["E","R"],["G","R"],["A","S"],["C","S"],["E","S"],["G","S"],["A","T"],["C","T"],["E","T"],["G","T"],["A","V"],["C","V"],["E","V"],["G","V"],["A","W"],["C","W"],["E","W"],["G","W"],["A","X"],["C","X"],["E","X"],["G","X"],["A","Y"],["C","Y"],["E","Y"],["G","Y"],["A","Z"],["C","Z"],["E","Z"],["G","Z"],["A","AA"],["C","AA"],["E","AA"],["G","AA"],["A","BB"],["C","BB"],["E","BB"],["G","BB"],["A","CC"],["C","CC"],["E","CC"],["G","CC"],["A","DD"],["C","DD"],["E","DD"],["G","DD"],["A","EE"],["C","EE"],["E","EE"],["G","EE"],["A","FF"],["C","FF"],["E","FF"],["G","FF"],["A","GG"],["C","GG"],["E","GG"],["G","GG"],["I","HH"],["J","HH"],["K","HH"],["L","II"],["M","II"],["N","II"],["O","JJ"],["P","JJ"],["Q","JJ"],["R","KK"],["S","KK"],["T","KK"],["V","LL"],["W","LL"],["X","LL"],["Y","MM"],["Z","MM"],["AA","MM"],["BB","NN"],["CC","NN"],["DD","NN"],["EE","OO"],["FF","OO"],["GG","OO"],["B","PP"],["D","PP"],["F","PP"],["H","PP"],["B","QQ"],["D","QQ"],["F","QQ"],["H","QQ"],["B","RR"],["D","RR"],["F","RR"],["H","RR"],["B","SS"],["D","SS"],["F","SS"],["H","SS"],["B","TT"],["D","TT"],["F","TT"],["H","TT"],["B","UU"],["D","UU"],["F","UU"],["H","UU"],["B","VV"],["D","VV"],["F","VV"],["H","VV"],["B","WW"],["D","WW"],["F","WW"],["H","WW"],["B","XX"],["D","XX"],["F","XX"],["H","XX"],["B","YY"],["D","YY"],["F","YY"],["H","YY"],["B","ZZ"],["D","ZZ"],["F","ZZ"],["H","ZZ"],["B","AAA"],["D","AAA"],["F","AAA"],["H","AAA"],["B","BBB"],["D","BBB"],["F","BBB"],["H","BBB"],["B","CCC"],["D","CCC"],["F","CCC"],["H","CCC"],["B","DDD"],["D","DDD"],["F","DDD"],["H","DDD"],["B","EEE"],["D","EEE"],["F","EEE"],["H","EEE"],["B","FFF"],["D","FFF"],["F","FFF"],["H","FFF"],["B","GGG"],["D","GGG"],["F","GGG"],["H","GGG"],["B","HHH"],["D","HHH"],["F","HHH"],["H","HHH"],["B","III"],["D","III"],["F","III"],["H","III"],["B","JJJ"],["D","JJJ"],["F","JJJ"],["H","JJJ"],["B","KKK"],["D","KKK"],["F","KKK"],["H","KKK"],["B","LLL"],["D","LLL"],["F","LLL"],["H","LLL"],["B","MMM"],["D","MMM"],["F","MMM"],["H","MMM"],["PP","NNN"],["QQ","NNN"],["RR","NNN"],["SS","OOO"],["TT","OOO"],["UU","OOO"],["VV","PPP"],["WW","PPP"],["XX","PPP"],["YY","QQQ"],["ZZ","QQQ"],["AAA","QQQ"],["BBB","RRR"],["CCC","RRR"],["DDD","RRR"],["EEE","SSS"],["FFF","SSS"],["GGG","SSS"],["HHH","TTT"],["III","TTT"],["JJJ","TTT"],["KKK","UUU"],["LLL","UUU"],["MMM","UUU"],["HH","VVV"],["II","VVV"],["JJ","VVV"],["KK","VVV"],["LL","VVV"],["MM","VVV"],["NN","VVV"],["OO","VVV"],["VVV","WWW"],["NNN","XXX"],["OOO","XXX"],["PPP","XXX"],["QQQ","XXX"],["RRR","XXX"],["SSS","XXX"],["TTT","XXX"],["UUU","XXX"],["XXX","YYY"],["WWW","END"],["YYY","END"]]

from itertools import product
from mip import Model, xsum, minimize, BINARY,INTEGER
n1=1
n2=1
n3=7
n4=2
n5=1
n6=1
n7=1
n8=1
n9=1

n = len(df)
p=[0 for i in range(len(df)+2)]
p[0]=0
p[-1]=0
for i in range(1,len(df)+1):
  p[i]=df['durée en j'][i-1]
print(p)
u=[0 for i in range(len(df)+2)]
u[0]=[0,0,0,0,0,0,0,0,0]
u[-1]=[0,0,0,0,0,0,0,0,0]
for i in range(1,len(df)+1):
  u[i]=[df['Chef de chantier'][i-1],df['Boiseurs'][i-1],df['Electricien'][i-1],df['Grutier'][i-1],df['Manœuvres'][i-1],df['Soudeur'][i-1],df['Topo'][i-1],df["Chef d'équipe"][i-1],df['Animateur HSE'][i-1]]
print(u)
S=[[0,1],[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[7,10],[7,11],[7,12],[7,13],[7,14],[7,15],[7,16],[7,17],[7,18],[7,19],[7,20],[7,21],[7,22],[7,23],[7,24],[7,25],[7,26],[7,27],[7,28],[7,29],[7,30],[7,31],[7,32],[9,33],[10,33],[11,33],[12,34],[13,34],[14,34],[15,35],[16,35],[17,35],[18,36],[19,36],[20,36],[21,37],[22,37],[23,37],[24,38],[25,38],[26,38],[27,39],[28,39],[29,39],[30,40],[31,40],[32,40],[8,41],[8,42],[8,43],[8,44],[8,45],[8,46],[8,47],[8,48],[8,49],[8,50],[8,51],[8,52],[8,53],[8,54],[8,55],[8,56],[8,57],[8,58],[8,59],[8,60],[8,61],[8,62],[8,63],[8,64],[41,65],[42,65],[43,65],[44,66],[45,66],[46,66],[47,67],[48,67],[49,67],[50,68],[51,68],[52,68],[53,69],[54,69],[55,69],[56,70],[57,70],[58,70],[59,71],[60,71],[61,71],[62,72],[63,72],[64,72],[33,73],[34,73],[35,73],[36,73],[37,73],[38,73],[39,73],[40,73],[73,74],[65,75],[66,75],[67,75],[68,75],[69,75],[70,75],[71,75],[72,75],[75,76],[74,77],[76,77]]
c = [n1,n3,n7,n8,n4,n6,n9,n2,n5]
(R, J, T) = (range(len(c)), range(len(p)), range(sum(p)))

model = Model(sense='MIN')

x = [[model.add_var(name="x({},{})".format(j, t), var_type=BINARY) for t in T] for j in J]
model.objective = minimize(xsum(t * x[n + 1][t] for t in T))

for j in J:
    model += xsum(x[j][t] for t in T) == 1

for (r, t) in product(R, T):
    model += (
        xsum(u[j][r] * x[j][t2] for j in J for t2 in range(max(0, t - p[j] + 1), t + 1))
        <= c[r])

for (j, s) in S:
    model += xsum(t * x[s][t] - t * x[j][t] for t in T) >= p[j]

model.optimize(max_seconds=10)

print("Schedule: ")
for (j, t) in product(J, T):
    if x[j][t].x >= 0.99:
        print("Job {}: begins at t={} and finishes at t={}".format(j, t, t+p[j]))
print("Makespan = {}".format(model.objective_value))

n1=int(input("Nombre chef de chantier est :")) # 1
n2=int(input("Nombre de boisseurs est : ")) # 7
n3=int(input("Nombre d'Electricien est : "))# 1
n4=int(input("Nombre de Grutiers est :"))# 1
n5=int(input("Nombre de manoeuvres est :"))# 2
n6=int(input("Nombre de Soudeur est :"))# 1
n7=int(input("Nombre de Topographes est :"))# 1
n8=int(input("Nombre de chef d'equipe est :"))# 1
n9=int(input("Nombre d'Animateur HSE est :"))# 1

import pulp as p
from itertools import product
from mip import Model, xsum, minimize, BINARY,INTEGER 
n1=1
n2=1
n3=7
n4=2
n5=1
n6=1
n7=1
n8=1
n9=1

n = len(df)

p=[0 for i in range(len(df))]
for i in range(len(df)):
  p[i]=df['durée en j'][i]
print(p)

u=[0 for i in range(len(df))]
u[0]=[0,0,0,0,0,0,0,0,0]
u[-1]=[0,0,0,0,0,0,0,0,0]
for i in range(len(df)):
  u[i]=[df['Chef de chantier'][i],df['Boiseurs'][i],df['Electricien'][i],df['Grutier'][i],df['Manœuvres'][i],df['Soudeur'][i],df['Topo'][i],df["Chef d'équipe"][i],df['Animateur HSE'][i]]
print(u)

S=[[0,1],[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[7,10],[7,11],[7,12],[7,13],[7,14],[7,15],[7,16],[7,17],[7,18],[7,19],[7,20],[7,21],[7,22],[7,23],[7,24],[7,25],[7,26],[7,27],[7,28],[7,29],[7,30],[7,31],[7,32],[9,33],[10,33],[11,33],[12,34],[13,34],[14,34],[15,35],[16,35],[17,35],[18,36],[19,36],[20,36],[21,37],[22,37],[23,37],[24,38],[25,38],[26,38],[27,39],[28,39],[29,39],[30,40],[31,40],[32,40],[8,41],[8,42],[8,43],[8,44],[8,45],[8,46],[8,47],[8,48],[8,49],[8,50],[8,51],[8,52],[8,53],[8,54],[8,55],[8,56],[8,57],[8,58],[8,59],[8,60],[8,61],[8,62],[8,63],[8,64],[41,65],[42,65],[43,65],[44,66],[45,66],[46,66],[47,67],[48,67],[49,67],[50,68],[51,68],[52,68],[53,69],[54,69],[55,69],[56,70],[57,70],[58,70],[59,71],[60,71],[61,71],[62,72],[63,72],[64,72],[33,73],[34,73],[35,73],[36,73],[37,73],[38,73],[39,73],[40,73],[73,74],[65,75],[66,75],[67,75],[68,75],[69,75],[70,75],[71,75],[72,75],[75,76],[74,77],[76,77]]

c = [n1,n3,n7,n8,n4,n6,n9,n2,n5]

(R, J, T) = (range(len(c)), np.arange(len(p)), np.arange(sum(p)))

model = p.LpProblem('Problem', p.LpMinimize)  
  
x =[[p.LpVariable(name="x({},{})".format(j, t)) for t in T] for j in J]
for j in J:
    model += xsum(x[j][t] for t in T) == 1

for (r, t) in product(R, T):
    model += xsum(u[j][r] * x[j][t2] for j in J for t2 in range(max(0, t - p[j] + 1), t + 1))<= c[r]

for (j, s) in S:
    model += xsum(t * x[s][t] - t * x[j][t] for t in T) >= p[j]

print(model) 
  
status = model.solve()   
print(p.LpStatus[status]) 
print(p.value(model.objective))