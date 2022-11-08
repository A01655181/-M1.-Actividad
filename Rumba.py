'''
Agente rumba, este representa una aspiradora inteligente. Tiene un id y el numero de pasos que ha realizado durante la simulacion.
Las funciones que posee, son 3 move, getPos y getStep. move se ocupa para mover al agente en 8 posibles direcciones, ademas eviita 
que estos realicen movientos fuera del grid que van a limpiar. getPos y getStep son funciones que obtienen la posicion actual del
agente, asi como el numero de movimientos que ha realzado.
''' 
import mesa

from Floor import FloorAgent

class RumbaAgent(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.id = "Rumba"
        self.numOfStep = 0
    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)

        print(self.pos)
        print(new_position)

        if(self.pos[0] == 0 and new_position[0] == 9):
            print("Nope")

        elif(self.pos[0] == 9 and new_position[0] == 0):
            print("Nope")

        elif(self.pos[1] == 0 and new_position[1] == 9):
            print("Nope")

        elif(self.pos[1] == 9 and new_position[1] == 0):
            print("Nope")
        
        else:
            self.model.grid.move_agent(self, new_position)
            self.numOfStep = self.numOfStep + 1
            
    def step(self):
        self.move()

    def getPos(self):
        return self.pos

    def getStep(self):
        return self.numOfStep
