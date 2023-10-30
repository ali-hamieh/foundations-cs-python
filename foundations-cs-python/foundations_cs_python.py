from token import NUMBER


def List():
    
 print ("press \n1 for Add matrices \n" + "2 to check rotation \n" +"3 invert dictionary \n" + "4 to convert Matrix to Dictionary \n" + "5 to Check Palindrom \n" + "5 search for element \n" + "7 to exit \n" )
 
def welcome():

 name = input(print("please enter your name"))
 print("welcome \t" + name) 
 
def matrixSum():
   m1 = []  
   m2 = []
   m3 = []

   row1 = int(input(print("enter number of row")))
   col1 = int(input(print ("enter number of column")))

   for row in range(row1):
      print("row", row)
      m1.append([])
      for col in range(col1):
       print("column", col)
       number = int(input("enter numbers "))
       m1[row].append(number)
   print(m1)    

   for row in range(row1):
     print("row", row)
     m2.append([])
     for col in range(col1):
      print("column", col)
      number = int(input("enter numbers "))
      m2[row].append(number)
   print(m2)    


   for row in range(row1):
      m3.append([])
      for col in range(col1):
       inx = m1[row][col] + m2[row][col]
       m3[row].append(inx)
   print(m3)
      
def inverse():
   m1 = []  
   m2 = []
  

   row1 = int(input(print("enter number of row")))
   col1 = int(input(print ("enter number of column")))

   for row in range(row1):
      print("row", row)
      m1.append([])
      for col in range(col1):
       print("column", col)
       number = int(input("enter numbers "))
       m1[row].append(number)
   print(m1)     
   
   for row in range(col1):
     print("row", row)
     m2.append([])
     for col in range(row1):
      print("column", col)
      number = int(input("enter numbers "))
      m2[row].append(number)
   print(m2)    
   
   for row in range(row1):
      for col in range(col1):
        if m1[row][col] == m2[col][row]:
             print ("yes")
        break


def apply():  
   dict = {}
   dict1 = {}
   for i in range(2):
     x=int(input(print("enter key")))
     y= input(print("enter name"))
     dict[x] = [y]
     dict1[y] = [x]
   print(dict)
   print(dict1)
   
def dction():
   def diction

m1 = []  
m2 = []
dict = {}

row1 = int(input(print("enter number of number of studenst")))

for row in range(row1):
 print("row", row)
 m1.append([])
 m2.append([])
   

def main():
    
    
    welcome()
    List()
    
    number = int(input(print("enter number")))

    if number == 1:
        matrixSum()
    elif number == 2:
          inverse()
    elif number == 3:
           apply()
    else: print("exit")
    
main()
    

