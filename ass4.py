
class Node:

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



main()