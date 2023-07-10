from REMOLib import *


#게임 오브젝트들을 선언하는 곳입니다.
class Obj:
    obj = imageObj.__new__(imageObj)
    obj2 = Rs.new(imageObj)
class mainScene(Scene):
    def initOnce(self):
        Rs.playMusic("peaceful.mp3",loops=-1)
        temp = pygame.Rect(0,0,200,50)
        mainScene.title = textObj("Example Game",(220,80),size=40)
        mainScene.b1 = textButton("Game Start",temp)
        mainScene.b2 = textButton("Settings",temp)
        mainScene.b3 = textButton("Credit",temp)
        mainScene.b4 = textButton("Exit",temp,color=Cs.dim(Cs.red))
        
        mainScene.layout = layoutObj(pygame.Rect(270,200,0,0),childs=[mainScene.b1,mainScene.b2,mainScene.b3,mainScene.b4])
        def goToCredit():
            REMOGame.setCurrentScene(Scenes.creditScene)
        def exitGame():
            REMOGame.exit()
        mainScene.b3.connect(goToCredit)
        mainScene.b4.connect(exitGame)
        return
    def init(cls):
        return

    def update(cls):
        #update childs
        #if child has update method, it updates child
        mainScene.layout.update()
        return
    def draw(cls):
        #draw childs
        Rs.fillScreen(Cs.mint)
        mainScene.title.draw()
        mainScene.layout.draw()
        return

class creditScene(Scene):
    def initOnce(self):
        Rs.acquireDrawLock()
        creditScene.authorTitle = textObj("Made by Dano Sato",(220,80),size=40)
        creditScene.backButton = textButton("Go Back",pygame.Rect(20,20,0,0))
        def goBack():
            REMOGame.setCurrentScene(Scenes.mainScene)
        creditScene.backButton.connect(goBack)
        Rs.ReleaseDrawLock()
        return

    def update(self):
        #update childs
        #if child has update method, it updates child
        creditScene.backButton.update()
        return
    def draw(self):
        #draw childs
        Rs.fillScreen(Cs.mint)
        creditScene.authorTitle.draw()
        creditScene.backButton.draw()
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
    creditScene = creditScene()


if __name__=="__main__":
    #Screen Setting
    window = REMOGame((800,600),False,caption="DEFAULT")
    REMOGame.setCurrentScene(Scenes.mainScene)
    window.run()

    # Done! Time to quit.
