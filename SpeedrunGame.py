from wikipedia import *
from tkinter import *
import random

wikiBlue = "#A1C1FA"
offWhite = "#F7F6F6"
linkBlue = "#294DAC"

window = Tk()
window.geometry("550x600")
window.title("Wikipedia Speedrun")

linkGrid = Frame(window)

GAMEFONT = "arial"

pages = ["New York (state)" , "Yellowstone National Park" , "John Green (author)" , "Watchmen" , "Cheetos" ,
         "Yoshi" , "Aphanius baeticus" , "Python (programming language)" , "Frindle" , "Yoda" , "Toaster" ,
         "Ice pop" , "Fast & Furious" , "DreamWorks Animation" , "Car Town" , "Android OS"]

startPage = random.choice(pages)
endPage = random.choice(pages)

while(endPage == startPage):
    endPage = random.choice(pages)

#easy start & end for testing 
#startPage = "Fast & Furious"
#endPage = "Car Town"

curPage = ""
links = []
linkNum = 0
steps = 0

def linkClicked(button):
    curPage = button
    print("End = " , endPage , "   Cur = " , curPage)
    if(curPage == endPage):
        gameEnd()
    else:
        print("New Page: " , curPage)
        loadLinks(curPage)

def startGame():

    #startPage = wikipedia.random(pages=1)
    #endPage = wikipedia.random(pages=1)

    #startPage = random.choice(pages)
    #endPage = random.choice(pages)

    #startPage = "Fast & Furious"
    #endPage = "Car Town"

    #while(endPage == startPage):
    #    endPage = random.choice(pages)

    banner = Label(window , text = startPage + " to " + endPage , bg=wikiBlue , fg="black" , font=(GAMEFONT , 20) , width=45)
    banner.grid(row=0 , column=0 , columnspan=3)

    print("Get from " , startPage  , " to " , endPage)

    curPage = startPage

    while(curPage != endPage):
        page = wikipedia.page(curPage)
        links = page.links

        print("HERE ARE ALL THE LINKS ON PAGE " , curPage , "/n")

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

def loadLinks(curPage):

    #steps += 1

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


    for row in range(numRows):
        for col in range(3):
            linkMat[row][col].grid(row=row + 1 , column=col)

    window.mainloop()


    print("ENTER THE NUMBER OF YOUR NEXT MOVE")
    inNum = input()
    curPage = links[int(inNum)]
    steps += 1

def gameEnd():
    print("You Win, Game has ended!!!")
    window.destroy()

    endWindow = Tk()
    endWindow.geometry("200x55")
    endWindow.title("Wikipedia Speedrun")

    banner = Label(endWindow , text = "Congratulations," , bg=wikiBlue , fg="black" , font=(GAMEFONT , 20) , width=45)
    banner.pack()

    banner = Label(endWindow , text = "You Win!" , bg=wikiBlue , fg="black" , font=(GAMEFONT , 20) , width=45)
    banner.pack()

    #stepLab = Label(endWindow , text = ("It took you " + str(steps) + " steps") , bg=wikiBlue , fg="black" , font=(GAMEFONT , 20) , width=45)
    #stepLab.pack()

startGame()
