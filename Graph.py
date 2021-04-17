import matplotlib.pyplot as plt
import numpy as np

class Graph:

    #Init creates empty graph
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        print("Graph initiated")

    #Creates a connection to the graph
    def connect_to_graph(self,typeEvent,typeUserInput):
        self.fig.canvas.mpl_connect(typeEvent,typeUserInput)

    #Creates a new plot taking event data on graph
    def draw_new_store(self,event):
        self.ax.plot(event.xdata, event.ydata, 'o')

    #Creates centroids
    def draw_new_centroids(self,centroid1,centroid2):
        centroid_one = self.ax.plot(centroid1[0], centroid1[1], 'X')
        centroid_two = self.ax.plot(centroid2[0], centroid2[1], 'X')

    #Updates graph
    def updateGraph(self):
        plt.show()
