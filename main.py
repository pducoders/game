import pyglet
from pyglet.window import key
import itertools
from random import randint as random
from collections import Counter
# nothing other than import above here
# summons window
game_window = pyglet.window.Window(resizable=True, width=1200, height=300)
keys = key.KeyStateHandler()
game_window.push_handlers(keys)
# your player &rename it later
class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.shape = "cube"
        self.gravity = "down"
        self.prev_x = 0
        self.prev_y = 0

    # jump
    def jump(self):
        if self.gravity == "down":
            self.y += 1
            level1.anti_collide(None)
            self.y += 1
            level1.anti_collide(None)
            self.y += 1
            level1.anti_collide(None)
        else:
            self.y -= 1
            level1.anti_collide(None)
            self.y -= 1
            level1.anti_collide(None)
            self.y -= 1
            level1.anti_collide(None)

    # gravity
    def fall(self):
        if self.gravity == "down":
            self.y = self.y - 1
        else:
            self.y = self.y + 1

    # anti-collide which is called when the player is in a block
    def anti_collide(self):
        self.x = self.prev_x
        self.y = self.prev_y


class cat():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.gravity = "down"
        self.prev_x = 0
        self.prev_y = 0

    # jump
    def jump(self):
        if self.gravity == "down":
            self.y = self.y + 3
        else:
            self.y = self.y - 3

    # gravity
    def fall(self):
        if self.gravity == "down":
            self.y = self.y - 1
        else:
            self.y = self.y + 1

    # anti-collide
    def anti_collide(self):
        self.jump()


# topsoil &rename
class topsoil():
    def __init__(self, x, y):
        self.x = x
        self.y = y


# bricks useful &change to sprite
class water():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class leaf():
    def __init__(self, x, y):
        self.x = x
        self.y = y



class trunk():
    def __init__(self, x, y):
        self.x = x
        self.y = y


# &remove
class endPoint():
    def __init__(self, x, color):
        self.x = x
        self.color = color

class lava():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 75, 0)
class stone():
    def __init__(self, x, y):
        self.x = x
        self.y = y
class dirt():
    def __init__(self,x,y):
        self.x=x
        self.y=y
class flower():
    def __init__(self, x, y):
        self.x = x
        self.y = y
class cloud():
    def __init__(self, x, y):
        self.x = x
        self.y = y
blocksdict = dict()
inventory = Counter()
deepbricks = [topsoil(16, 2), topsoil(0, -1), topsoil(1, 0), topsoil(2, 0), topsoil(3, 0), topsoil(9, 0), topsoil(6, 0), topsoil(7, 0),
              topsoil(8, 0), topsoil(9, 0), topsoil(10, 0), topsoil(11, 0), topsoil(12, 0), topsoil(13, 0),
              topsoil(4, 0), topsoil(14, 0), topsoil(8, 0), topsoil(14, 6), topsoil(18, 0), topsoil(18, 3),
              topsoil(21, 2), topsoil(58, 13), topsoil(60, 13), topsoil(96, 0), topsoil(36, 2)]
# blocks cooridinates &rename make sprite
blocks = [water(5, 0), water(20, 3), water(68, 13), water(71, 13), water(71, 12), water(79, 8), water(95, 0), water(70, -2)]
trunks = [trunk(50, 0), trunk(50, -1), trunk(30, 0), trunk(30, -1), trunk(67, 0), trunk(67, -1), trunk(22, 0),
          trunk(22, -1), trunk(74, 0), trunk(74, -1), trunk(43, 0), trunk(43, -1), trunk(100, -1), trunk(100, 0),
          trunk(89, -1), trunk(89, 0), trunk(123, -1), trunk(123, 0), trunk(97, -1), trunk(97, -1), trunk(107, 0),
          trunk(107, -1), trunk(114, 0), trunk(114, -1), trunk(130, 0), trunk(130, -1)]
leaves = [leaf(50, 1), leaf(49, 1), leaf(51, 1), leaf(50, 2), leaf(22, 1), leaf(21, 1),
          leaf(23, 1), leaf(22, 2), leaf(30, 1), leaf(29, 1), leaf(31, 1), leaf(30, 2),
          leaf(43, 1), leaf(42, 1), leaf(44, 1), leaf(43, 2), leaf(67, 1), leaf(66, 1), leaf(68, 1), leaf(67, 2),
          leaf(74, 1), leaf(73, 1), leaf(75, 1), leaf(74, 2),
          leaf(89, 1), leaf(88, 1), leaf(90, 1), leaf(89, 2),
          leaf(100, 1), leaf(99, 1), leaf(101, 1), leaf(100, 2),
          leaf(107, 1), leaf(106, 1), leaf(108, 1), leaf(107, 2),
          leaf(114, 1), leaf(113, 1), leaf(115, 1), leaf(114, 2),
          leaf(123, 1), leaf(122, 1), leaf(124, 1), leaf(123, 2),
          leaf(130, 1), leaf(129, 1), leaf(131, 1), leaf(130, 2)]
# bricks
brickslist = [deepbricks, blocks, trunks, leaves]
for bricktype in brickslist:
    for brick in bricktype:
        blocksdict[(brick.x, brick.y)] = brick
# makes deep ground
def makedirt():
    for x,y in itertools.product(range(-1000, 1000), range(-10, -2)):
        blocksdict[(x,y)] = dirt(x,y)
def maketopsoil():
    for x in range(-1000,1000):
        blocksdict[(x,-2)] = topsoil(x,-2)
def makelava():
    for x,y in itertools.product(range(-1000, 1000), range(-30, -20)):
        blocksdict[(x,y)] = lava(x,y)
def makestone():
    for x,y in itertools.product(range(-1000, 1000), range(-20,-5)):
        blocksdict[(x,y)] = stone(x,y)
def makeflowers():
    for x in range(-1000,1000):
        if x % random(1,50) == 0:
            blocksdict[x,-1]=flower(x,-1)
makeflowers()
makelava()
maketopsoil()
makestone()
makedirt()
# makes all the stuff
class level():
    def __init__(self, deepbricks, end, player, blocks, cat, creatures, trunks, leaves, dict):
        self.deepbricks = deepbricks
        self.end = end
        self.player = player
        self.exploFrame = 0
        self.blocks = blocks
        self.cat = cat
        self.creatures = [self.cat, self.player]
        self.trunks = trunks
        self.leaves = leaves
        self.dict = blocksdict


    def movecamera(self, direction, amount):
        """for coords, blok in blocksdict.items():
            if direction == "down":
                blok.y += amount
            else:
                blok.y -= amount
        if direction == "down":
            self.player.y += amount
        else:
            self.player.y -= amount"""

    # dont walk into blocks
    def anti_collide(self, _):
        for creature in level1.creatures:
            for coords, blok in blocksdict.items():

                if creature.x == blok.x and creature.y == blok.y:
                    creature.anti_collide()

    # moving stuff
    def one_second(self, _):
        for creature in self.creatures:
            if self.creatureOnFloor(creature) == False:
                creature.fall()

    def movecat(self, _):
        if self.cat.x < self.player.x - 3:
            self.cat.x += 1
        if self.cat.x > self.player.x - 3:
            self.cat.x -= 1

    def mine(self, direction):
        if direction == "down":
            del blocksdict[self.player.x, self.player.y - 1]
            inventory["topsoil"] += 1
        if direction == "up":
            del blocksdict[self.player.x, self.player.y + 1]
            inventory["topsoil"] += 1
        if direction == "right":
            del blocksdict[self.player.x + 1, self.player.y]
            inventory["topsoil"] += 1
        if direction == "left":
            del blocksdict[self.player.x - 1, self.player.y]
            inventory["topsoil"] += 1
        print(inventory["topsoil"])
    def place(self, direction):
        if inventory["topsoil"] > 0:
            if direction == "down":
                blocksdict[(self.player.x, self.player.y - 1)] = topsoil(self.player.x, self.player.y - 1)
            if direction == "up":
                blocksdict[(self.player.x, self.player.y + 1)] = topsoil(self.player.x, self.player.y + 1)
            if direction == "left":
                blocksdict[(self.player.x + 1, self.player.y)] = topsoil(self.player.x + 1, self.player.y)
            if direction == "right":
                blocksdict[(self.player.x - 1, self.player.y)] = topsoil(self.player.x - 1, self.player.y)
            inventory["topsoil"] -= 1
    # stay on blocks &condense int one for loop
    def creatureOnFloor(self, creature):
        for coords, blok in blocksdict.items():
            if creature.y == blok.y + 1 and creature.x == blok.x:
                return True
        return False

    def auto_downscroll(self):
        self.movecamera("down", level1.player.y * -1 + 3)


# summons level
level1 = level(
    deepbricks=deepbricks,
    end=endPoint(140, (200, 150, 5)),
    player=Player(),
    blocks=blocks,
    cat=cat(),
    creatures=[cat(), Player()],
    trunks=trunks,
    leaves=leaves,
    dict=blocksdict,
)
# size of everything do not chnage
cube_size = 32


def update():
    game_window.clear()
    level1.auto_downscroll()
    camera = 0
    # defines images uses colin magic
    pyglet.shapes.Rectangle(level1.cat.x * cube_size - camera, level1.cat.y * cube_size + 10, cube_size,
                            cube_size, (0, 255, 100)).draw()
    for screen_x,screen_y in (itertools.product(range(game_window.width // cube_size), range(game_window.height // cube_size))):
        blok_cord = (level1.player.x-15+screen_x,level1.player.y-5+screen_y)
        if blok_cord in blocksdict:
            blok=blocksdict[blok_cord]
        else:continue
        if type(blok) == topsoil:
            pyglet.image.load("./assets/images/topsoil.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
        elif type(blok) == leaf:
            pyglet.image.load("./assets/images/leaves.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
        elif type(blok) == water:
            pyglet.image.load("./assets/images/water.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
        elif type(blok) == trunk:
            pyglet.image.load("./assets/images/wheatplanted.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
        elif type(blok) == stone:
            pyglet.image.load("./assets/images/stone.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
        elif type(blok) == lava:
            pyglet.shapes.Rectangle(screen_x * cube_size, screen_y * cube_size, cube_size, cube_size, blok.color).draw()
        elif type(blok) == dirt:
            pyglet.image.load("./assets/images/dirt.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
        elif type(blok) == flower:
            pyglet.image.load("./assets/images/flower.png").blit(screen_x * cube_size - camera, screen_y * cube_size)

            pyglet.shapes.Rectangle(15 * cube_size, 5 * cube_size, cube_size,
                                cube_size).draw()
def on_key_press(space, _):
    key = pyglet.window.key.symbol_string(space)
    level1.player.prev_x = level1.player.x
    level1.player.prev_y = level1.player.y
    if key == "UP":
        if level1.creatureOnFloor(level1.player):
            level1.player.jump()

    if key == "DOWN":
        if level1.creatureOnFloor(level1.player) == False:
            level1.player.fall()
    if key == "SLASH":
        level1.movecamera("down", 1)
    if key == "PERIOD":
        level1.mine("down")
    if key == "L":
        level1.movecamera("up", 1)
    if key == "P":
        level1.place("right")
    if key == "U":
        level1.place("left")
    if key == "I":
        level1.place("down")
    if key == "O":
        level1.place("up")
    if key == "W":
        level1.mine("up")
    if key == "D":
        level1.mine("right")
    if key == "A":
        level1.mine("left")
    if key == "S":
        level1.mine("down")
    if key == "V":
        print(level1.player.x)
        print(level1.player.y)
    if key =="G":
        print(inventory["topsoil"])
def leftrightmarker(_):
    if keys[key.LEFT]:
        level1.player.prev_x = level1.player.x
        level1.player.prev_y = level1.player.y
        level1.player.x -= 1
        level1.anti_collide(_)
    if keys[key.RIGHT]:
        level1.player.prev_x = level1.player.x
        level1.player.prev_y = level1.player.y
        level1.player.x += 1
        level1.anti_collide(_)
@game_window.event
def on_mouse_press(clickx, clicky, button, modifiers):
    adjustedx = int(clickx / 32) - 15 + level1.player.x
    adjustedy=int(clicky/32)-5+level1.player.y
    if button ==1:
        if inventory["topsoil"]>0:
            blocksdict[adjustedx,adjustedy]=topsoil(adjustedx,adjustedy)
            inventory["topsoil"]-=1
    if button ==4:
        del blocksdict[adjustedx,adjustedy]
# run it nothing below here expect for run
game_window.on_draw = update
game_window.on_key_press = on_key_press
pyglet.clock.schedule_interval(leftrightmarker, 0.1)
pyglet.clock.schedule_interval(level1.one_second, 0.5)
pyglet.clock.schedule_interval(level1.anti_collide, 0.05)
pyglet.clock.schedule_interval(level1.movecat, 0.5)
pyglet.app.run()
