from itertools import zip_longest
from time import sleep
import time
import pyglet
from pyglet.window import key
import itertools
from random import randint as random
from collections import Counter
# nothing other than import above here
game_start_time=time.time()
# summons window
game_window = pyglet.window.Window(resizable=True, width=1200, height=300)
keys = key.KeyStateHandler()
game_window.push_handlers(keys)
# your player &rename it later
class Player:
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
class cat:
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


# topsoil &rename
class topsoil:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# bricks useful &change to sprite
class water:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class leaf:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class trunk:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# &remove
class endPoint:
    def __init__(self, x, color):
        self.x = x
        self.color = color

class lava:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 75, 0)
class stone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class dirt:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class flower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class diamondore:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class emeraldore:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class rubyore:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class goldore:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class coal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class cabbage:
    def __init__(self,x,y):
        self.x= x
        self.y=y
blocksdict = dict()
inventory = Counter()
blok_in_hand=topsoil
deepbricks = [topsoil(16, 2), topsoil(0, -1), topsoil(1, 0), topsoil(2, 0), topsoil(3, 0), topsoil(9, 0), topsoil(6, 0), topsoil(7, 0),
              topsoil(8, 0), topsoil(9, 0), topsoil(10, 0), topsoil(11, 0), topsoil(12, 0), topsoil(13, 0),
              topsoil(4, 0), topsoil(14, 0), topsoil(8, 0), topsoil(14, 6), topsoil(18, 0), topsoil(18, 3),
              topsoil(21, 2), topsoil(58, 13), topsoil(60, 13), topsoil(96, 0), topsoil(36, 2)]
# blocks cooridinates &rename make sprite
blocks = [water(5, 0), water(20, 3), water(68, 13), water(71, 13), water(71, 12), water(79, 8), water(95, 0), water(70, -2)]
ores=[diamondore,emeraldore,rubyore,coal,goldore]
#referance for newclass.py[stays after lists] DO NOT EDIT OR DELETE(2)
# bricks
classlist=[topsoil,water,dirt,stone,trunk,flower,leaf,diamondore,emeraldore,rubyore,coal,goldore]
brickslist = [deepbricks, blocks]
for bricktype in brickslist:
    for brick in bricktype:
        blocksdict[(brick.x, brick.y)] = brick
# makes deep ground
def makeblocks():
    for x,y in itertools.product(range(-1000, 1000), range(-30, -2)):
        if y > -10:
            blocksdict[(x,y)] = dirt(x,y)
        if -20 >= y >= -30:
            blocksdict[(x, y)] = lava(x, y)
        if -10>= y >=-20:
            if random(1, 100) == 1:
                blocksdict[(x, y)] = ores[random(0, len(ores) - 1)](x, y)
            else:
                blocksdict[(x, y)] = stone(x, y)
    for x in range(-1000,1000):
        blocksdict[(x, -2)] = topsoil(x, -2)
        if x % random(1, 70) == 0:
            if (x,-1)or(x,0) not in blocksdict:
                tree_height=random(1,10)
                for tree_y in range(tree_height):
                    blocksdict[x,tree_y-1]=trunk(x,tree_y-1)
                    if tree_height==tree_y+1:
                        blocksdict[x-1,tree_y]=leaf(x-1,tree_y)
                        blocksdict[x , tree_y] = leaf(x - 1, tree_y)
                        blocksdict[x + 1, tree_y] = leaf(x - 1, tree_y)
                        blocksdict[x, tree_y+1] = leaf(x, tree_y+1)
        if x % random(1,50) == 0:
            if (x,-1) not in blocksdict:
                blocksdict[x,-1]=flower(x,-1)
blocksdict[(-1, -1)] = cabbage(-1, -1)
#referance for newclass.py[stays between layer making functions and their calls] DO NOT EDIT OR DELETE(1)
makeblocks()
def round_to_cube_size(number):
    return cube_size*round(number/cube_size)
game_length=0
class level():
    def __init__(self, deepbricks, end, player, blocks, cat, creatures, dict):
        self.deepbricks = deepbricks
        self.end = end
        self.player = player
        self.exploFrame = 0
        self.blocks = blocks
        self.cat = cat
        self.creatures = [self.cat, self.player]
        self.dict = blocksdict

    # dont walk into blocks
    def anti_collide(self, _):
        for creature in level1.creatures:
            for coords, blok in blocksdict.items():
                if creature.x == blok.x and creature.y == blok.y:
                    creature.anti_collide()
                if creature.x+1 == blok.x and creature.y == blok.y and type(creature)==cat:
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
        self.cat.prev_x=self.cat.x
        self.cat.prev_y=self.cat.y
    def mine(self, direction):
        try:
            if direction == "down":
                del blocksdict[self.player.x, self.player.y - 1]
                inventory[topsoil] += 1
            if direction == "up":
                del blocksdict[self.player.x, self.player.y + 1]
                inventory[topsoil] += 1
            if direction == "right":
                del blocksdict[self.player.x + 1, self.player.y]
                inventory[topsoil] += 1
            if direction == "left":
                del blocksdict[self.player.x - 1, self.player.y]
        except KeyError:
            pass
    def add_to_inventory(self, blok):
        inventory[blok]+=1

    def place(self, direction):
        if inventory[topsoil] > 0:
            if direction == "down":
                blocksdict[(self.player.x, self.player.y - 1)] = topsoil(self.player.x, self.player.y - 1)
            if direction == "up":
                blocksdict[(self.player.x, self.player.y + 1)] = topsoil(self.player.x, self.player.y + 1)
            if direction == "left":
                blocksdict[(self.player.x + 1, self.player.y)] = topsoil(self.player.x + 1, self.player.y)
            if direction == "right":
                blocksdict[(self.player.x - 1, self.player.y)] = topsoil(self.player.x - 1, self.player.y)
            inventory[topsoil] -= 1
    # stay on blocks &condense int one for loop
    def creatureOnFloor(self, creature):
        for coords, blok in blocksdict.items():
            if creature.y == blok.y + 1 and creature.x == blok.x:
                return True
        return False
# summons level
level1 = level(
    deepbricks=deepbricks,
    end=endPoint(140, (200, 150, 5)),
    player=Player(),
    blocks=blocks,
    cat=cat(),
    creatures=[cat(), Player()],
    dict=blocksdict,
)
# size of everything do not chnage
cube_size = 32
batch=pyglet.graphics.Batch()
inventoryshown=False
fps=pyglet.window.FPSDisplay(window=game_window)
speed=1
game_speed=3
background=pyglet.image.load("./assets/images/night-test.png")
night=pyglet.shapes.Rectangle(0,0,1200,900,(0,0,0,0))
sun=pyglet.image.load("./assets/images/bookshelf.png")
sun_x=0
sun_y=0
background.width=game_window.width
background.height=game_window.height
game_window.set_mouse_visible(False)
mouse=pyglet.shapes.Rectangle(0,0,cube_size,cube_size,(255,255,255,100))
blok_in_hand_x = 0
blok_in_hand_y = 0
sun_falling = False
def sun_rise():
    global sun_x,sun_y,sun_falling
    if sun_y>8:
        sun_falling=True
    if sun_falling:
        sun_y-=1
    else:
        sun_y+=1
    sun_x+=1
cabbagegrowth=12
def update():
    global speed, blok_in_hand_x, blok_in_hand_y, blok_in_hand,sun_x,sun_y,game_length,cabbagegrowth
    if night.color[3]>100:
        background.blit(0,0)
    else:
        game_window.clear()
    if game_length>10:cabbagegrowth=13
    sun.blit(sun_x,sun_y)
    camera = 0
    images=[]
    sun_rise()
    night.color=(0,0,0,int(game_length/2))
    def loadimages():
        images.append(pyglet.image.load("./assets/images/topsoil.png"))
        images.append(pyglet.image.load("./assets/images/dirt.png"))
        images.append(pyglet.image.load("assets/images/leaf.png"))
        images.append(pyglet.image.load("./assets/images/water.png"))
        images.append(pyglet.image.load("./assets/images/trunk.png"))
        images.append(pyglet.image.load("./assets/images/stone.png"))
        images.append(pyglet.image.load("./assets/images/flower.png"))
        images.append(pyglet.image.load("assets/images/diamondore.png"))
        images.append(pyglet.image.load("./assets/images/rubyore.png"))
        images.append(pyglet.image.load("assets/images/emeraldore.png"))
        images.append(pyglet.image.load("assets/images/goldore.png"))
        images.append(pyglet.image.load("./assets/images/coal.png"))
        images.append(pyglet.image.load("./assets/images/cabbageplanted.png"))
        images.append(pyglet.image.load("./assets/images/cabbagegrown.png"))
    todraw=[]
    if len(fps.label.text)==4:
        if float(fps.label.text)<game_speed:
            speed+=1
        if float(fps.label.text)>game_speed and speed>0.1:
            speed-=1
    try:
        loadimages()
    except Exception as ex:
        print(str(ex)+" Download needed image from the images folder in Coding folder ")
        exit()
    if not inventoryshown:
        for screen_x,screen_y in (itertools.product(range(game_window.width // cube_size), range(game_window.height // cube_size))):
            blok_cord = (level1.player.x-15+screen_x,level1.player.y-5+screen_y)
            if (level1.cat.x,level1.cat.y) == blok_cord:
                pyglet.image.load("./assets/images/kitty2.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
            if blok_cord in blocksdict:
                blok=blocksdict[blok_cord]
            else:continue
            if type(blok) == topsoil:
                todraw.append(pyglet.sprite.Sprite(images[0], screen_x * cube_size, screen_y * cube_size, batch=batch))
                #pyglet.image.load("./assets/images/topsoil.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
            elif type(blok) == leaf:
                todraw.append(pyglet.sprite.Sprite(images[2], screen_x * cube_size, screen_y * cube_size, batch=batch))
                #pyglet.image.load("./assets/images/leaf.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
            elif type(blok) == water:
                todraw.append(pyglet.sprite.Sprite(images[3], screen_x * cube_size, screen_y * cube_size, batch=batch))

                #pyglet.image.load("./assets/images/water.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
            elif type(blok) == trunk:
                todraw.append(pyglet.sprite.Sprite(images[4], screen_x * cube_size, screen_y * cube_size, batch=batch))
                #pyglet.image.load("./assets/images/wheatplanted.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
            elif type(blok) == stone:
                todraw.append(pyglet.sprite.Sprite(images[5], screen_x * cube_size, screen_y * cube_size, batch=batch))
                #pyglet.image.load("./assets/images/stone.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
            elif type(blok) == lava:
                pyglet.shapes.Rectangle(screen_x * cube_size, screen_y * cube_size, cube_size, cube_size, blok.color).draw()
            elif type(blok) == dirt:
                todraw.append(pyglet.sprite.Sprite(images[1], screen_x * cube_size, screen_y * cube_size, batch=batch))
                #pyglet.image.load("./assets/images/dirt.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
            elif type(blok) == flower:
                todraw.append(pyglet.sprite.Sprite(images[6], screen_x * cube_size, screen_y * cube_size, batch=batch))
                #pyglet.image.load("./assets/images/dirt.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
            elif type(blok) == emeraldore:
                todraw.append(pyglet.sprite.Sprite(images[8], screen_x * cube_size, screen_y * cube_size, batch=batch))
            elif type(blok) == diamondore:
                todraw.append(pyglet.sprite.Sprite(images[7], screen_x * cube_size, screen_y * cube_size, batch=batch))
            elif type(blok) == rubyore:
                todraw.append(pyglet.sprite.Sprite(images[9], screen_x * cube_size, screen_y * cube_size, batch=batch))
            elif type(blok) == goldore:
                todraw.append(pyglet.sprite.Sprite(images[10], screen_x * cube_size, screen_y * cube_size, batch=batch))
            elif type(blok) == coal:
                todraw.append(pyglet.sprite.Sprite(images[11], screen_x * cube_size, screen_y * cube_size, batch=batch))
            elif type(blok) == cabbage:
                todraw.append(pyglet.sprite.Sprite(images[cabbagegrowth], screen_x * cube_size, screen_y * cube_size, batch=batch))
        batch.draw()
        #Draw the player
        pyglet.shapes.Rectangle(15 * cube_size, 5 * cube_size, cube_size,
                            cube_size).draw()
        fps.draw()
    if inventoryshown:
        y=0
        for (classname,x) in zip_longest(classlist,range(int(game_window.width/cube_size))):
            if classname is not None:
                pyglet.image.load("./assets/images/"+str(classname.__name__)+".png").blit(x * cube_size, y * cube_size)
                pyglet.text.Label(str(inventory[classname.__name__]),x=x*cube_size,y=y*cube_size).draw()
            if x>30:y+=1
            if blok_in_hand_x ==x and blok_in_hand_y==y:blok_in_hand= classname
        pyglet.shapes.Rectangle(blok_in_hand_x*cube_size,blok_in_hand_y*cube_size,cube_size,cube_size,(0,100,255,200)).draw()
    mouse.draw()
    night.draw()
    game_length=int(time.time())-int(game_start_time)
def on_key_press(space, _):
    global inventoryshown,blok_in_hand_y,blok_in_hand_x
    key = pyglet.window.key.symbol_string(space)
    level1.player.prev_x = level1.player.x
    level1.player.prev_y = level1.player.y
    if inventoryshown:
        if key=="RIGHT": blok_in_hand_x += 1
        if key=="LEFT": blok_in_hand_x -= 1
    if key == "UP":
        if level1.creatureOnFloor(level1.player):
            level1.player.jump()

    if key == "DOWN":
        if level1.creatureOnFloor(level1.player) == False:
            level1.player.fall()
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
        inventoryshown=True
    if key =="F":
        inventoryshown = False
def leftrightmarker(_):
    if keys[key.LEFT]:
        sleep(speed / 6)
        level1.player.prev_x = level1.player.x
        level1.player.prev_y = level1.player.y
        level1.player.x -= 1
        level1.anti_collide(_)
    if keys[key.RIGHT]:
        sleep(speed / 6)
        level1.player.prev_x = level1.player.x
        level1.player.prev_y = level1.player.y
        level1.player.x += 1
        level1.anti_collide(_)
@game_window.event
def on_mouse_motion(x,y,dx,dy):
    global mouse
    mouse = pyglet.shapes.Rectangle(round_to_cube_size(x), round_to_cube_size(y), cube_size, cube_size, (255, 255, 255, 100))
@game_window.event
def on_mouse_press(x,y,button,modifiers):
    adjusted_mouse_x = int(mouse.x / 32) - 15 + level1.player.x
    adjusted_mouse_y = int(mouse.y / 32) - 5 + level1.player.y
    if button == 1:
        if inventory[str(blok_in_hand.__name__)] > 0:
            blocksdict[adjusted_mouse_x, adjusted_mouse_y] = blok_in_hand(adjusted_mouse_x, adjusted_mouse_y)
            inventory[str(blok_in_hand.__name__)] -= 1
    if button == 4:
        try:
            print(type(blocksdict[adjusted_mouse_x, adjusted_mouse_y]).__name__)
            level1.add_to_inventory(type(blocksdict[adjusted_mouse_x, adjusted_mouse_y]).__name__)
            del blocksdict[adjusted_mouse_x, adjusted_mouse_y]
        except KeyError:
            pass
# run it nothing below here expect for run
game_window.on_draw = update
game_window.on_key_press = on_key_press
pyglet.clock.schedule_interval(leftrightmarker, 0.1)
pyglet.clock.schedule_interval(level1.one_second, 0.5)
pyglet.clock.schedule_interval(level1.anti_collide, 0.05)
pyglet.clock.schedule_interval(level1.movecat, 0.5)
pyglet.app.run()
