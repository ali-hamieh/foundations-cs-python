class Graph:

  def __init__(self, number_vertices):
    self.number_vertices = num_vertices
    self.adj_matrix = [[0] * number_vertices for _ in range(number_vertices)]

  def addVertex(self):
      self.number_vertices += 1
      for row in self.adj_matrix:
          row.append(0)
      self.adj_matrix.append([0] * self.number_vertices)
      print( self.number_vertices - 1, )

  def addEdge(self, v1, v2):
      if 0 <= v1 < self.number_vertices and 0 <= v2 < self.number_vertices:
          self.adj_matrix[v1][v2] = 1
          self.adj_matrix[v2][v1] = 1
          print( v1, "and", v2, "\n")

      elif ((v1 < 0 or v1 >= self.number_vertices)
            and (v2 < 0 or v2 >= self.number_vertices)):
          print("Invalid ", v1, "and", v2, "\n")
      elif (v1 < 0 or v1 >= self.number_vertices):
          print("vertex invalid", v1, "\n")
      else:
          print("vertex invalid", v2, "\n")

  def displayGraph(self):
      if len(self.adj_matrix) == 0:
          print("Graph is empty!\n")
          return
      for row in self.adj_matrix:
          print(" ".join(map(str, row)))



  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:

  def __init__(self):
    self.head = None
    self.size = 0


def addNode(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    self.size += 1


def displayNodes(self):
    temp = self.head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


def welcome():
  name = input(print("enter your name"))
  print("welcome" + name)

def singlyLinked():
    print("1.add node\n" +
         "2.desplay nodes\n" +
          "3.search and delete nodes\n" +
          "4.return to menue\n")

 ll = LinkedList()
  nodesNumber = int(input(print("number of nodes")))
   for i in range(nodesNumber):
      nod = int(input(print("enter node")))
      ll.addNode(nod)

   ll.displayNodes()


def displayMenu2():

    print("1.add node\n"  +
         "2.desplay nodes\n"   +
         "3.search and delete nodes\n"  +
          "4.return to menue\n" )

def displayMenu():

    print("1.singly linked list\n"  +
          "2.Check if plaindrome\n"   +
          "3.priority queue\n"  +
          "4.evaluate an infix expression\n" +
          "5.Graph\n"  +
          "6.exit\n")

def plaindrom():
    s = input("enter string")
    if (s == s[::-1]):
        print("yes")
    else:
        print("no")

class student:

def __init__(self,name, mgrade, fgrade, attitude):
  self.name = name
  self.mgrade = mgrade
  self.fgrade = fgrade
  self.attitude = attitude

class Node:

def __init__(self, data):
  self.data = data
  self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

def enqueue(self, value):

node = Node(value)
if self.size == 0:
  self.head = node
  self.tail = node
  self.size += 1
else:
  self.tail.next = node
  self.tail = node
  self.size += 1
print(" student added", node.info)

def main():
 welcome()
 displayMenu()
 choice = int(input(print("enter choice")))
 while (choice != 6):
      if choice == 1:
          singlyLinked()
      elif choice == 2:
          pass
      elif choice == 3:
          pass
      elif choice == 4:
          pass
      elif choice == 5 :
          pass
      elif choice == 6:
          pass



main()