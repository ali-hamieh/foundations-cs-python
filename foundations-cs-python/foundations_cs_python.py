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
      
  

def main():
    
    
    welcome()
    List()
    
    number = int(input(print("enter number")))

    if number == 1:
        matrixSum()
    else: print("exit")
             
        
main()
    

