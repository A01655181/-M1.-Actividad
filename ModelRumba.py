'''
Agente rumba, este representa una aspiradora inteligente. Tiene un id y el numero de pasos que ha realizado durante la simulacion.
Las funciones que posee, son 3 move, getPos y getStep. move se ocupa para mover al agente en 8 posibles direcciones, ademas eviita 
que estos realicen movientos fuera del grid que van a limpiar. getPos y getStep son funciones que obtienen la posicion actual del
agente, asi como el numero de movimientos que ha realzado.
''' 
import mesa
from Rumba import RumbaAgent
from Floor import FloorAgent
from mesa.datacollection import DataCollector

class RumbaModel(mesa.Model):

    def __init__(self, N, N_Dirt, limit, width, height):
        self.num_agents = N
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.cond = limit
        self.currentStep = 0
        self.dirtyCells = N_Dirt
        self.agentsFPos = []
        self.agentsF ={}
        self.running = True

        self.datacollector_currents = DataCollector(
            {
                "Cleaned Cells": RumbaModel.current_CleanCells,
                "Dirty Cells": RumbaModel.current_DirtyCells,
                "Cleaned Cells Porcentage": RumbaModel.cleanCellsPorcentage,
                "Dirty Cells Porcentage": RumbaModel.dirtyCellsPorcentage,
                "Steps of agents": RumbaModel.calculateStepOfAgent,
            }
        )

        # Create agents
        for i in range(self.num_agents):
            n = i
            a = RumbaAgent(i, self)
            self.schedule.add(a)
            x = 1
            y = 1
            self.grid.place_agent(a, (x, y))
            n = n + 1
        
        for i in range(N_Dirt):
            a = FloorAgent(n, self)
            self.schedule.add(a)
            while(True):
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                if (x,y) not in self.agentsFPos:
                    self.grid.place_agent(a, (x, y))
                    self.agentsFPos.append((x,y))
                    self.agentsF[(x,y)] = n
                    n = n + 1
                    break
        



    def step(self):
        self.schedule.step()
        self.currentStep = self.currentStep + 1

        if(self.currentStep == self.cond):
            self.running = False
        
        else:

            for agent in self.schedule.agents:
                if agent.id == "Rumba":
                    if agent.getPos() in self.agentsFPos:
                        print("Let's clean")
                        self.schedule.agents[self.agentsF[agent.getPos()]].dirty = False
                        self.agentsFPos.remove(agent.getPos())
            
            if len(self.agentsFPos) == 0:
                self.running = False

        self.datacollector_currents.collect(self)       

    @staticmethod  
    def current_DirtyCells(model) -> int:
        
        dirtyCells = 0

        for agent in model.schedule.agents:
            if agent.id == "Floor":
                if agent.dirty == True:
                    dirtyCells = dirtyCells + 1

        return dirtyCells
    
    @staticmethod
    def dirtyCellsPorcentage(model) -> int:
        
        dirtyCells = 0

        for agent in model.schedule.agents:
            if agent.id == "Floor":
                if agent.dirty == True:
                    dirtyCells = dirtyCells + 1
                    
        porcentage = dirtyCells * 100
        porcentage = porcentage / model.dirtyCells

        return porcentage


    @staticmethod
    def current_CleanCells(model) -> int:
        
        cleanCells = 0

        for agent in model.schedule.agents:
            if agent.id == "Floor":
                if agent.dirty == False:
                    cleanCells = cleanCells + 1

        return cleanCells

    @staticmethod
    def cleanCellsPorcentage(model) -> int:
        
        porcentage = 100 - model.dirtyCellsPorcentage(model)

        return porcentage

    @staticmethod
    def calculateStepOfAgent(model) -> int:

        steps = 0
        
        for agent in model.schedule.agents:
            if agent.id == "Rumba":
                steps = steps + agent.getStep()

        return steps 
        
                    
                
    
