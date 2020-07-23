# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 18:00:41 2020

@author: Giovanni
"""

# Trabalho 1 - Pesquisa Operacional - Problema do Fluxo Máximo 

from ortools.linear_solver import pywraplp
from igraph import Graph
from igraph import plot 

def PFM():

    arquivo = open('instance7.txt','r')
    
    arcos = []
    indices = []
    file = arquivo.readlines()
    arquivo.close()

    numVertices = file[0] # Número de Vértices 
    numVertices = int(numVertices.split()[0])
    numArcos = int(file[1].split()[0]) # Número de Arcos 
    origem = file[2] # Vértice de origem
    origem = int(origem.split()[0])
    escoadouro = file[3] # Vértice Final 
    escoadouro = int(escoadouro.split()[0])
    #print(nVertices)
    #print(nArcos)
    #print(origem)
    #print(escoadouro)
    
    indices = [numVertices, numArcos, origem, escoadouro]

    arco_aux = file[4:]
    for i in arco_aux:
        arcos.append([int(s) for s in i.split() if s.isdigit()])
       
    solver = pywraplp.Solver('PFM', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING) 
        # Solver é passado como variável 
    
    entradaNo = [i[0] for i in arcos] 
    saidaNo = [j[1] for j in arcos] 
    capacidades = [c[2] for c in arcos] 

    numVertices = indices[0]
    numArcos = indices[1]
    varSolver=[] 
    rest=[] 
    
    #Criando as variáveis de cada arco para o solver
    cont = 0
    while(cont < numArcos):
        varSolver.append(solver.NumVar(0, capacidades[cont], str(cont+1)))
        cont+=1

    # Criação do arco de ligação entre o nó de origem e o nó escoadouro, com o custo infinito 
    varSolver.append(solver.NumVar(0, solver.infinity(), 'X'))
    
    # Restrições: 
    cont=2
    cont_aux = 0
    while(cont <= numVertices): 
        cont_aux = 0
        constraint = solver.Constraint(0, 0) # Limites 
        
        while(cont_aux < len(entradaNo)): # While de 0 até o final do array de inicio
            if(cont == entradaNo[cont_aux]):
                constraint.SetCoefficient(varSolver[cont_aux], 1)
            cont_aux+=1  
            
        cont_aux=0 # Reinicia para entrar no próximo while 
        
        while(cont_aux < len(saidaNo)):  # While de 0 até o final do array de saida
            if(cont == saidaNo[cont_aux]): 
                constraint.SetCoefficient(varSolver[cont_aux], -1) 
            cont_aux+=1 
            
        cont_aux=0 # Reinicia para entrar na próxima função 
        
        if(cont==numVertices): 
            constraint.SetCoefficient(varSolver[len(varSolver)-1], 1) 
            rest.append(constraint) # Adiciona a restrição na lista
            cont+=1  
        else:  
            cont+=1 
            rest.append(constraint) # Salva a restrição 
            del constraint  
            
    # Criação da Função Objetivo: 
    FO = solver.Objective()
    FO.SetCoefficient(varSolver[len(varSolver)-1], -1) # Z = -X
    FO.SetMinimization()

    solver.Solve() # Ativação do Solver 
    
    z = varSolver[len(varSolver)-1].solution_value() # Solução ótima
    print('Arcos =', solver.NumVariables())
    print('Restrições =', solver.NumConstraints())

    cont=0 
    while(cont < len(varSolver)): # Print do fluxo em cada arco 
        if(varSolver[cont].solution_value()!=0):
            if(varSolver[cont].name() != 'X'):
                print('Fluxo:', arcos[ int(varSolver[cont].name() )-1][0], '->' , arcos[ int(varSolver[cont].name() )-1][1])
            print(varSolver[cont].name(), '=', varSolver[cont].solution_value(), '-', varSolver[cont].ub())
        cont+=1
        
    print('Solução de Fluxo Ótimo =', z)
        
    ######################################################
    # Print do grafo
 
    #k=0 
    #while k < len(arcos)-1:
        #grafo = Graph(edges=[(arcos[k][0], arcos[k][1])], directed=True)
        #k+=1
    #plot(grafo, bbox = (300,300), edge_label = grafo.es['weight'])
    
    # Por algum motivo ao usar a função dentro desse algoritmo o resto do algoritmo não funciona direito
    # Os prints contidos no relatório foram feitos de um algoritmo paralelo a esse trecho aqui demonstrado

PFM()
