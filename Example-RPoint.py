from REMOLib import *






#게임 오브젝트들을 선언하는 곳입니다.
class Obj:
    None

class mainScene(Scene):
    def initOnce(self):
        p = RPoint(0,0) ## RPoint is 2D Point used in REMO Library
        p += RPoint(30,30)
        p -= RPoint(15,15) ## it supports arithmetic operations
        p *= 2        
        print(p)
        self.mouse_pos = textObj(str(Rs.mousePos()),font = "BMJUA_ttf.ttf",color=Cs.yellow,angle=10,size=20,pos=RPoint(50,50)) ## textObj : object that represents text in the game
        ## you can set its (font)color, (font)size, angle(0~360),pos(position)

        return
    def init(self):
        return
    def update(self):
        self.mouse_pos.text = str(Rs.mousePos())
        self.mouse_pos.pos = Rs.mousePos()
        return
    def draw(self):
        Rs.fillScreen(Cs.black)
        self.mouse_pos.draw() ## draws current mouse position
        return


class defaultScene(Scene):
    def initOnce(self):
        return
    def init(self):
        return
    def update(self):
        return
    def draw(self):
        return

class Scenes:
    mainScene = mainScene()


if __name__=="__main__":
    #Screen Setting
    window = REMOGame((800,600),False,caption="DEFAULT")
    window.setCurrentScene(Scenes.mainScene)
    window.run()

    # Done! Time to quit.
