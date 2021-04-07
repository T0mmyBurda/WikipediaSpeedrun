from wikipedia import *

ny = wikipedia.page("New York (state)")
print(ny.links)

def playGame():
    steps = 0

    curPage = ""

    print("Enter the start page: ")
    startPage = input()
    print("Enter the end page: ")
    endPage = input()

    curPage = startPage

    while(curPage != endPage):
        page = wikipedia.page(curPage)
        links = page.links

        print("ENTER THE NUMBER OF YOUR NEXT MOVE")

        for num , link in enumerate(links):
            print(num , ":  " , link)

        print("ENTER THE NUMBER OF YOUR NEXT MOVE")
        inNum = input()
        curPage = links[inNum]
        steps += 1

    print("congratuations! you got from " , startWord , " to " , endWord , " in " , steps , " steps")



playGame()