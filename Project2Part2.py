import random
class newNode:
    def __init__(self, nodeVal):
        self.val = nodeVal
        self.adjList = set()

class DirectedGraph:
    def __init__(self):
        self.listVertex = set() 

    def addNode(self, nodeVal): # ret type is void, parameter is string
        N = newNode(nodeVal)
        self.listVertex.add(N)

    def addUndirectedEdge(self, first, second): # ret type is void, parameters are nodes
        first.adjList.add(second)
       
    def removeUndirectedEdge(self, first, second): #ret type is void, parameters are final nodes
        first.adjList.remove(second)
     
    def getAllNodes(self): # return type is hashSet
        return self.listVertex


class TopSort:
    def Kahns(self, graph):#ret type is a ArrayList, parameter is a DirectedGraph
        counterList = {}
        x = graph.getAllNodes()
        for n in x:
            counterList[n] = 0
        for node in x:
            adjList = node.adjList
            for n in adjList:
                counterList[n] += 1
        queue = []
        for node in counterList:
            if counterList[node] == 0:
                queue.append(node)
                counterList[node] -= 1

        for item in queue:
            adjList = item.adjList
            for n in adjList:
                counterList[n] -= 1
            for node in counterList:
                if counterList[node] == 0:
                    queue.append(node)
                    counterList[node] -= 1
        return queue
   
    def mDFS(self, graph): #ret type is ArrayList, parameter is a DirectedGraph
        listNodes = graph.getAllNodes()
        start = next(iter(listNodes))
        visited = set()
        stack = []
        for node in listNodes:
            if node not in visited:
                self.mDFSHelper(node, visited, stack)
        stack.reverse()
        return stack

    def mDFSHelper(self,n, visited, stack):   
        visited.add(n)
        x = n.adjList
        for node in x:
            if node not in visited:
                self.mDFSHelper(node, visited, stack)
        stack.append(n)

class newNode2:
    def __init__(self, nodeVal):
        self.val = nodeVal
        self.adjList = {}

class WeightedGraph:
    def __init__(self):
        self.listVertex = set() 

    def addNode(self, nodeVal): # ret type is void, parameter is string
        N = newNode2(nodeVal)
        self.listVertex.add(N)

    def addUndirectedEdge(self, first, second, weight): # ret type is void, parameters are nodes, and integer weight
        first.adjList[second] = weight

    def removeUndirectedEdge(self, first, second): #ret type is void, parameters are final nodes
        del first.adjList[second]
     
    def getAllNodes(self): # return type is hashSet
        return self.listVertex

class newNode3:
    def __init__(self, x, y, nodeVal):
        self.val = nodeVal
        self.coordinates = (x,y)
        self.adjList = set()

class GridGraph:
    def __init__(self):
        self.nodesList = set() 

    def AddGridNode(self, x, y, nodeVal): #ret type is void, parameters are integers and a string
        N = newNode3(x, y, nodeVal)
        self.nodesList.add(N)
        return N

    def addUndirectedEdge(self, first, second): #ret type is void, parameters are GridNodes
        first.adjList.add(second)
        second.adjList.add(first)

        if abs(first.coordinates[0]- second.coordinates[0]) == 1 or abs(first.coordinates[1]- second.coordinates[1]) == 1 :
            first.adjList.add(second)
            second.adjList.add(first)

    def removeUndirectedEdge(self, first, second): #ret type is void, parameters are GridNodes
        first.adjList.remove(second)
        second.adjList.remove(first)
    
    def getAllNodes(self):
        return self.nodesList

    def getNode(self, x, y): #returns node with the specified x and y coordinates
        set = self.nodesList
        for node in set:
            if node.coordinates[0] == x and node.coordinates[1] == y:
                return node
        return None
    
def main():

    def ManhattanDistance (Node1, finalNode): 
        x1 = Node1.coordinates[0]
        x2 = Node1.coordinates[1]

        Final1 = finalNode.coordinates[0]
        Final2 = finalNode.coordinates[1]
        d = abs(Final1 - x1) + abs(Final2-x2)
        return d

    def astar(sourceNode, destNode): #ret type is a arrayList, parameters are Nodes
        visited = set()
        distancedict = {}
        parentDict = {}
        distancedict[sourceNode] = 0
        parentDict[sourceNode] = None
        finalDist = {}
        finalDist[source] = ManhattanDistance(sourceNode, destNode)
        curr = sourceNode
        a = True
        while a:
            adjlist = curr.adjList
            for neighbor in adjlist:
                if neighbor not in visited: 
                    if distancedict.get(neighbor) == None: #same as infinite
                        distancedict[neighbor] = distancedict[curr] 
                        parentDict[neighbor] = curr
                        finalDist[neighbor] = distancedict[neighbor] + ManhattanDistance(neighbor,destNode)
                    else:
                        if distancedict[curr]  < distancedict[neighbor]:
                            distancedict[neighbor] = distancedict[curr] 
                            parentDict[neighbor] = curr
                            finalDist[neighbor] = distancedict[neighbor] + ManhattanDistance(neighbor,destNode)
            visited.add(curr)
            min_ = 9999999
            for node in distancedict: #get the smallest val in dictionary
                if node not in visited:
                    if finalDist[node] < min_:
                        min_ = finalDist[node]
                        curr = node
            if curr == destNode:
                break
        final_array = []
        final_array.insert(0, destNode) 

        parent = parentDict[destNode]
        while parent:
            final_array.insert(0, parent)
            parent = parentDict[parent]
        
        return final_array

    def createRandomGridGraph(q): #ret type is a GridGraph, parameter is an int
        n = q+1
        g = GridGraph()
        dict = {}
        for i in range (n):
            for j in range (n):
                nodeVal = random.randint(1,10000)
                N = g.AddGridNode(i,j, nodeVal) 
                ans = dict.get(N, "no")
                if ans != "no": #means nodeVal not original
                    a = True
                    while a:
                        N = g.AddGridNode(i,j, i*2) 
                        ans = dict.get(N, "no")
                        if ans == "no":
                            a = False
                dict[N] = 1  
        allNodes = g.getAllNodes()
        for node in allNodes:
            #print("node 1: "+str(node.coordinates[0])+ " , "+ str(node.coordinates[1]))
            x = node.coordinates[0]
            y = node.coordinates[1]
            r = random.randint(1,4)
            if r == 1:
                node2 = g.getNode(x, y+1)
            elif r ==2:
                node2 = g.getNode(x, y-1)
            elif r==3:
                node2 = g.getNode(x-1, y)
            elif r==4:
                node2 = g.getNode(x+1, y)
            if node2:
                #print("node 2: " + str(node2.coordinates[0]) + " , " + str(node2.coordinates[1]))
                g.addUndirectedEdge(node,node2)
        return g

    def dijkstras (start, g): # ret type is a dictionary{node, integer} and parameter is the starting node
        x = g.getAllNodes()
        NumNodesGraph = len(x)
        visited = set()
        distancedict = {}
        parentDict = {}
        distancedict[start] = 0
        parentDict[start] = None
        curr = start
        while len(visited) != NumNodesGraph:
            adjlist = curr.adjList
            for neighbor in adjlist:
                if neighbor not in visited: 
                    if distancedict.get(neighbor) == None: 
                        distancedict[neighbor] = distancedict[curr] + adjlist[neighbor]
                        parentDict[neighbor] = curr
                    else:
                        if (distancedict[curr] + adjlist[neighbor]) < distancedict[neighbor]:
                            distancedict[neighbor] = distancedict[curr] + adjlist[neighbor]
                            parentDict[neighbor] = curr
            visited.add(curr)
            min_ = 9999999
            for node in distancedict: #get the smallest val in dictionary
                if node not in visited:
                    if distancedict[node] < min_:
                        min_ = distancedict[node]
                        curr = node
        return distancedict

    def createLinkedList (n): #ret type is a WeightedGraph object, parameter is an int
        g4 = WeightedGraph()
        node1Val = 0
        g4.addNode(node1Val)
        for i in range (1,n):
            nodeVal2 = i
            g4.addNode(nodeVal2)
            allNodes = g4.getAllNodes()
            for node in allNodes:
                if node.val == node1Val:
                    N1 = node
                if node.val == nodeVal2:
                    N2 = node
            g4.addUndirectedEdge(N1, N2, 1)
            node1Val = nodeVal2
        
        z = g4.getAllNodes()
        '''
        for node in z:
            print("node is ")
            print(node.val)
            print("and")
            for n in node.adjList:
                print(n.val)
                print(node.adjList[n]) 
        '''
        return g4
    
    def createRandomCompleteWeightedGraph(n) : #ret type is a WeightedGraph, parameter is a integer
        g = WeightedGraph()
        dicts = {}
        for i in range (n):
            g.addNode(i)
        allNodes = g.getAllNodes()
        for node1 in allNodes:
            for node2 in allNodes:
                weightVal = random.randint(0, 10)
                if node1 != node2:
                    g.addUndirectedEdge(node1, node2,weightVal) #creates a edge between every node and every other node
        return g


    def createRandomDAGIter(n): #ret type is DirectedGraph, parameter is an integer
        g = DirectedGraph()
        dicts = {}
        for i in range (n):
            a = True
            while a:
                nodeVal = random.randint(0, 1000000000)
                ans = dicts.get(nodeVal, "no")
                if ans == "no": #means nodeVal is orginal
                    dicts[nodeVal] = 1
                    a = False
                    g.addNode(nodeVal)
        allNodes = g.getAllNodes()
        allNodesList = list(allNodes)
        for i in range(n):
            if i< (n-2):
                g.addUndirectedEdge(allNodesList[i], allNodesList[i+2])
        return g
    
if __name__ == "__main__":
    main()
