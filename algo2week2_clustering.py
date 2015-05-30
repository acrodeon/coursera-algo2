##################################
# Algo2 Week2                      #
# Single Link Clustering Algorithm #
####################################

from dheap import HeapItem, DHeapHandler
from kruskal import Kruskal, DisjointSet

INFINITY = float("inf")

class SingleLinkClustering(Kruskal):
    """to get the maximum spacing k-clusterings"""
    
    def __init__(self, nbNodes, weightedEdges):
        """set of 3-uples u,v,weight"""
        self.nbNodes = nbNodes
        # set of 3uples weighted edges in increasing order of weights
        Kruskal.__init__(self,weightedEdges)

    def getCurrentSpacing(self):
        """get the minimum distance from two nodes"""
        for u,v,w in self.weightedEdges:
            if self.disjointSet.findSet(u) != self.disjointSet.findSet(v):
                self.disjointSet.unionSet(u,v)
                return w
            
    def getMaxSpacing(self, k):
        """get the maximum spacing of k-clustering"""
        for _ in range(self.nbNodes - k): 
            self.getCurrentSpacing()
        return self.getCurrentSpacing()


class HammingClustering(DisjointSet):
    """Compute the maximum number of clusters for a spacing at least 3; Hamming distance"""

    def __init__(self, elements, nbBits):
        """elements is a set of nodes, each node has nbBits bits"""
        DisjointSet.__init__(self, elements)
        self.nbBits = nbBits
        self.elements = elements
        self.nbClusters = len(self.elements)
        print("self.nbClusters ", self.nbClusters)

    def _mergeOneDistanceNodes(self):
        """merge pair of nodes with weight one"""
        count = 0
        for x in self.elements:
            for pos in range(self.nbBits):
                y = x ^ (1 << pos)
                if y in self.elements and self.findSet(x) != self.findSet(y):
                    self.unionSet(x, y)
                    self.nbClusters -=1
                    count += 1
        print("Count 1 ", count)
                    
    def _mergeTwoDistanceNodes(self):
        """merge pair of nodes with weight two"""
        count = 0
        for x in self.elements:
            for pos1 in range(self.nbBits):
                for pos2 in range(self.nbBits):
                    y = ['0'] * self.nbBits
                    y[pos1] = '1'
                    if pos1 != pos2:
                        y[pos2] = '1'
                    node_y = ''.join(y)
                    z = x ^ int(node_y, base=2)
                    if z in self.elements and self.findSet(x) != self.findSet(z):
                        self.unionSet(x, z)
                        self.nbClusters -=1
                        count += 1
        print("Count 2 ", count)
                    


    def getNbClustersSpacingThree(self):
        """return the maximum number of clusters for spacing at least 3"""
        self._mergeOneDistanceNodes()
        self._mergeTwoDistanceNodes()
        return self.nbClusters
            


##################
# Main() to test #
##################
if __name__ == '__main__':
    # For question 1, max-spacing 4-clustering
    with open("clustering1.txt", mode='r') as f:
        nbNodes = int(f.readline())
        G = set()
        for line in f:
            i, j, d = line.split()
            d = int(d)
            G |= {(i,j,d)}
        print("For a 4-clustering, the maximum spacing is {}".format(SingleLinkClustering(nbNodes, G).getMaxSpacing(4)))   
        
    with open("clustering_big.txt", mode='r') as f:
        nbNodes, nbBits = f.readline().split()
        nbNodes, nbBits = int(nbNodes), int(nbBits)
        print(nbNodes, nbBits)
        #nbNodes = 10000
        elements = set()
        for line in f:
            node = ''.join(line.strip().split())
            elements |= {int(node, base=2)}
        hammingClusterAlgo = HammingClustering(elements, 24)
        print("{} clusters to have a spacing greater than 2".format(hammingClusterAlgo.getNbClustersSpacingThree()))
