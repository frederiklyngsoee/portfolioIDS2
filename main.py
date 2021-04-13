from GraphController import *
from KMeans import *

def main():
    try:
        graphyboi = GraphController()
        graphyboi.update()
        kmeansyboi = KMeans(graphyboi.coords)
    except:
        print("Nothing in coords")


if __name__ == "__main__":
    main()   






