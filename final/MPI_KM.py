from mpi4py import MPI
import numpy as np
from kmteste import solve
import time
import matplotlib.pyplot as plt
from database import data_pick


#inicia os dados para processamento paralelo
comm = MPI.COMM_WORLD
num_process = comm.Get_size()
rank = comm.Get_rank()
data1=data_pick()


#divide a database para cada processo
def divide_partes(l, n):    
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  

#chama o metodo para dividor os dados, e os emvia para outros processos
if rank==0:
    chunks=list(divide_partes(data1,243))
    chunks=np.insert(chunks,0,[0],axis = 0) 
    data=comm.scatter(chunks, root=0)


else:
    #cada processo realiza o kmeans p/ 1/3 dos dados
    chunks=[]
    data=comm.scatter(chunks, root=0)
    valor=solve(data,(len(data1)/3))


    #plota os graficos 
    if rank==1:
        plt.plot([0,0],[0,0] ,'rx')
        for x in range(len(valor)):
            if valor[x][2]==0:
                plt.plot(valor[x][0],valor[x][1] ,'ro')
            elif valor[x][2]==1:
                plt.plot(valor[x][0],valor[x][1] ,'go')
            else:
                plt.plot(valor[x][0],valor[x][1] ,'bo')
    elif rank==2:
        plt.plot([0,0],[0,0] ,'bx')
        for x in range(len(valor)):
            if valor[x][2]==1:
                plt.plot(valor[x][0],valor[x][1] ,'ro')
            elif valor[x][2]==0:
                plt.plot(valor[x][0],valor[x][1] ,'go')
            else:
                plt.plot(valor[x][0],valor[x][1] ,'bo')
    else:
        plt.plot([0,0],[0,0] ,'gx')
        for x in range(len(valor)):
            if valor[x][2]==1:
                plt.plot(valor[x][0],valor[x][1] ,'ro')
            elif valor[x][2]==0:
                plt.plot(valor[x][0],valor[x][1] ,'go')
            else:
                plt.plot(valor[x][0],valor[x][1] ,'bo')

plt.show()


