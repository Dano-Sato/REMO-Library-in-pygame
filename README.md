---
### REMO Library in Pygame 
REMO Library is useful wrapper of the pygame library that would make your game-making easier.
The Library is presented by Dano Sato in RealMono Inc.

REMO is an abbreviation of RealMono, so it means RealMono Library.

You can download REMOLib.py in this repo and include the functions by adding this one line in your python code;

```python
from REMOLib import *
```

Or cloning this repo might be help;

```
git clone https://github.com/Dano-Sato/REMO-Library-in-pygame
```

---
### Features

It supports scene control, and useful 2D graphic objects in pygame.

```python
class mainScene(Scene):
    def initOnce(self):
        ###Fill in the functions
        return
    def init(self):
        return
    def update(self):
        return
    def draw(self):
        return
```

It supports image, text, sprite, grid, layout, button, slider objects

```python
Obj.me = imageObj("test_me.png",pos=(50,50))
self.indicator = textObj("Don't Eat Me!")
```

It supports user I/O and smart path finding

```python
Rs.userJustPressed(pygame.K_z)
Rs.userJustLeftClicked()
Rs.userPressing(pygame.K_UP)
```


It is an efficient 2D Game Library. 3D calculation is not supported.

Example files included, will be updated soon.

The following code is one of the example game, it is simply an eating game.

```python
from REMOLib import *

#Global Game Objects 
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
        ## if you make different file that has same name and extension, and in different directories, it would cause file conflicts. (* the conflicts would be mentioned in your terminal)
        ## in that case you must specify it's detailed path like "Resources/Examples/test.png". I'd recommend not to use the same name for your game assets.
        ###

        Obj.prey = imageObj("test_prey.png",pos=(300,300),scale=0.3)
        self.indicator = textObj("Don't Eat ME!")
        self.indicator.setParent(Obj.prey)
        self.indicator.pos =RPoint(0,-30)
        self.score = textObj("SCORE:0",(200,50))
        return
    def init(self):
        return
    
    def setScore(self,s):
        self.score.text = "SCORE:{0}".format(str(s))

    def getScore(self):
        return int(self.score.text.split(":")[-1])

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

        ## you eat prey
        if Obj.me.center.distance(Obj.prey.center) < 55:
            self.setScore(self.getScore()+10)
            r1 = random.randint(100,700)

            r2 = random.randint(100,500)
            Obj.prey.center = (r1,r2)


        if Rs.userJustLeftClicked():
            print(Rs.mousePos())

        return
    def draw(self):
        #draw childs
        Rs.fillScreen(Cs.black)
        Rs.drawBenchmark() # shows the game fps
        Obj.prey.draw()
        Obj.me.draw()
        self.score.draw()
        return

class Scenes:
    mainScene = mainScene()


if __name__=="__main__":
    #Screen Setting
    window = REMOGame((800,600),False,caption="DEFAULT")
    window.setCurrentScene(Scenes.mainScene)
    window.run()

    # Done! Time to quit.
```

If you execute the code with resources included, result is this;
![](https://github.com/Dano-Sato/REMO-Library-in-pygame/blob/main/example_game.gif)


---
### License

REMO Library is under MIT License. For detail, watch license.txt file.

pygame is under LGPL License. The library doesn't change pygame code.
