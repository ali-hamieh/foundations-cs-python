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
       number = int(input("enter numbers of first column"))
       m1[row].append(number)
     print(m1)    

     for row in range(row1):
       print("row", row)
        m2.append([])
      for col in range(col1):
       print("column", col)
       number = int(input("enter numbers of first column"))
       m2[row].append(number)
     print(m2 )


      for row in range(len(m1)):
       for col in range(len(m2)):
       m3[row][col] = m1[row][col] + m2[row][col]

      
  

def main():
    
    matrixSum()
    welcome()
    List()
   
main()
    

