#################################################################################
#                         Algo2 Week1                                           #
# greedy algorithms for minimizing the weighted sum of completion times         #                      
#################################################################################

from operator import itemgetter, attrgetter


def getWeightedSumCompletion(orderedJobs):
    """return the weighted sum of completion of jobs as a list of tuple (weight, length, key for decreasing order)"""
    #first order the list by decreasing order of weigth
    jobs = sorted(orderedJobs, key=itemgetter(0), reverse=True)
    #second order by decreasing key as three element in t-uple
    jobs.sort(key=itemgetter(2), reverse=True)
    sum = 0
    res = 0
    for w,l,key in jobs:
        sum += l
        res += sum * w
    return res
        
##################
# Main() to test #
##################
if __name__ == '__main__':
    nonOptimalJobs, optimalJobs = [], []
    
    with open('jobs.txt') as f:
        for line in f:
            w, l = line.split()
            w = int(w)
            l = int(l)
            nonOptimalJobs.append((w,l,w-l))
            optimalJobs.append((w,l, w/l))
        print("Non optimal scheduling: ", getWeightedSumCompletion(nonOptimalJobs))
        print("Optimal scheduling: ", getWeightedSumCompletion(optimalJobs))

      

        
