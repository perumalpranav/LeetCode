class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Graph Problem
        #Topological Sort
        #Build adjacency list then remove one by one

        adjList = [{"in":set(),"out":set()} for _ in range(numCourses)]

        for a, b in prerequisites:
                adjList[a]["in"].add(b) #A receives B
                adjList[b]["out"].add(a)

        order = []
        while True:
            before = len(order)
            for i in range(numCourses):
                if adjList[i] != 'X' and len(adjList[i]["in"]) == 0:
                    #Remove/Take this first

                    #Remove prereqs
                    for reciever in adjList[i]["out"]:
                        adjList[reciever]["in"].remove(i)

                    adjList[i] = 'X'
                    order.append(i)
                    break

            if len(order) == numCourses:
                return order
            elif before == len(order):
                return []

            




        