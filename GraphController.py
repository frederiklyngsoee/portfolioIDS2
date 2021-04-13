import matplotlib.pyplot as plt 
from matplotlib.widgets import Cursor, Button

class GraphController:
    def __init__(self): #Constructor
        self.p, = plt.plot(0,0,'o') #Plot origin
        self.cursor = Cursor(self.ax, horizOn=True, vertOn = True, color = 'red', linewidth = 2.0) ##Cursor coordinates + crosshair
        self.coords = [] ##Init coord-array
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick) #Make connection between mouse and screen

    def update(self): #Updates the plot 
        plt.show() 
    

    def onclick(self,event): #Onclick event that adds a vertex to the array and plots it aswell.
        self.coords.append([event.xdata, event.ydata])
        self.ax.plot(event.xdata,event.ydata,'o')

    