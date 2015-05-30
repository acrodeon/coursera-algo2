##########################################################################
#                          FLOYD-WARSHALL                                #
# all-pairs shortest paths                                               #
##########################################################################

INFINITE = 10000000


class FloydWarshall():
    """Floyd Warshall algorithm in O(n**3) with n vertices in a dense graph"""

    def __init__(self, g, n):
        """g as adjacencies matrix with n vertices named from 0 to n-1"""
        self.n = n
        #self.adjMatrix = FloydWarshall.buildAdjacencyMatrix(g, self.n)
        self.parents = FloydWarshall.initParentMatrix(g, self.n)
        self.d = FloydWarshall.initDMatrix(g, self.n)
        
##
##    def buildAdjacencyMatrix(g, n):
##        """(i,j,w) is for an edge (i,j) with a weigh w; n the number of vertices"""
##        m = []
##        for i in range(n):
##            m.append([None]*n)
##        for i in range(n):
##            m[i][i] = 0
##        for (i,j,w) in g:
##            if (i != j):
##                m[i][j] = w
##        return m

    def initParentMatrix(g, n):
        """Initialize the matrix where (i,j) is the parent of j in a shortest path from i"""
        #pi = [[None]*n]*n is not working because pi pi[0] pi[1] ... is same list
        pi = []
        for i in range(n):
            pi.append([None]*n)
        for (i,j,w) in g:
            if (i != j and w != INFINITE):
                pi[i][j] = i
        return pi

    def initDMatrix(g,n):
         """Initialize two matrices where (i,j) is the weight of a shortest path from i to j with intermediate vertices in {0..k} at step k"""
         matrix = []
         for row in range(n):
             matrix.append([INFINITE]*n)
             matrix[row][row] = 0
         for (i,j,w) in g:
             matrix[i][j] = w
         return matrix

    def computeAllPairsShortestPaths(self):
        """Return False if a non-negative circuit is present"""
        for k in range(self.n):
            print(k)
            for i in range(self.n):
                for j in range(self.n):
                    if self.d[i][j] > self.d[i][k] + self.d[k][j]:
                        self.d[i][j] = self.d[i][k] + self.d[k][j]
                        self.parents[i][j] = self.parents[k][j]
        for i in range(self.n):
            if self.d[i][i] < 0:
                return False
        return True

    def getParents(self):
        """return the parent matrix"""
        return self.parents

    def getShortestPathsWeights(self):
        """return the matrix of shortest paths' weight"""
        return self.d
    
    def printShortestPath(pi, i, j):
        """print shortest path -if any- from i to j"""
        if i == j:
            print("{} ".format(i), end='')
        elif pi[i][j] == None:
            print ("No path from {} to {}".format(i,j))
        else:
            FloydWarshall.printShortestPath(pi,i,pi[i][j])
            print("{} ".format(j), end='')
    
    
##################
# Main() to test #
##################
if __name__ == '__main__':
    g = [(0,1,3), (0,4,-4), (0,2,8), (1,4,7), (1,3,1), (2,1,4), (3,0,2),(3,2,-5),(4,3,6)]
    nbVertices = 5
    floydWarshall = FloydWarshall(g,nbVertices)
    if not floydWarshall.computeAllPairsShortestPaths():
        print("Non-Negative circuit!!!")
    else:
        pi = floydWarshall.getParents()
##        print(pi)
        d = floydWarshall.getShortestPathsWeights()
        print(d)
        for i in range(nbVertices):
            for j in range(nbVertices):
                if (i != j and d[i][j] != INFINITE):
                    print("Le chemin de {} à {} de poids {}".format(i,j,d[i][j]))
                    FloydWarshall.printShortestPath(pi,i,j)
                    print()
               
                
