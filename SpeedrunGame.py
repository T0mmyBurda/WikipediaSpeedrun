from wikipedia import *

#ny = wikipedia.page("New York (state)")
#print(ny.links)

pages = ["New York (state)" , "Yellowstone National Park" , "John Green (author)" , "Watchmen" , "Cheetos" ,
         "St. Barnabas Episcopal Church (Troy, New York)" , "Aphanius baeticus" , "Python (programming language)" ,
         "Ice pop"]

#print("here")
print(wikipedia.random(pages=1))

def playGame():
    steps = 0

    curPage = ""

    #print("Enter the start page: ")
    #startPage = input()
    #print("Enter the end page: ")
    #endPage = input()

    startPage = wikipedia.random(pages=1)
    endPage = wikipedia.random(pages=1)

    print("Get from " , startPage  , " to " , endPage)

    curPage = startPage

    while(curPage != endPage):
        page = wikipedia.page(curPage)
        links = page.links

        print("ENTER THE NUMBER OF YOUR NEXT MOVE")

        for num , link in enumerate(links):
            print(num , ":  " , link)

        print("ENTER THE NUMBER OF YOUR NEXT MOVE")
        inNum = input()
        curPage = links[int(inNum)]
        steps += 1

    print("congratuations! you got from " , startPage , " to " , endPage , " in " , steps , " steps")



playGame()