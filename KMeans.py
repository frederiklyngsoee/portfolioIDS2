from sklearn.cluster import KMeans as K
import numpy as np

class KMeans:
    def __init__(self, coords):
        self.X = np.array(coords)
        self.kmeans = K(n_clusters=2, random_state=0).fit(self.X)
        

    def returnKMeans(self):
        return self.kmeans