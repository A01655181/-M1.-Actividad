# Agente piso, puede tener 2 estados sucio o limpio (boolean)

import mesa

class FloorAgent(mesa.Agent):
    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.dirty =  True
        self.id = "Floor"