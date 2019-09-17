from mpi4py import MPI
import numpy
from mc import toroide, integrate
import time

#define os limites de integracao
x0 = 1
x1 = 4
y0 = -3
y1 = 4
z0 = -1
z1 = 1

comm = MPI.COMM_WORLD
num_process = comm.Get_size()
rank = comm.Get_rank()
   
#calcula os passos para subdivir os intervalos de integracao
passo_x = float(x1-x0)/float(num_process)
passo_y = float(y1-y0)/float(num_process)
passo_z = float(z1-z0)/float(num_process)

#calcula a integral
tempo=time.time()
mc2=integrate(toroide,int(100000 // num_process),1+(rank*passo_x),1+(rank*passo_x)+passo_x,-3+(rank*passo_y),-3+(rank*passo_y)+passo_y,-1+(rank*passo_z),-1+(rank*passo_z)+passo_z,2)
valor = comm.gather(mc2, root=0)
if rank==0:
    vf=0
    for x in range(len(valor)):
        vf=vf+valor[x]
    vf=(vf/100000)*42
    #calcula o erro
    v_correto=22.0924
    erro=(abs(vf-v_correto)/v_correto)
    print("Tempo para calculo =",time.time()-tempo,"s")
    print("Numero de processos =",num_process)
    print ("Volume calculado= ",vf)
    print("Erro =",erro*100,"%")
    



