---
### REMO Library in Pygame 
REMO Library is useful wrapper of the pygame library.
The Library is presented by Dano Sato in RealMono Inc.

REMO is an abbreviation of RealMono, so it means RealMono Library.

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

---
### License

REMO Library is under MIT License. For detail, watch license.txt file.

pygame is under LGPL License. The library doesn't change pygame code.
