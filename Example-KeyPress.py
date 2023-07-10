from REMOLib import *






#게임 오브젝트들을 선언하는 곳입니다.
class Obj:
    me = Rs.new(imageObj)
    prey = Rs.new(imageObj)
    speed = 5

class mainScene(Scene):
    def initOnce(self):
        Obj.me = imageObj("test_me.png",pos=(50,50)) 

        ###
        ## When you load file in REMO Library, you can just type it's name. you don't have to specify it's folder. 
        ## for example, "test_me.png" file is in "Resources/examples" directory. the Library would automatically find it.
        ## for who wants the algorithm, watch _buildPath function in REMOLib.py
        ###

        Obj.prey = imageObj("test_prey.png",pos=(300,300))
        self.score = textObj("SCORE:0",(200,50))
        return
    def init(self):
        return

    def update(self):
        if Rs.userPressing(pygame.K_UP): ## if user is pressing up key in the keyboard
            Obj.me.pos+=RPoint(0,-Obj.speed) ## me object will move upward
            Obj.me.angle=180
        elif Rs.userPressing(pygame.K_DOWN):
            Obj.me.pos+=RPoint(0,Obj.speed)
            Obj.me.angle=0
        elif Rs.userPressing(pygame.K_LEFT):
            Obj.me.pos+=RPoint(-Obj.speed,0)
            Obj.me.angle=270

        elif Rs.userPressing(pygame.K_RIGHT):
            Obj.me.pos+=RPoint(Obj.speed,0)
            Obj.me.angle=90

        #update childs
        #if child has update method, it updates child
        return
    def draw(self):
        #draw childs
        Rs.fillScreen(Cs.black)
        Obj.me.draw()
        self.score.draw()
        return


class defaultScene(Scene):
    def initOnce(self):
        return
    def init(self):
        return
    def update(self):
        #update childs
        #if child has update method, it updates child
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
