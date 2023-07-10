from REMOLib import *


#Global Game Objects 
class Obj:
    obj = imageObj.__new__(imageObj)
    obj2 = Rs.new(imageObj)


## The Scene class has initOnce, init, update, draw function in it
## you can load Scene by Rs.setCurrentScene function
## in default the game has an update loop (60fps), so update funtion will be loaded for every 1/60 second
## the game loads draw function as a different thread so sometimes it requires thread lock 
## initOnce function is executed when the scene is first loaded, and after that happens it would never called again.
## init function is executed when the scene is loaded.

class mainScene(Scene):
    def initOnce(self):
        Rs.playMusic("peaceful.mp3",loops=-1) ## play "peaceful.mp3" in "Resources/examples" folder. loops=-1 means it loops endlessly.
        temp = pygame.Rect(0,0,200,50)
        mainScene.title = textObj("Example Game",(220,80),size=40) ## game Title text Object
        mainScene.b1 = textButton("Game Start",temp) ## text Buttons for main Scene
        mainScene.b2 = textButton("Settings",temp)
        mainScene.b3 = textButton("Credit",temp)
        mainScene.b4 = textButton("Exit",temp,color=Cs.dim(Cs.red))
        
        mainScene.layout = layoutObj(pygame.Rect(270,200,0,0),childs=[mainScene.b1,mainScene.b2,mainScene.b3,mainScene.b4])
        def goToCredit():
            REMOGame.setCurrentScene(Scenes.creditScene)
        def exitGame():
            REMOGame.exit()
        mainScene.b3.connect(goToCredit) ## when you click the button, the connected function will be executed
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
    window = REMOGame((800,600),False,caption="DEFAULT") ## resolution, fullscreen, caption
    REMOGame.setCurrentScene(Scenes.mainScene) ## loads the mainScene
    window.run()

    # Done! Time to quit.
