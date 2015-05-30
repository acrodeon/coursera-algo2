##########################################################################
#                          Algo 2 Week 4                                 #
# all-pairs shortest paths                                               #
##########################################################################

from floyd_warshall import FloydWarshall, INFINITE

class APSP(FloydWarshall):
    """All-Pair Shortest Path extension of FloydWarshall which returns the shortest shortest path length if no negative cyle"""

    def __init__(self, g, n):
        """g as adjacencies matrix with n vertices named from 0 to n-1"""
        FloydWarshall.__init__(self, g, n)

    def getShortestShortestPathLength(self):
        """Return the length of shortest shortest path if no negative cycle"""
        if not self.computeAllPairsShortestPaths():
            print("Negative circuit!!!")
            return INFINITE
        else:
            min = INFINITE
            for i in range(self.n):
                for j in range(self.n):
                    if min > self.d[i][j]:
                        min = self.d[i][j]
            return min
            
##################
# Main() to test #
##################
if __name__ == '__main__':
    with open("g3.txt", mode='r') as f:
        #1st line is [number of vertices][number of edges]
        n, m = f.readline().split()
        n = int(n)
        g = []
        for line in f:
            u, v, w  = line.split()
            u, v, w  = int(u)-1, int(v)-1, int(w)
            g.append((u,v,w))
        apsp = APSP(g,n)
        min = apsp.getShortestShortestPathLength()
        if min != INFINITE:
            print("Shortest Shortest Path Length is {}".format(min))
            

    
