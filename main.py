import sys

class Tarjan:
    def __init__(self, graph):
        self.graph = graph
        self.index = 0
        self.stack = []
        self.indexes = {}
        self.lowlinks = {}
        self.answer = []

    def setup(self):
        for v in self.graph:
            self.indexes[v] = None
            self.lowlinks[v] = None

    def run(self):
        for v in self.graph:
            if self.indexes[v] == None:
               self.SCC(v)
    
    def SCC(self, v):
        self.indexes[v] = self.index
        self.lowlinks[v] = self.index
        self.index += 1
        self.stack.append(v)
        SCComp = []

        for w in self.graph[v]:
            if self.indexes[w] == None:
                self.SCC(w)
                self.lowlinks[v] = min(self.lowlinks[v], self.lowlinks[w])
            elif w in self.stack:
                self.lowlinks[v] = min(self.lowlinks[v], self.indexes[w])
        
        if self.lowlinks[v] == self.indexes[v]:
            w = None
            while w != v:
                w = self.stack.pop()
                SCComp.append(w)
        if SCComp != [] and SCComp not in self.answer:
            SCComp.sort()
            self.answer.append(SCComp)

    def FindInSCC(self, element):
        for scc in self.answer:
            if element in scc:
                return scc[0]
        
    def GetFinalAnswer(self):
        FinalAnswer = {}
        for answer in self.answer:
            for element in answer:
                destinations = self.graph[element]
                for destination in destinations:
                    if self.FindInSCC(element) not in FinalAnswer:
                        FinalAnswer[self.FindInSCC(element)] = []

                    if self.FindInSCC(destination) != [] and self.FindInSCC(destination) != self.FindInSCC(element):
                        if self.FindInSCC(destination) not in FinalAnswer[self.FindInSCC(element)]:
                            FinalAnswer[self.FindInSCC(element)].append(self.FindInSCC(destination))

        #R
        print(len(self.answer))
        
        #L
        connections = 0
        for element in FinalAnswer:
            connections += len(FinalAnswer[element])
        print(connections)

        for key in sorted (FinalAnswer.keys()):
            FinalAnswer[key].sort()
            for element in FinalAnswer[key]:
                print(f'{key} {element}')
    


class Graph:
    def __init__(self, vertices):
        self.graph = self.setup(vertices)
  
    def setup(self, vertices):
        graph = {}
        for i in range(vertices):
            graph[i+1] = []
        return graph

    def getGraph(self):
        return self.graph
    
    def addEdge(self, origin, destination):
        self.graph[origin].append(destination)



if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:
        inputLines = f.read().split("\n")
    
    N = eval(inputLines[0])
    M = eval(inputLines[1])
    
    connections = inputLines[2:]
    
    graph = Graph(N)
    
    for line in connections:
        line = line.split(" ")
        origin = eval(line[0])
        destination = eval(line[1])
        graph.addEdge(origin, destination)


    tarj = Tarjan(graph.getGraph())
    tarj.setup()
    tarj.run()
    tarj.GetFinalAnswer()