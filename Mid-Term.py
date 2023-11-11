






def addTab():
    dict = {}
    z = input(print("enter number of tabs "))
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
            pass
main()
