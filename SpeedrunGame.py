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
         "Yoshi" , "Aphanius baeticus" , "Python (programming language)" , "Frindle" , "Yoda" , "Toaster" ,
         "Ice pop"]

startPage = ""
endPage = ""
curPage = ""
links = []
linkNum = 0

def linkClicked(button):
    curPage = button
    if(curPage = endPage):
        gameEnd()
    else:
        print("New Page: " , curPage)
        loadLinks(curPage)

def startGame():

    steps = 0
    curPage = ""

    startPage = wikipedia.random(pages=1)
    endPage = wikipedia.random(pages=1)

    banner = Label(window , text = startPage + " to " + endPage , bg=wikiBlue , fg="black" , font=(GAMEFONT , 20) , width=45)
    banner.grid(row=0 , column=0 , columnspan=3)

    print("Get from " , startPage  , " to " , endPage)

    curPage = startPage

    while(curPage != endPage):
        page = wikipedia.page(curPage)
        links = page.links

        #print("HERE ARE ALL THE LINKS ON PAGE " , curPage , "/n")

        for num , link in enumerate(links):
            print(num , ":  " , link)

        even = True #indexes at 0
        numCol = 3
        numRows = len(links) // numCol

        linkMat = []
        
        linkNum = 0
        for i in range(numRows):
            row = []
            for j in range(3):
                nextButton = 'Button(window , text="' + links[linkNum] + '" , padx=0 , pady=0 , width=15 , command=lambda:linkClicked("' + links[linkNum] + '"))'
                row.append(eval(nextButton))
                linkNum += 1
            linkMat.append(row)

        #print(linkMat)

        for row in range(numRows):
            for col in range(3):
                linkMat[row][col].grid(row=row + 1 , column=col)

        window.mainloop()

#       print("ENTER THE NUMBER OF YOUR NEXT MOVE")
#       inNum = input()
#        curPage = links[int(inNum)]
#        steps += 1

#   print("congratuations! you got from " , startPage , " to " , endPage , " in " , steps , " steps")

def loadLinks(curPage):

    page = wikipedia.page(curPage)
    links = page.links
   
    for num , link in enumerate(links):
        print(num , ":  " , link)

    even = True #indexes at 0
    numCol = 3
    numRows = len(links) // numCol

    linkMat = []
        
    linkNum = 0
    for i in range(numRows):
        row = []
        for j in range(3):
            nextButton = 'Button(window , text="' + links[linkNum] + '" , padx=0 , pady=0 , width=15 , command=lambda:linkClicked("' + links[linkNum] + '"))'
            row.append(eval(nextButton))
            linkNum += 1
        linkMat.append(row)

    print(linkMat)

    for row in range(numRows):
        for col in range(3):
            linkMat[row][col].grid(row=row + 1 , column=col)


    print("ENTER THE NUMBER OF YOUR NEXT MOVE")
    inNum = input()
    curPage = links[int(inNum)]
    steps += 1

def gameEnd:
    print("You Win, Game has ended!!!")
    window.destroy()

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def buttonPress():
    pass

startGame()