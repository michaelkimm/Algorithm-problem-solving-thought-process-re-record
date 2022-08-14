import sys
input = sys.stdin.readline

class Node:
    def __init__(self, val):
        self.blueLine = []
        self.redLine = []
        self.horses = []
        self.val = val
        self.isEnd = False
    
    def addBlueLine(self, target):
        self.blueLine.append(target)

    def addRedLine(self, target):
        self.redLine.append(target)

    def addHorse(self, horseNum):
        self.horses.append(horseNum)

    def extractHorse(self, horseNum):
        self.horses.remove(horseNum)

    def existsHorse(self, horseNum):
        result = self.horses.index(horseNum)
        return True if result != -1 : False

    def existsAnyHorse(self):
        return True if len(self.horses) != 0 : False

    def setEnd(self):
        self.isEnd = True

    def isEnd(self):
        return self.isEnd


start = 0
end = 50
graph = [[] for _ in range(end + 1)]

def initializeGraph(graph):
    global start, end

    # 노드 정의
    startNode = Node(0)
    n1 = Node(2)
    startNode.addRedLine(n1)

    n2 = Node(4)
    n1.addRedLine(n2)
    
    n3 = Node(6)
    n2.addRedLine(n3)

    n4 = Node(8)
    n3.addRedLine(n4)

    n5 = Node(10)
    n4.addRedLine(n5)

    n6 = Node(12)
    n7 = Node(14)
    n8 = Node(16)
    n9 = Node(18)
    n10 = Node(20)
    n11 = Node(22)
    n12 = Node(24)
    n13 = Node(26)
    n14 = Node(28)
    n15 = Node(30)
    n16 = Node(32)
    n17 = Node(34)
    n18 = Node(36)
    n19 = Node(38)
    n20 = Node(40)

    n21 = Node(13)
    n22 = Node(16)
    n23 = Node(19)
    n24 = Node(25)
    n25 = Node(22)
    n26 = Node(24)
    n27 = Node(28)
    n28 = Node(27)
    n29 = Node(26)
    n30 = Node(30)
    n31 = Node(35)

    end = Node(0)
    end.setEnd()

    # 노드 연결


