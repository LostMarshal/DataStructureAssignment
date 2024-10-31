class Node:
  def __init__(self, value) :
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.count = 0

  def insert(self, value):
    new_node = Node(value)
    if self.root is None:
      self.root = new_node
      self.count += 1
      return True
    temp = self.root
    while (True):
      if new_node.value == temp.value:
        return False
      if new_node.value < temp.value:
        if temp.left is None:
          temp.left = new_node
          self.count += 1
          return True
        temp = temp.left
      else:
        if temp.right is None:
          temp.right = new_node
          self.count += 1
          return True
        temp = temp.right

  def contains(self,value):
    temp = self.root
    while (temp is not None):
      if value < temp.value:
        temp = temp.left
      elif value > temp.value:
        temp = temp.right
      else:
        return True
    return False

  def min_value_node(self, current_node):
    while current_node.left is not None:
      current_node = current_node.left
    return current_node

  def max_value_node(self, current_node):
    while current_node.right is not None:
      current_node = current_node.right
    return current_node

  def average_value_node(self, current_node):
    if current_node is None:
      return 0
    return (current_node.value + self.average_value_node(current_node.left) + self.average_value_node(current_node.right))

  def standard_deviation(self, current_node, mean):
    if current_node is None:
      return 0
    return ((current_node.value - mean) ** 2 + self.standard_deviation(current_node.left, mean) + self.standard_deviation(current_node.right, mean))

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('Standard Deviation in Tree:')
print((my_tree.standard_deviation(my_tree.root, my_tree.average_value_node(my_tree.root) / my_tree.count) / my_tree.count) ** 0.5)