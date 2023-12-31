import urllib.request
import json

def load():  # #time complexity is O(N) n the length of list. in this function same as previous function (#7) but here after it is saved it will be extracted
    dict = {}  #to view the data that was saved in json format
    z = int(input(print("enter number of tabs ")))
    for i in range(z):
        x = input(print("enter website"))
        y = input(print("enter url"))
        dict[x] = [y]
    print(dict)
    l = input(print("enter file path + extension . json"))

    with open(l, "w") as outfile:
        json.dump(dict, outfile)

    with open(l) as f:
        data = f.read()

    js = json.loads(data)                              # code used here from: https://www.geeksforgeeks.org/how-to-read-dictionary-from
    print("the output of the file you saved", js)

def jSon(): #time complexity is O(N) n the length of list. in this fuction after the user enter data to dictionary .the user is promted to enter a file
    dict = {}  #name with .json extension to save the dictionay data in json format
    z = int(input(print("enter number of tabs ")))
    for i in range(z):
        x = input(print("enter website"))
        y = input(print("enter url"))
        dict[x] = [y]
    print(dict)

    l = input(print("enter file path + extension . json"))

    with open(l, "w") as outfile:       # code used here from: https://www.datasciencelearner.com/how-to-save-dict-as-json-in-python/
        json.dump(dict, outfile)


def clearAll():#time complexity is O(N) n the length of list. in this fuction the dict.clear will close all tabs of dict
    dict = {}
    z = int(input(print("enter number of tabs ")))
    for i in range(z):
        x = input(print("enter website"))
        y = input(print("enter url"))
        dict[x] = [y]
    print(dict)
    dict.clear()
    print("you are cleared" ,dict)


def printIndex(): #time complexity is O(N) n the length of loop. this function wil print all tabs. and the it loops to print the index or website nam
    dict = {}
    z = int(input(print("enter number of tabs ")))
    for i in range(z):
        x = input(print("enter website"))
        y = input(print("enter url"))
        dict[x] = [y]
    print(dict)
    for key, value in dict.items():
        print("The index is:", key)

def webScrap(): #time complexity is O(N) with n the length of the list . after entering the url's in dictionary .by using the index the user
  dict = {}     # will be able to webscrap the desired website
  z = int(input(print("enter number of tabs ")))
  for i in range(z):
      x = input(print("enter website"))
      y = input(print("enter url"))
      dict[x] = [y]
  print(dict)

  m = input(print("enter full address ex: http://www.python.org"))
  b = dict[(m)][0]
  print(b)
  fp = urllib.request.urlopen(b)    # i got this from https://www.edureka.co/blog/web-scraping-with-python/
  mybytes = fp.read()
  mystr = mybytes.decode("utf8")
  fp.close()
  print(mystr)


def closeTab(): #time complexity is O(N) with n the length of the list. here the uset enter or open as much tabs he want and then he can choose by
  dict = {}     #entering the desired index he wants to delete
  z = int(input(print("enter number of tabs ")))
  for i in range(z):
      x = input(print("enter website"))
      y = input(print("enter url"))
      dict[x] = [y]
  print(dict)
  m = input(print("enter website to delete"))
  del dict[m]
  print(dict)





def addTab(): #time complexity is O(N) with n the length of the list.in this fuction the user can add tabs to dictionary containing the website name and url and then print it to the user
    dict = {}
    z = int(input(print("enter number of tabs ")))
    for i in range(z):
        x = input(print("enter website"))
        y = input(print("enter url"))
        dict[x] = [y]
    print(dict)

def nest(): #time complexity is O(N) where is the length of list. here the user will enter nested tabs to a specific key or index of the dictionary
    Dict = {}    #and then print them all
    f = int(input(print("enter number of tabs ")))
    for i in range(f):
        x = input(print("enter website"))
        y = input(print("enter title"))
        z = input(print("enter content"))
        Dict[x] = {}
        Dict[x]['title'] = y
        Dict[x]['content'] = z
    print(Dict)






def displayMenu():# here is the meuu that was used to display the items in the main function
    print("1.Open Tab\n"  +
          "2.Cose Tab\n"   +
          "3.Switch Tab\n"  +
          "4.Display All Tabs\n" +
          "5.Open Nester Tabs\n"  +
          "6.Clear All Tabs\n"  +
          "7.Save Tabs\n"  +
          "8.Import Tabs\n"+
          "9.Exit\n")
    

def main(): #here i created the main menu to view the choices the user can use if the user chooses 9 the while loop will stop
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
            printIndex()
        elif choice == 5:
            nest()
        elif choice == 6:
            clearAll()
        elif choice == 7:
            jSon()
        elif choice == 8:
            load()
main()
