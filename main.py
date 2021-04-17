
from Graph import *
from UserInput import *
from KMeansAlgorithm import *

def main():

    graph = Graph()
    kmeans = KMeansAlgorithm()
    usein = UserInput(graph,kmeans)
    graph.updateGraph()

if __name__ == "__main__":
    main()




