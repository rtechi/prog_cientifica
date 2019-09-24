
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from sympy import * 
import timeit
from database import data_pick

#metodo para resolucao 
def solve(data,q_pontos=729,q_centroides=3):
    q_pontos=int(q_pontos)
    q_centroides=q_centroides
    centroides=np.random.rand(q_centroides,2)
    centroides_n=np.random.rand(q_centroides,2)
    dst=np.empty(q_centroides)
    grupos=np.empty(q_pontos)
    dataf=np.random.rand(q_pontos,3)
    cont=0



    start = timeit.default_timer()

    #enquanto a variacao dos centroides nao diminuir, executa o loop
    while distance.euclidean(centroides[0],centroides_n[0]) + distance.euclidean(centroides[0],centroides_n[0]) + distance.euclidean(centroides[0],centroides_n[0])>=0.05:
        #atualiza os centoides
        centroides=centroides_n
        
        #determina a qual grupo pertence cada ponto
        for x in range(q_pontos):
            a=data[x]
            for y in range(q_centroides):
                b=centroides[y]
                dst[y] = distance.euclidean(a, b)
            seletor=np.where(dst==np.amin(dst))
            grupos[x]=seletor[0]
            dataf[x]=np.append(data[x],grupos[x])

        #manipulacao de dados para calcular novo centroide
        a=np.where(dataf==0)
        b=np.where(dataf==1)
        c=np.where(dataf==2)
        aux1=np.random.rand(len(a[0]),2)
        aux2=np.random.rand(len(b[0]),2)
        aux3=np.random.rand(len(c[0]),2)
        for x in range(len(a[0])):
            t=a[0][x]
            aux1[x][0]=dataf[t][0]
            aux1[x][1]=dataf[t][1]
        for x in range(len(b[0])):
            t=b[0][x]
            aux2[x][0]=dataf[t][0]
            aux2[x][1]=dataf[t][1]
        for x in range(len(c[0])):
            t=c[0][x]
            aux3[x][0]=dataf[t][0]
            aux3[x][1]=dataf[t][1]

        #calculo dos novos centroides para comparacao
        centro1=np.mean(aux1, axis=0)  
        centro2=np.mean(aux2, axis=0)  
        centro3=np.mean(aux3, axis=0)

        centroides_n[0]=centro1
        centroides_n[1]=centro2
        centroides_n[2]=centro3
        cont+=1
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    #plota os graficos 
    for x in range(len(dataf)):
            if dataf[x][2]==0:
                plt.plot(dataf[x][0],dataf[x][1] ,'ro')
            elif dataf[x][2]==1:
                plt.plot(dataf[x][0],dataf[x][1] ,'go')
            else:
                plt.plot(dataf[x][0],dataf[x][1] ,'bo')
    plt.show()

    return(dataf)
    
solve(data1)


