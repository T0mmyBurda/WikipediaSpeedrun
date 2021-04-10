from wikipedia import *
from tkinter import *

window = Tk()
window.geometry("400x600")
window.title("Wikipedia Speedrun")

GAMEFONT = "arial"

pages = ["New York (state)" , "Yellowstone National Park" , "John Green (author)" , "Watchmen" , "Cheetos" ,
         "St. Barnabas Episcopal Church (Troy, New York)" , "Aphanius baeticus" , "Python (programming language)" ,
         "Ice pop"]

#print(wikipedia.random(pages=1))

def playGame():
    steps = 0

    curPage = ""

    startPage = wikipedia.random(pages=1)
    endPage = wikipedia.random(pages=1)

    banner = Label(window , text = startPage + " to " + endPage , bg="green")
    banner.pack(fill = BOTH)

    print("Get from " , startPage  , " to " , endPage)

    curPage = startPage

    while(curPage != endPage):
        page = wikipedia.page(curPage)
        links = page.links

        #clear()
        #print("Get from " , startPage  , " to " , endPage , "/n/n")
        print("HERE ARE ALL THE LINKS ON PAGE " , curPage , "/n")

        for num , link in enumerate(links):
            print(num , ":  " , link)

        print("ENTER THE NUMBER OF YOUR NEXT MOVE")
        inNum = input()
        curPage = links[int(inNum)]
        steps += 1

    print("congratuations! you got from " , startPage , " to " , endPage , " in " , steps , " steps")

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

playGame()