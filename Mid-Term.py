import urllib.request



def webScrap():
  dict = {}
  z = int(input(print("enter number of tabs ")))
  for i in range(z):
      x = input(print("enter website"))
      y = input(print("enter url"))
      dict[x] = [y]
  print(dict)

  m = input(print("enter full address ex: http://www.python.org"))
  b = dict[(m)][0]
  print(b)
  fp = urllib.request.urlopen(b)
  mybytes = fp.read()
  mystr = mybytes.decode("utf8")
  fp.close()
  print(mystr)


def closeTab():
  dict = {}
  z = int(input(print("enter number of tabs ")))
  for i in range(z):
      x = input(print("enter website"))
      y = input(print("enter url"))
      dict[x] = [y]
  print(dict)
  m = input(print("enter website to delete"))
  del dict[m]
  print(dict)





def addTab():
    dict = {}
    z = int(input(print("enter number of tabs ")))
    for i in range(z):
        x = input(print("enter website"))
        y = input(print("enter url"))
        dict[x] = [y]
    print(dict)








def displayMenu():
    print("1.Open Tab\n"  +
          "2.Cose Tab\n"   +
          "3.Switch Tab\n"  +
          "4.Display All Tabs\n" +
          "5.Open Nester Tabs\n"  +
          "6.Clear All Tabs\n"  +
          "7.Save Tabs\n"  +
          "8.Import Tabs\n"+
          "9.Exit\n")
    

def main():
    displayMenu()
    choice = int(input(("enter choice")))
    while (choice !=9 ):
        if choice == 1:
            addTab()
        elif choice == 2:
            closeTab()
        elif choice == 3:
            webScrap()
        elif choice == 4:
            pass
main()
