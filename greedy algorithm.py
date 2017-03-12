###########################
# 6.00.2x Problem Set 1: Space Cows 
import time

#================================
# Part A: Transporting Space Cows
#================================
start=time.time()
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

def maxa(coww,lims):
    
    
    maxi=0
    
    
    for i in coww:
        if coww[i]>maxi and coww[i]<=lims:
            maxi=coww[i]
            name=i
            
    if(maxi!=0):
        return name
    else:
        return 'n'

# Problem 1
def greedy_cow_transport(cows,limit):
    l=len(cows)
    c=1
    answer=[]
    while(c<l):
        list1=[]
        limi=limit
        for x in range(0,l):
            naamcow=maxa(cows,limi)
            if(naamcow!='n'):
                list1.append(naamcow)
                limi=limi-cows[naamcow]
                
                del cows[naamcow]
                c=c+1
                
                

        answer.append(list1)

    return answer


end=time.time()
    
    #pass


"""
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)
print(end-start)
print(greedy_cow_transport(cows, limit))


