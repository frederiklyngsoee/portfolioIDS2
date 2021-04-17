from sklearn.cluster import KMeans as K

class KMeansAlgorithm:
    def __init__(self):
        self.arrayOfStores = []

    #Call to update array for kmeans
    def updateStoreArray(self,coords):
        self.arrayOfStores.append(coords)

    #Calculates KMeans if there is more than 4 stores in the array
    def calculateKMeans(self):
        if len(self.arrayOfStores) > 4:
            kmeans = K(n_clusters=2)
            kmeans.fit(self.arrayOfStores)
            clusters = kmeans.cluster_centers_
            cluster1 = [clusters[0][0],clusters[0][1]]
            cluster2 = [clusters[1][0],clusters[1][1]]
            return cluster1, cluster2
        else:
            print("Need more stores to calculate KMeans")
            return 0

    #def nodes_to_category(self,node):
    #    for i in
