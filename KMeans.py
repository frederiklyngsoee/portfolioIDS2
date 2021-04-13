from sklearn.cluster as KMeans
from numpy import np

class KMeans:
    X = np.array(coords)
    kmeans = KMeans(n_clusters=2, random_state=0).fit(X)