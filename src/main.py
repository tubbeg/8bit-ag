import pyxel


pyxel.init(160, 120)


def quit_game ():
    return pyxel.btnp(pyxel.KEY_ESCAPE) or pyxel.btnp(pyxel.KEY_Q)

def update():
    if quit_game():
        pyxel.quit()

def draw():
    pyxel.cls(254)
    pyxel.rect(10, 10, 20, 30, 0)

pyxel.run(update, draw)