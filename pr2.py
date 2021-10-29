from abc import ABC, abstractmethod 
import unittest
import doctest
import math

class CalcApp(ABC): 

  @abstractmethod
  def calcSum(self): 
    pass

class PageRank(CalcApp): 
  '''
  Fuer die Berechnung des PageRanks von Internetseiten.
  Einkommende und ausgehende Links nehmen Einfluss auf die Wertigkeit 
  der Verlinkungen und auch somit wieder auf den PageRank der nächsten verlinkten Seite.

  '''

  def __init__(self,appName): 
    self.appName = pr

  def calcSum(self, sites, leavingLinks, incomingLinks, whoIAM):
    result = float(0)
    for x in range( 0, incomingLinks[whoIAM] ):
      if ( True == isinstance(leavingLinks[x], list) ): 
        result = result + ( sites[x] / len( leavingLinks[x] ) )
    return result
  
  # sites is a list, leavingLinks is a list of lists
  def pR(self, sites, leavingLinks, incomingLinks, iterationNum=15):
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

    pR([1, 6, 13], [ [1,2] , [0,2] , [0] ], [1,1,2], 15)



class PageRankTest(unittest.TestCase):
  # todo


print("test")

doctest.testmod()





########################



