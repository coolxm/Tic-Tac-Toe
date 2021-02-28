import sys, pygame, time, os
pygame.init()

size = width, height = 900, 900

Player = 1
winner = False

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue =  0, 0, 255
color = red
borderLimit = width / 37

lines = {
    1 : [(width / 3, borderLimit), (width / 3, height - borderLimit)],
    2 : [(2 * width / 3, borderLimit), (2 * width / 3, height - borderLimit)],
    3 : [(borderLimit, height / 3), (width-borderLimit, height / 3)],
    4 : [(borderLimit, 2 * height / 3), (width-borderLimit, 2 * height / 3)]
}

vakken = {
    1 : {'x' : [(borderLimit, height / 3), (width / 3, height / 3)], 'y' : [(width / 3, height / 3), (width / 3, borderLimit)], "isTrue" : False},
    2 : {'x' : [(width / 3, height / 3), (2 * width / 3, height / 3)], 'y' : [(2 * width / 3, height / 3), (2 * width / 3, borderLimit)], "isTrue" : False},
    3 : {'x' : [(2 * width / 3, height / 3), (width - borderLimit, height / 3)], 'y' : [(width - borderLimit, height / 3), (width - borderLimit, borderLimit)], "isTrue" : False},

    4 : {'x' : [(borderLimit, 2 * height / 3), (width / 3, 2 * height / 3)], 'y' : [(width / 3, 2 * height / 3), (width / 3, height / 3)], "isTrue" : False},
    5 : {'x' : [(width / 3, 2 * height / 3), (2 * width / 3, 2 * height / 3)], 'y' : [(2 * width / 3, 2 * height / 3), (2 * width / 3, height / 3)], "isTrue" : False},
    6 : {'x' : [(2 * width / 3, 2 * height / 3), (width - borderLimit, 2 * height / 3)], 'y' : [(width - borderLimit, 2 * height / 3), (width - borderLimit, height / 3)], "isTrue" : False},
    
    7 : {'x' : [(borderLimit, height - borderLimit), (width / 3, height - borderLimit)], 'y' : [(width / 3, height - borderLimit), (width / 3, 2 * height / 3)], "isTrue" : False},
    8 : {'x' : [(width / 3, height - borderLimit), (2 * width / 3, height - borderLimit)], 'y' : [(2 * width / 3, height - borderLimit), (2 * width / 3, 2 * height / 3)], "isTrue" : False},
    9 : {'x' : [(2 * width / 3, height - borderLimit), (width - borderLimit, height - borderLimit)], 'y': [(width - borderLimit, height - borderLimit), (width - borderLimit, 2 * height / 3)], "isTrue" : False},
}


screen = pygame.display.set_mode(size)

#events
def Event(event):
    if event.type == pygame.QUIT: sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        return True

def getVak():
    pos = pygame.mouse.get_pos()
    if vakken[1]["y"][1][1] <= pos[1] <= vakken[1]["y"][0][1]:
        print("row a")
        
        if vakken[1]["x"][0][0] <= pos[0] <= vakken[1]["x"][1][0]:
            print("column 1")
            return(1)
        elif vakken[2]["x"][0][0] <= pos[0] <= vakken[2]["x"][1][0]:
            print("column 2")
            return(2)
        elif vakken[3]["x"][0][0] <= pos[0] <= vakken[3]["x"][1][0]:
            print("column 3")
            return(3)

    elif vakken[4]["y"][1][1] <= pos[1] <= vakken[4]["y"][0][1]:
        print("row b")

        if vakken[4]["x"][0][0] <= pos[0] <= vakken[4]["x"][1][0]:
            print("column 1")
            return(4)
        elif vakken[5]["x"][0][0] <= pos[0] <= vakken[5]["x"][1][0]:
            print("column 2")
            return(5)
        elif vakken[6]["x"][0][0] <= pos[0] <= vakken[6]["x"][1][0]:
            print("column 3")
            return(6)

    elif vakken[7]["y"][1][1] <= pos[1] <= vakken[7]["y"][0][1]:
        print("row c")

        if vakken[7]["x"][0][0] <= pos[0] <= vakken[7]["x"][1][0]:
            print("column 1")
            return(7)
        elif vakken[8]["x"][0][0] <= pos[0] <= vakken[8]["x"][1][0]:
            print("column 2")
            return(8)
        elif vakken[9]["x"][0][0] <= pos[0] <= vakken[9]["x"][1][0]:
            print("column 3")
            return(9)
    else:
        return False

def placeSign(vak):
    global Player
    if Player == 1:
        DrawCircle(vak)
    if Player == 2:
        DrawCross(vak)

def Checkwinner():
    global winner
    for i in range(1,10, 3):
        if vakken[i]["isTrue"] == "circle"and vakken[i + 1]["isTrue"] == "circle" and vakken[i + 2]["isTrue"] == "circle":
            winner = red
        elif vakken[i]["isTrue"] == "cross" and vakken[i + 1]["isTrue"] == "cross" and vakken[i + 2]["isTrue"] == "cross":
            winner = green

    for i in range(1, 4, 1):
        if vakken[i]["isTrue"] == "circle" and vakken[i + 3]["isTrue"] == "circle" and vakken[i + 6]["isTrue"] == "circle":
            winner = red
        elif  vakken[i]["isTrue"] == "cross" and vakken[i + 3]["isTrue"] == "cross" and vakken[i + 6]["isTrue"] == "cross":
            winner = green
    
    if vakken[1]["isTrue"] == "circle" and vakken[5]["isTrue"] == "circle" and vakken[9] == "circle":
        winner = red
    elif vakken[1]["isTrue"] == "cross" and vakken[5]["isTrue"] == "cross" and vakken[9] == "cross":
        winner = green
    elif vakken[3]["isTrue"] == "circle" and vakken[5]["isTrue"] == "circle" and vakken[7] == "circle":
        winner = red
    elif vakken[3]["isTrue"] == "cross" and vakken[5]["isTrue"] == "cross" and vakken[7] == "cross":
        winner = green
    return winner
        
#drawing
def DrawLine(i, color):
    pygame.draw.line(screen, color, lines[i][0], lines[i][1], 3)

widthVak = width / 3
heightVak = height / 3

def DrawCircle(vak):
    vakken[vak]["isTrue"] = "circle"
    centerX = vakken[vak]["x"][0][0] + width / 6
    centerY = vakken[vak]["y"][1][1] + height / 6
    center = (int(centerX), int(centerY))
    radius = (width / 13)
    pygame.draw.circle(screen, red, center, radius, 5)

def DrawCross(vak):
    vakken[vak]["isTrue"] = "cross"

    #right to left
    startPos = (vakken[vak]["x"][0][0], vakken[vak]["y"][0][1] - 10)   #bottom Left
    endPos = (vakken[vak]["x"][1][0], vakken[vak]["y"][1][1] + 10)     #Top Right
    pygame.draw.line(screen, green, startPos, endPos, 5)

    #left to right
    startPos = (vakken[vak]["x"][0][0] + widthVak, vakken[vak]["y"][0][1] - 10)
    endPos = (vakken[vak]["x"][1][0] - widthVak, vakken[vak]["y"][1][1] + 10)     #top left
    pygame.draw.line(screen, green, startPos, endPos, 5)

def restart():
    print("restart")
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 

def onStart():
    global color
    global Player
    global winner
    Player = 1
    r = 0
    while 1:  
        x = 0
        for event in pygame.event.get():
            ev = Event(event)

            if ev:
                vak = getVak()
                if not vak == False:
                    if not vakken[vak]["isTrue"]:
                        placeSign(vak)
                        if Player == 1:
                            Player = 2
                        else:
                            Player = 1
        
        screen.fill(black)
        if Player == 1:
            color = red
        elif Player == 2:
            color = green

        for i in range(1,10):
            
            if not vakken[i]["isTrue"]:
                break
            elif vakken[i]["isTrue"] == "circle":
                DrawCircle(i)
                x = x + 1
            elif vakken[i]["isTrue"] == "cross":
                DrawCross(i)
                x = x + 1
            
        if x == 9:
            restart()

        for i in range(1,5):
            DrawLine(i, color)

        if not not Checkwinner():
            screen.fill(winner)
            pygame.display.flip()
            time.sleep(1)
            screen.fill(black)
            pygame.display.flip()
            time.sleep(1)
            
            r = r+1
            if r     == 2:
                restart()


        pygame.display.flip()

while True:       
    onStart()