try:
    import pygame
except:
    import os
    os.system('pip install pygame')
    import pygame
import random
import time

class Button():
    x ,y,wigth,hight,text= 0,0,0,0,'';
    xPos,yPos = 0,0
    spehal = False
    def __init__(self,x,y,xPos,yPos,wigth,hight,text):
        self.x=x
        self.y=y
        self.wigth=wigth
        self.hight=hight
        self.text = text
        self.xPos=xPos
        self.yPos=yPos

        if(text!=''):
            pygame.draw.rect(sc, (0, 0, 0), (x, y, wigth, hight))
            pygame.draw.rect(sc, (255, 15, 135), (x, y, wigth, hight),1)
            f1 = pygame.font.Font(None, 36)
            text = f1.render(text, 1, (180, 180, 180))
            place = text.get_rect(center=(x+50, y+50))
            sc.blit(text, place)
            self.spehal=False
        else:
            self.spehal=True
    def hit(self,clikX,clikY):
        if(clikX>self.x and clikY>self.y and clikX<self.x+100 and clikY<self.y+100):
            return True
        else:
            return False
    def getText(self):
        return self.text
    def getSpehal(self):
        return self.spehal

    
def randomPos():
    global table
    for o in range(100):
        x,y=-1,-1
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j]=='':
                    x,y=i,j
        arr = []
        if(x!=0):
            arr.append(table[x-1][y])
        if(y!=0):
            arr.append(table[x][y-1])
        if(x!=3):
            arr.append(table[x+1][y])
        if(y!=3):
            arr.append(table[x][y+1])
        item = random.choice(arr)
        print(arr)
        for i in buttonArr:
            if i.getText()==item:
                print(type(i))
                change(i)
                break
        arr=[]
        item=''
def change(btn):
    x,y=-1,-1
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j]=='':
                x,y=i,j
    if(btn.xPos==x and y==btn.yPos+1 or btn.xPos+1==x and y==btn.yPos or btn.xPos==x and y==btn.yPos-1 or btn.xPos-1==x and y==btn.yPos):
        table[x][y],table[btn.xPos][btn.yPos]=table[btn.xPos][btn.yPos],table[x][y]
        update()
        
def update():
    global buttonArr
    global noneBtn
    buttonArr = []
    sc.fill((255, 255, 255)) 
    pygame.draw.rect(sc, (0, 0, 0), (47,47, 406, 406),3)
    f1 = pygame.font.Font(None, 36)
    for i in range(len(table)):
        for j in range(len(table[i])):
            buttonArr.append(Button(j*100+50, i*100+50,i,j, 100, 100,table[i][j]))
            if(table[j][i]==''):
                noneBtn = buttonArr[len(buttonArr)-1]
    pygame.display.update()

buttonArr = []
textBtn = None

table = [[ '1', '2', '3', '4'],
         [ '5', '6', '7', '8'],
         [ '9','10','11','12'],
         [ '13','14','15', '']]
tableFinal = [[ '1', '2', '3', '4'],
         [ '5', '6', '7', '8'],
         [ '9','10','11','12'],
         [ '13','14','15', '']]
pygame.init()
 
sc = pygame.display.set_mode((500,500))
sc.fill((255, 255, 255))

update()

randomPos()


while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                for j in buttonArr:
                    if(j.hit(i.pos[0],i.pos[1])):
                        if(j.getSpehal()!=True):
                            textBtn = j
                        break
    #print(type(textBtn),type(noneBtn))
    if(noneBtn != None and textBtn!=None):
        change(textBtn)
        textBtn = None
    if(tableFinal==table):
        print("YRAA")
    time.sleep(0.01)
        
        
