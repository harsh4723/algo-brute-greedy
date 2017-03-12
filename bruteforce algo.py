###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict






# Problem 2

def minimum(listfi):
    min=10000
    minlist=[]
    
    for list1 in listfi:
        if len(list1)<min:
            min=len(list1)
            minlist=list1
            
    return minlist

            



def brute_force_cow_transport(cows,limit):
    list1=cows.keys()
    
    
    listfi=[]
    for parti in get_partitions(list1):
        l=len(parti)
        c=0
        for trip in parti:
            s1=0
            for val in trip:
                s1=s1+cows[val]
            if(s1<=limit):
                c=c+1
        if(c==l):
            listfi.append(parti)
    
    return minimum(listfi)




    
          
        
                    






cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)


print(brute_force_cow_transport(cows, limit))


