'''
The Ruler of HackerLand believes that every citizen of the country should have access to a library. But unfortunately, HackerLand was hit by a tornado that destroyed all of its libraries and obstructed its roads! As you are the greatest programmer of HackerLand, the ruler wants your help to repair the roads and build some new libraries efficiently.

HackerLand has  cities numbered from  to . The cities are connected by  bidirectional roads. A citizen has access to a library if:

Their city contains a library.
They can travel by road from their city to a city containing a library.
The following figure is a sample map of hackerland where the dotted lines denote obstructed roads:

image

The cost of repairing any road is  dollars, and the cost to build a library in any city is  dollars.

You are given  queries, where each query consists of a map of HackerLand and value of  and .

For each query, find the minimum cost of making libraries accessible to all the citizens and print it on a new line.

Input Format

The first line contains a single integer, , denoting the number of queries. The subsequent lines describe each query in the following format:

The first line contains four space-separated integers describing the respective values of  (the number of cities),  (the number of roads),  (the cost to build a library), and  (the cost to repair a road).
Each line  of the  subsequent lines contains two space-separated integers,  and , describing a bidirectional road connecting cities  and .
Constraints

Each road connects two distinct cities.
Output Format

For each query, print an integer denoting the minimum cost of making libraries accessible to all the citizens on a new line.

Sample Input

2
3 3 2 1
1 2
3 1
2 3
6 6 2 5
1 3
3 4
2 4
1 2
2 3
5 6
Sample Output

4
12
Explanation

We perform the following  queries:

HackerLand contains  cities connected by  bidirectional roads. The price of building a library is  and the price for repairing a road is .
image
The cheapest way to make libraries accessible to all is to:

Build a library in city  at a cost of .
Repair the road between cities  and  at a cost of .
Repair the road between cities  and  at a cost of .
This gives us a total cost of . Note that we don't need to repair the road between cities  and because we repaired the roads connecting them to city !

In this scenario it's optimal to build a library in each city because the cost of building a library () is less than the cost of repairing a road (). image

There are  cities, so the total cost is .
'''
# n is number of cities
# m is number of roads connecting cities
# x is cost of building library
# y is cost of repairing road
# need either a library in city or road connection
'''
Have to start off with a library in the first city. If road is cheaper, then just repair roads for rest.
Any nodes not connected then need their own library also.
'''

import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.hasLibrary = False
    def getNeighbors(self):
        return self.neighbors
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)
    def hasLibrary(self):
        return self.hasLibrary
    def addLibrary(self):
        self.hasLibrary = True

def create_nodes(n):
    cities = []
    for i in range(0,n):
        cities.append(Node(i+1))
    return cities


q = int(raw_input().strip())
for a0 in xrange(q):
    n,m,x,y = raw_input().strip().split(' ')
    n,m,x,y = [int(n),int(m),int(x),int(y)]
    cities = create_nodes(n)
    cost = 0
    for a1 in xrange(m):
        city_1,city_2 = raw_input().strip().split(' ')
        city_1,city_2 = [int(city_1),int(city_2)]
        cities[city_1 - 1].addNeighbor(cities[city_2 - 1])
        cities[city_2 - 1].addNeighbor(cities[city_1 - 1])
    for i in range(0,n):


