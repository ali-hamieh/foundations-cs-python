
class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

      
def welcome():
  name = input(print("enter your name"))
  print("welcome" + name)

def singlyLinked():
    print("1.add node\n" +
         "2.desplay nodes\n" +
          "3.search and delete nodes\n" +
          "4.return to menue\n")

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