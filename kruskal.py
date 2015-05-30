#########################  
# Kruskal's Algorithm   #
# Minimum spanning tree #
#########################

# to sort according to item number in tuple
from operator import itemgetter

class DisjointSet:
    """Union by rank and Path Compression heuristics"""

    def __init__(self, elements):
        """a dictionary as key=x value=[parent of x, rank of x] from set elements"""
        self.dictElements = dict()
        for x in elements:
            self.createSet(x)
        
    def createSet(self, x):
        """key=x value=[parent of x, rank of x]"""
        self.dictElements[x] = [x, 0]
        
    def findSet(self, x):
        """find the root of the discovery path or None if not defined"""
        if x == None:
            return None
        p_x = self.dictElements.get(x, [None,-1])[0]
        if p_x == None:
            return None
        if x != p_x:
            return self.findSet(p_x)
        else:
            return p_x
                
    def _bindSets(self, x, y):
        """one root is child of another root"""
        rank_x = self.dictElements.get(x, [None,-1])[1]
        rank_y = self.dictElements.get(y, [None,-1])[1]
        if rank_x != -1 and rank_y != -1 :
            if rank_x > rank_y:
                # root x becomes parent of root y
                self.dictElements[y][0] = x
            else:
                # root y becomes parent of root x
                self.dictElements[x][0] = y
                if rank_x == rank_y:
                    # height of y is incremented
                    self.dictElements[y][1] = rank_y + 1

    def unionSet(self, x, y):
        """Union of two disjoint sets containing respectively x and y"""
        self._bindSets(self.findSet(x),self.findSet(y))
         
class Kruskal:
    """Minimum spanning tree Kruskal Algorithm O(A lg(S))"""

    def __init__(self, weightedEdges):
        """set of 3-uples u,v,weight"""
        # set of 3uples weighted edges in increasing order of weights
        self.weightedEdges = sorted(weightedEdges, key=itemgetter(2))
        # disjoint sets of vertices
        vertices = set()
        for u,v,w in self.weightedEdges:
            vertices |= {u,v}
        self.disjointSet = DisjointSet(vertices)

    def getMinimumSpanningTree(self):
        """return the edges of the minimum spanning tree"""
        mst = set()
        for u,v,w in self.weightedEdges:
            if self.disjointSet.findSet(u) != self.disjointSet.findSet(v):
                mst.add((u,v))
                self.disjointSet.unionSet(u,v)
        return mst
        

##################
# Main() to test #
##################
if __name__ == '__main__':
    G = {('a','b',4), ('a','h',8), ('b','h',11), ('b','c',8), ('h','i',7), ('h','g',1), ('i','c',2),('i','g',6), ('c','d',7), ('c','f',4), ('g','f',2), ('d','f',14), ('d','e',9), ('f','e',10)}
    print(sorted(Kruskal(G).getMinimumSpanningTree()))

       
    
            
        

