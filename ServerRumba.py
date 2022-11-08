'''
Visualizacion de la simulacion, esta puede ser personalizada mediante los parametros: numero de celdas sucias, numero de agentes
rumba y numero de steps limite.
Graficacion de los resultados mediante el data collector de mesa. Se grafican el numero de celdas sucias y limitas, el numero de
movimientos totales realizados por los agentes y el porcentaje de de celdas sucias y limpias.
''' 
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from ModelRumba import RumbaModel

from mesa.visualization.modules import CanvasGrid, ChartModule

from mesa.visualization.UserParam import UserSettableParameter

NO_OF_CELLS = 10

PIXLES_X = 500

PIXLES_Y = 500

params = {
    "N": UserSettableParameter("slider", "Number of agentes", 1, 1, 10, 1, description= "Number of agents in the sim"),
    "N_Dirt": UserSettableParameter("slider", "Number of dirty cells", 2, 1, 100, 1, description= "Number of dirty cells in the sim"),
    "limit": UserSettableParameter("slider", "Limit of steps in the simulation", 100, 1, 500, 1, description= "Number of steps to stop the sim"),
    "width": NO_OF_CELLS,
    "height": NO_OF_CELLS,
}

def agentPortrayl(agent):
    portrayl = {"Shape": "circle", "Filled": "true", "r": 0.5}

    if agent.id == "Rumba":
        portrayl["Color"] = "black"
        portrayl["Layer"] = 1

    if agent.id == "Floor":
        if agent.dirty == True:
            portrayl["Color"] = "red"
            portrayl["Layer"] = 0
        
        else:
            portrayl["Color"] = "white"
            portrayl["Layer"] = 0
    
    return portrayl

grid = CanvasGrid(agentPortrayl, NO_OF_CELLS, NO_OF_CELLS, PIXLES_X, PIXLES_Y)

dataCurrents = ChartModule(
    [
        {"Label": "Cleaned Cells", "Color": "green"},
        {"Label": "Dirty Cells", "Color": "red"},
    ],
    canvas_height = 300,
    data_collector_name = "datacollector_currents",
)

dataCurrentsPor = ChartModule(
    [
        {"Label": "Cleaned Cells Porcentage", "Color": "green"},
        {"Label": "Dirty Cells Porcentage", "Color": "red"},
    ],
    canvas_height = 300,
    data_collector_name = "datacollector_currents",
)

dataCurrentsSteps = ChartModule(
    [
        {"Label": "Steps of agents", "Color": "blue"},
    ],
    canvas_height = 300,
    data_collector_name = "datacollector_currents",
)

server = ModularServer(RumbaModel, [grid, dataCurrents, dataCurrentsSteps, dataCurrentsPor], "Rumba Model", params)
server.port = 8521
server.launch()