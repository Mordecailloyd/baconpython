class BinaryTree():
  def __init__(self,rootid):
    self.left = None
    self.right = None
    self.rootid = rootid
    #self.rootid = str(rootid)

  def getLeftChild(self):
      return self.left
  def getRightChild(self):
      return self.right
  def setNodeValue(self,value):
      self.rootid = value
  def getNodeValue(self):
      return self.rootid

  def rightInsert(self,value):
    self.right = BinaryTree(value)

  def leftInsert(self,value):
    self.left = BinaryTree(value)





def print_tree(tree,depth=0):
  if tree == None:
    return
  else:
    if depth > 0:
      print ('| ' * (depth-1) + '- ' + (tree.getNodeValue()))
    else:
      print (tree.getNodeValue())

    print_tree(tree.getLeftChild(),depth+1)

    print_tree(tree.getRightChild(),depth+1)
tree=BinaryTree("A")
tree.leftInsert("B")
tree.left.leftInsert("C")
tree.left.left.leftInsert("c1")
tree.left.left.left.leftInsert("c1child")
tree.left.left.rightInsert("c2")
tree.left.rightInsert("D")
tree.rightInsert("E")
tree.right.rightInsert("G")
tree.right.leftInsert("F")
print_tree(tree)
 
