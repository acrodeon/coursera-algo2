##########################################################################
#                          Algo 2 Week 6                                 #
# 2-SAT problem via SCC algos                                            #
##########################################################################

from algo1week4_sccs import DFSGraph, KosarajuAlgo
import threading
import sys

class TwoSat(KosarajuAlgo):
    """2-SAT problem using Kosaraju SCC algo"""

    def __init__(self):
        KosarajuAlgo.__init__(self)

    def isSatisfiable(self, g, grev):
        """return true if there is an assignment for the 2SAT problem"""
        res = self.kosarajuAlgo(g, grev)
        for scc in res.values():
            vertices = set()
            for x in scc:
                if -(x.getId()) in vertices:
                    return False
                vertices.add(x.getId())
        return True

def main():
    with open("2sat1.txt", mode='r') as f:
        next(f)
        g = DFSGraph()
        grev = DFSGraph()
        for line in f:
            x, y = line.split()
            x, y = int(x), int(y)
            g.addEdge(-x,y)
            grev.addEdge(y,-x)
            g.addEdge(-y,x)
            grev.addEdge(x,-y)
        solver = TwoSat()
        if solver.isSatisfiable(g, grev):
            print("OK : 2SAT problem is satisfiable")
        else:
            print("KO : 2SAT problem is unsatisfiable")

##################
# Main() to test #
##################
if __name__ == '__main__':
    # In summary, sys.setrecursionlimit is just a limit enforced by the interpreter itself.
    # threading.stack_size lets you manipulate the actual limit imposed by the OS. If you hit the latter limit first, Python will just crash completely.
    threading.stack_size(67108864) # 64MB stack
    # to avoid RuntimeError: maximum recursion depth exceeded because by default 1000 is the limit returnt by sys.getrecursionlimit()
    sys.setrecursionlimit(2 ** 20) # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target

            
