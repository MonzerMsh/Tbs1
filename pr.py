import math
# base Pr is 1st
# leavingLinks is number of links from each site
# iterationNum is number of iterations

def calcSum(sites, leavingLinks, incomingLinks, whoIAM):
    result = float(0)
    for x in range( 0, incomingLinks[whoIAM] ):
        if ( True == isinstance(leavingLinks[x], list) ): 
            result = result + ( sites[x] / len( leavingLinks[x] ) )
    return result

# sites is a list, leavingLinks is a list of lists
def pR(sites, leavingLinks, incomingLinks, iterationNum=15):

    for x in range(0,iterationNum):
        
        if ( len(sites) == len(leavingLinks) ) :
            # A = sites[0]
            calculated = sites

            for x in range(0, len(sites) ) :
                calculated[x] = 0.85 * ( calcSum(sites, leavingLinks, incomingLinks, x) ) + (1-0.85)
        
        else :
            print("You did something wrong!")
        
        sites = calculated
    
    print(sites)

#Testen
#print(type([ [1,2],[0,2], 0 ]))
#print(calcSum([1, 1, 1], [ [1,2],[0,2], 0 ], [1,1,2], 2 )  )

#Erklärung
#[1,1,1] -> A(p)=1 , B(p)=1, C(p)=1,
#0 -> A, 1 -> B, 2 -> C


pR([1, 6, 13], [ [1,2] , [0,2] , [0] ], [1,1,2], 15)