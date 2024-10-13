import pyglet
from pyglet.window import key
import os
#no code above here other than import
window=pyglet.window.Window()
keys = key.KeyStateHandler()
window.push_handlers(keys)

images=dict()
for file in os.listdir("./assets"):
    images[file] = pyglet.image.load("./assets/"+file)

ground = []
for x in range (30):
    ground.append(pyglet.sprite.Sprite(images["image25.png"], x*13, 0))


def on_draw():
    for tile in ground:
        tile.draw()
    pass








#]:~—~Names~—~:[#
#dont mess with stuff on other peoples line !! so dont use control z ever
# also if you want to type gibberish type in here not in the code
#{&~~:AVNI("Yellow"):~~&}#<[$(@^💾^*~|~*^💻^*~|~*^💿^*~|~*^⌨^*~|~*^🖱^@)$]>
#rosa :3:3:3 idk how to do python r.i.p. me ig & $$$$$$
#ayda
#sylvia|〜(￣▽￣〜)
#colin ,}{...}[oter]/\?:"fnf"%%*,90+?&&&&@><^><#$$||}}}^^?27;;::''''>>><<<)("<">"!\\/:$?&?%?@?!?*?^?***K-boi
#colin2>>&
#ridge | (づ￣ u￣)づ
#finley
#
#this is the very bottom nothing below other than run
window.on_draw=on_draw
pyglet.app.run()