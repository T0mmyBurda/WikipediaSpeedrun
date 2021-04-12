from wikipedia import *
from tkinter import *

wikiBlue = "#A1C1FA"
offWhite = "#F7F6F6"
linkBlue = "#294DAC"

window = Tk()
window.geometry("400x600")
window.title("Wikipedia Speedrun")

linkGrid = Frame(window)

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

    banner = Label(window , text = startPage + " to " + endPage , bg=wikiBlue , fg="black" , font=(GAMEFONT , 20))
    banner.pack(fill = BOTH)

    redbutton = Button(window, text="Red", fg="red")
    greenbutton = Button(window, text="green", fg="green")
    #redbutton.grid(row = 0, column = 0, sticky = W, pady = 2)
    #greenbutton.grid(row = 1, column = 0, sticky = W, pady = 2)
    redbutton.pack()
    greenbutton.pack()

    mainloop()

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

        #b1 = Label(window , text = "text1" , bg=offWhite , fg="black" , font=(GAMEFONT , 20))
        #b1.pack(fill = X)
        #b2 = Label(window , text = "text2" , bg="white" , fg="black" , font=(GAMEFONT , 20))
        #b2.pack(fill = X)

        even = True #indexes at 0
        #while(len(links) >= 3):


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

def buttonPress():
    pass

playGame()