import math 
import networkx as nx #graphs
import folium #Biblioteca de mapas simples
import webbrowser #Pagina WEB - automotiza abertura de URLs

class Cidade:
    def __init__(self,nome,coordenada):
        self.nome = nome
        self.coordenada = coordenada

#Implementar uma Heuristica para o problema do caminho
def heuristica (cidade_atual,cidade_destino):
    #Obter as cooredenadas das cidade atual e destino
    lat1,long1 = cidade_atual.coordenada
    lat2,long2 = cidade_destino.coordenada
    #calcular a distancia euclidiana entre as coordenadas
    distancia = math.sqrt((lat1-lat2)**2 +(long1-long2)**2)
    return distancia

#Criar um graph 
Arad = Cidade('Arad',(46.1667, 21.3167))
Zerind = Cidade('Zerind',(46.6225, 21.5175))
Timesoara = Cidade('Timesoara',(45.7489, 21.2087))
Lugoj = Cidade('Lugoj',(45.6904, 21.9033))
Mehadia = Cidade('Mehadia', (44.9000, 22.3500))
Dobreta = Cidade('Dobreta',(44.7500, 22.3500))
Craiova = Cidade('Craiova',(44.3167, 23.8000))
Rimnicu_vilcea = Cidade('Rimnicu_vilcea',(45.1047, 24.3750))
Pintesti = Cidade('Pintesti',(44.8563, 24.8696))
Bucarest = Cidade('Bucarest',(44.4323, 26.1063))
Sibiu = Cidade('Sibiu',(45.8035, 24.1450))
Fagaras = Cidade('Fagaras',(45.8416, 24.9731))
Oradea = Cidade('Oradea',(47.0485, 21.9189))

#Criar suas conexões 
graph = nx.Graph()
graph.add_edge(Arad,Zerind,weight = 75)
graph.add_edge(Arad,Timesoara,weight = 118)
graph.add_edge(Arad,Sibiu,weight = 140)
graph.add_edge(Zerind,Oradea,weight = 71)
graph.add_edge(Timesoara,Lugoj,weight = 111)
graph.add_edge(Lugoj,Mehadia,weight = 70)
graph.add_edge(Mehadia,Dobreta,weight = 75)
graph.add_edge(Arad,Zerind,weight = 75)
graph.add_edge(Dobreta,Craiova,weight = 120)
graph.add_edge(Craiova,Rimnicu_vilcea,weight = 146)
graph.add_edge(Rimnicu_vilcea,Sibiu,weight = 80)
graph.add_edge(Rimnicu_vilcea,Pintesti,weight = 97)
graph.add_edge(Sibiu,Fagaras,weight = 99)
graph.add_edge(Fagaras,Bucarest,weight = 211)
graph.add_edge(Pintesti,Bucarest,weight = 101)
graph.add_edge(Craiova,Pintesti,weight = 138)

caminho = nx.astar_path(graph, Arad, Bucarest, heuristic=heuristica, weight='weight')

print("Shorest path", Arad.nome, "to", Bucarest.nome)
print("Shorest path", Arad.coordenada, "to", Bucarest.coordenada)
print([Cidade.nome for Cidade in caminho])
print(heuristica(Arad,Bucarest))

mapa = folium.Map(location=[44.8563, 24.8696], zoom_start=7)
for Cidade in graph:
    folium.Marker(location=[Cidade.coordenada[0], Cidade.coordenada[1]], popup=Cidade.nome).add_to(mapa)

#Adicionando caminho ao mapa
path_coordinates = [[Cidade.coordenada[0], Cidade.coordenada[1]] for Cidade in caminho]
folium.PolyLine(locations=path_coordinates, color = 'blue', weigth=5).add_to(mapa)

mapa.save(r'Example.html')
webbrowser.open(r'Example.html')

