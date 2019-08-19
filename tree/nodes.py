class BinaryTree(object):

    def __init__(self,rootobj):
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None

    def insertleft(self,newNode):
        if self.leftchild ==None:
            self.leftchid = BinaryTree(newNode)
        else:
            t= BinaryTree(newNode)
            t.leftchid = self.leftchid
            self.leftchid = t

    def insertRight(self,newNode):
        if self.rightchild == None:
            self.rightchild = BinaryTree(newNode)

        else:
            t= BinaryTree(newNode)
            t.rightchild = self.rightchild
            self.rightchild = t

    def getRightChild(self):
        return self.rightchild

    def getleftchild(self):
        return self.leftchild

    def setRootVal(self,obj):
        self.key=obj

    def getRootVal(self):
        return self.key