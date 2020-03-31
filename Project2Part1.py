import random

class newNode:
    def __init__(self, nodeVal):
        self.val = nodeVal
        self.adjList = []

class Graph:
    def __init__(self):
        self.listVertex = set() 

    def addNode(self, nodeVal): # ret type is void, parameter is string
        #print("in addNode")
        N = newNode(nodeVal)
        self.listVertex.add(N)
        #for node in self.listVertex:
        #    print(node.val)
        #return N

    def addUndirectedEdge(self, first, second): # ret type is void, parameters are nodes
        first.adjList.append(second)
        second.adjList.append(first)

    def addUndirectedEdgeOneWay(self, first, second): # ret type is void, parameters are nodes
        first.adjList.append(second)

    def removeUndirectedEdge(self, first, second): #ret type is void, parameters are final nodes
        first.adjList.remove(second)
        second.adjList.remove(first)
     
    def getAllNodes(self): # return type is hashSet
        return self.listVertex

class GraphSearch:
    def __init__(self):
        pass

    def DFSIter(self, start , end): # ret type is a list of nodes, parameters are nodes
        stack = []
        visited_list = []
        stack.append(start) #stack.push()
        visited_list.append(start)

        while stack: #checks that stack is not empty
            peek = stack[-1] #stack.peek()
            if peek == end:
                return visited_list
            adjNodes = peek.adjList #returns a list
            notVisited = [] #list of neighbor nodes that have not been visited

            for node in adjNodes:
                if node not in visited_list:
                    notVisited.append(node)
            if notVisited:
                stack.append(notVisited[0])
                visited_list.append(notVisited[0])
            else:
                stack.pop()
        return None
  
    def DFSHelper(self, node, visited, end):
        visited.append(node)
        if node == end:
            return visited
        x = node.adjList
        while x:
            notVisited = []
            for n in x:
                if n not in visited:
                    notVisited.append(n)
            if notVisited:
                visited = self.DFSHelper(notVisited[0], visited, end)
                if visited[-1] == end:
                    return visited
            else:
                return visited

    def DFSRec(self, start , end): # ret type is a list of nodes, parameters are nodes
        visited = []
        visited = self.DFSHelper(start, visited, end)
        return visited
   
    def BFTIter(self, graph): # ret type is a list of nodes, parameter is a graph
        x = graph.getAllNodes()
        start = next(iter(x))
        queue = []
        visited_list = []
        queue.append(start) #queue.add()
        visited_list.append(start)

        while queue: #checks that queue is not empty
            element = queue[0] #queue.element()
            #if element == end:
            #    return visited_list
            adjNodes = element.adjList#returns a list
            notVisited = [] #list of neighbor nodes that have not been visited
            for node in adjNodes:
                if node not in visited_list:
                    notVisited.append(node)
            
            for node in notVisited:
                queue.append(node)
                visited_list.append(node)
            del queue[0] #removes the head

        return visited_list

    def BFTHelper(self, node, visited, queue):
        x = node.adjList
        notVisited = []
        for node in x:
            if node not in visited:
                notVisited.append(node)
        for node in notVisited:
            visited.append(node)
            queue.append(node)
        del queue[0] #removes the head
        if queue:
            Node = queue[0]
            self.BFTHelper(Node, visited, queue)
        return visited

    def BFTRec(self, graph ): # ret type is a list of nodes, parameter is a graph
        visited = []
        queue = []
        x = graph.getAllNodes()
        start = next(iter(x))
        visited.append(start)
        queue.append(start)
        visited = self.BFTHelper(start, visited, queue)
        return visited

def main():
   
    def createRandomUnweightedGraphIter (n): #ret type is Graph object, parameter is an int
        g = Graph()
        dicts = {}
        for i in range (n):
            a = True
            while a:
                nodeVal = random.randint(0, 10)
                ans = dicts.get(nodeVal, "no")
                if ans == "no": #means nodeVal is orginal
                    dicts[nodeVal] = 1
                    a = False
                    g.addNode(nodeVal)
        allNodes = g.getAllNodes()
        for node1 in allNodes:
            for node2 in allNodes:
                if node1 != node2:
                    g.addUndirectedEdgeOneWay(node1, node2) #creates a edge between every node and every other node
        return g
    gb = createRandomUnweightedGraphIter(5)
    
    def createLinkedList (n): #ret type is Graph object, parameter is an int
        g4 = Graph()
        #node1Val = random.randint(0, 50)
        node1Val = 0
        dicts = {}
        dicts[node1Val] = 1
        g4.addNode(node1Val)
        #for i in range (n):
        for i in range (1,n):
            a = True
            while a:
                #nodeVal2 = random.randint(0, 50)
                nodeVal2 = i
                ans = dicts.get(nodeVal2, "no")
                if ans == "no": #means nodeVal is orginal
                    dicts[nodeVal2] = 1
                    a = False
                    g4.addNode(nodeVal2)
                    allNodes = g4.getAllNodes()
                    for node in allNodes:
                        if node.val == node1Val:
                            N1 = node
                        if node.val == nodeVal2:
                            N2 = node
                    g4.addUndirectedEdgeOneWay(N1, N2)
                    node1Val = nodeVal2
    
        return g4
    gc = createLinkedList(6)

    def BFTRecLinkedList (graph): #ret type ArrayList, parameter is a graph
        graph = createLinkedList(10000)
        Gs2 = GraphSearch()
        array_list = Gs2.BFTRec(graph)
        return array_list

    def BFTIterLinkedList (graph): #ret type ArrayList, parameter is a graph
        graph = createLinkedList(10000)
        Gs2 = GraphSearch()
        array_list = Gs2.BFTIter(graph)
        return array_list
  
if __name__ == "__main__":
    main()