class Node:
    def __init__(self, content):
        self.content = content
        self.left = self
        self.right = self

    def getContent(self):
        return self.content

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def remove(self):
        if self.right is not None and self.left is not None:
            self.right.setLeft(self.left)
            self.left.setRight(self.right)


class Circle:
    def __init__(self):
        self.start = None

    def append(self, content):
        if self.start is None:
            self.start = Node(content)
        else:
            self.start.getLeft().setRight(Node(content))
            self.start.getLeft().getRight().setLeft(self.start.getLeft())
            self.start.setLeft(self.start.getLeft().getRight())
            self.start.getLeft().setRight(self.start)

    def find(self, content):
        if self.start is None:
            return
        testNode = self.start
        loop_over = False
        while testNode.getContent() != content:
            if testNode == self.start:
                if loop_over:
                    return
                loop_over = True
            testNode = testNode.getRight()
        return testNode

    def insert(self, content, insertafter):
        node = self.find(insertafter)
        if node is None:
            return
        self.start = node.getRight()
        self.append(content)

    def remove(self, content):
        node = self.find(content)
        if node is None:
            return
        if node == self.start:
            self.start = self.start.getRight()
        node.remove()

    def getStart(self):
        return self.start.getContent()

    def getRightFrom(self, content):
        node = self.find(content)
        if node is None:
            return
        return node.getRight().getContent()

    def isPresent(self, content):
        return self.find(content) is not None

    def print(self, after=None):
        if after is None:
            after = self.getStart()
        node = self.find(after)

        re = ""
        node = node.getRight()
        while node.getContent() != after:
            re = re + str(node.getContent())
            node = node.getRight()
        return re


fileline = open("example.txt").read().split("\n")
c = Circle()
for cup in fileline[0]:
    c.append(int(cup))

currentCup = c.getStart()
for x in range(100):

    pickedCups = []
    for i in range(3):
        cup = c.getRightFrom(currentCup)
        pickedCups.append(cup)
        c.remove(cup)

    destinationCup = currentCup-1
    while not c.isPresent(destinationCup):
        destinationCup -= 1
        if destinationCup <= 0:
            destinationCup = 10

    for p_cup in pickedCups:
        c.insert(p_cup, destinationCup)
        destinationCup = p_cup

    currentCup = c.getRightFrom(currentCup)
    print(c.print(1))


