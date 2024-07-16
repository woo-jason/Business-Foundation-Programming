import sys

class Node:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self, root_value):
        self.root = root_value

    def __init__(self):
        self.root = None

    def insertNode(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        walker = None
        current = self.root
        while current is not None:
            walker = current
            if value > current.value:
                current = current.right_child
            elif value < current.value:
                current = current.left_child
            else: # Duplicate case, ignore
                return

        if walker.value > value:
            walker.left_child = Node(value)
        else:
            walker.right_child = Node(value)


    def printTree(self):
        currlevel = [self.root]
        layerNum = 0

        while len(currlevel) != 0:
            nextlevel = [None for i in range(0, pow(2, layerNum + 1))]
            currIndex = 0
            for node in currlevel:
                if node is not None:
                    print(node.value,end=' ')
                else:
                    currIndex += 2
                    print('X',end=' ')
                    continue

                nextlevel[currIndex] = node.left_child
                currIndex += 1
                nextlevel[currIndex] = node.right_child
                currIndex += 1

            print("")
            currlevel = nextlevel

            allempty = True
            for node in currlevel:
                if node is not None:
                    allempty = False
                    break
            if allempty:
                return
            layerNum += 1


if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " numbers_file.txt")
    exit()

my_tree = Tree() # create empty tree
with open(sys.argv[1], 'r') as f:
    for item in f.readlines():
        val = int(item.strip())
        my_tree.insertNode(val)
my_tree.printTree()