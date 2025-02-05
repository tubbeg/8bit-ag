import pyxel 
import esper 

def quit_game ():
    if pyxel.btnp(pyxel.KEY_ESCAPE) or pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def move_image():
    global mloc
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        mloc = (pyxel.mouse_x, pyxel.mouse_y)
    (x,y) = mloc
    pyxel.blt(x,y,0, 0,0, 15,15, 0, 180)

# blt(x, y, img, u, v, w, h, [colkey], [rotate], [scale])
# x y is the position in your game
# img is which "page" in your image bank
# u v is the position in the bank (i think)
# colkey: is the color which will be transparent, for instance:
#   if your image background (in the image bank) is black then
#   setting colkey to 0 will make all black colors transparent (actually quite useful)
# rotation in degrees
# scale up to 1.0 (100 %)


#bltm(x, y, tm, u, v, w, h, [colkey], [rotate], [scale])


# so it seems that I can't load multiple resource files
# i think it just switches between resources
# so you can only use 1 resource per scene as far as I know.
# It's a limitation for sure...but that's not necessarily a bad thing


# Now that I have figured out how to use simple tilemaps and sprites,
# it should be fairly easy to employ esper Entity Component System

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("./assets.pyxres")
        self.x = 0
        #self.my_player = PlayerSprite()
        pyxel.run(self.update, self.draw)

    def update(self):
        quit_game()

    def draw(self):
        pyxel.cls(3)
        pyxel.bltm(0,0,0,0,0,128,128)
        move_image()


mloc = (0,0)
App()