from sympy import * 
import numpy as np
import math
import random as r 
import time
x=Symbol('x')

#funcoes implementadas para serem integradas
def func1(x):
    return 4/(1+x**2)

def func2(x):
    return math.sqrt(x+math.sqrt(x))

def toroide(x,y,z):
    if x>=1 and y>=-3 and ((z**2)+(((x**2+y**2)**0.5)-3)**2) <=1:
        return True
    else:
        return False

#metodo para realizar a integracao
def integrate(func,n,x0,x1,y0=0,y1=0,z0=-1,z1=1,mode=0):
    tempo=time.time()
    if mode==0:
        if func==toroide:
            toroide_cont=0
            #gera trio de pontos aleatorios
            pontos_x=np.random.uniform(x0,x1,n)
            pontos_y=np.random.uniform(y0,y1,n)
            pontos_z=np.random.uniform(z0,z1,n)
            
            #verifica se pontos pertencem ao toroide
            for x,y,z in zip(pontos_x,pontos_y,pontos_z):  
                if toroide(x,y,z)==True:
                    toroide_cont = toroide_cont+1
                
            
            #calcula a porcentagem de pontos pertencentes ao toroide
            #em relacao ao total
            porcentagem_toroide=toroide_cont/float(n)
            v_cubo=float(x1-x0)*float(y1-y0)*float(z1-z0)
            #Calcula o volume do toride
            v_toroide=v_cubo*porcentagem_toroide
            
            #calcula o erro
            v_correto=22.0924
            erro=(abs(v_toroide-v_correto)/v_correto)
            print("Tempo para calculo =",time.time()-tempo,"s")
            print ("Volume calculado= ",v_toroide)
            print("Erro =",erro*100,"%")
            


        else:
            f=func
            Sf=0
            for x in range(n):
                #gera os pontos aleatorios
                x=r.uniform(x0,x1)
                #faz a soma dos valores de f(x)
                #para os pontos gerados
                Sf=Sf+f(x)
            #calcula o valor da integral
            Sm=Sf/n
            I=(x1-x0)*Sm
            print (I)

    #usado com MPI
    elif mode!=1:
        if func==toroide:
            #gera trio de pontos aleatorios
            pontos_x=np.random.uniform(x0,x1,n)
            pontos_y=np.random.uniform(y0,y1,n)
            pontos_z=np.random.uniform(z0,z1,n)
            toroide_cont=0
            #verifica se pontos pertencem ao toroide
            for x,y,z in zip(pontos_x,pontos_y,pontos_z):  
                if toroide(x,y,z)==True:
                    toroide_cont = toroide_cont+1
        #retorna quantidade de pontos pertencentes no toroide
        return (toroide_cont)

            
    
        


integrate(func1,1000000,0.0,1.0)
#integrate(toroide,100000,1.0,4.0,-3.0,4.0,-1.0,1.0)
