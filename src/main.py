import pyxel # type: ignore


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

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("./res.pyxres")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width
        quit_game()

    def draw(self):
    
        pyxel.cls(12)
        pyxel.rect(10, 10, 20, 30, 25)
        move_image()


mloc = (0,0)
App()