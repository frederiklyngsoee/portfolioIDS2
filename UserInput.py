    
class UserInput:
    def onclick(self,event, coords): #Onclick event that adds a vertex to the array and plots it aswell.
        self.coords.append([event.xdata, event.ydata])
        self.ax.plot(event.xdata,event.ydata,'o')