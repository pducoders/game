from itertools import zip_longest
from time import sleep
import time
import pyglet
from pyglet.window import key
import itertools
from random import randint as random
from collections import Counter
from urllib.request import urlretrieve
import os.path
# nothing other than import above here
game_start_time=time.time()
# summons window
game_window = pyglet.window.Window(resizable=True, width=1200, height=300)
keys = key.KeyStateHandler()
game_window.push_handlers(keys)
dependencies=[
    ("pyglet.image.load(","./assets/images/topsoil.png","1_snTnZDZOAphu23GtlGHc8crIWGvWZwn")
        ,("pyglet.image.load(","./assets/images/dirt.png","1l-LFTTHy2jrx51ZXVOi2ZLo6zrmFN96u")
        ,("pyglet.image.load(","./assets/images/leaf.png","1P6IQW7-mMSsk1YmR4n-Yopl5uZw2IcnE")
        ,("pyglet.image.load(","./assets/images/water.png","1IyEV0FXw_qHcNpiGsECuiEfXLQ-zWmBU")
        ,("pyglet.image.load(","./assets/images/trunk.png","1eP3XVuvL68GSB1ZtzeNe35UDlvRLl00z")
        ,("pyglet.image.load(","./assets/images/stone.png","1_PdchorIC0sAG7EjTPM5X10Kwhu6YApy")
        ,("pyglet.image.load(","./assets/images/flower.png","1_snTnZDZOAphu23GtlGHc8crIWGvWZwn")
        ,("pyglet.image.load(","./assets/images/diamondore.png","1_xDSW7clXE59bftjW_kaslX7y3ytb8LP")
        ,("pyglet.image.load(","./assets/images/rubyore.png","1V_mgKUg5kAct90oODaw4ZpQQ_O10LAmg")
        ,("pyglet.image.load(","./assets/images/emeraldore.png","1VT_cmTjwgSGobsL8sL17Mev4ythDnAJ4")
        ,("pyglet.image.load(","./assets/images/goldore.png","1JNOnxYXEf2rNEkPI3_1SrbroOck8Mh0d")
        ,("pyglet.image.load(","./assets/images/coal.png","1WVTEwMeaMdcKBlg0mKH601UQHahNJFhW")
        ,("pyglet.image.load(","./assets/images/cabbageplanted.png","1qPeKoihXoAHo7iSysp6Umx2w8JujHElk")
        ,("pyglet.image.load(","./assets/images/cabbagegrown.png","1JJjtsjKAXY8OyrQcMNvlTLHCoT941MPh")
        ,("pyglet.image.load(","./assets/images/cabbagegrown.png","1JJjtsjKAXY8OyrQcMNvlTLHCoT941MPh")
        ,("pyglet.image.load(","./assets/images/sheepegg.png","1-Z1cnrr8IvKxncA_0O5H7fYUxiD1yaz2")
]
for file in dependencies:
    if not os.path.exists(file[1]):
        urlretrieve("https://drive.google.com/uc?export=download&id="+file[2],file[1])
# your player
class Player:
    def __init__(self):
        self.x = 5
        self.y = 2
        self.shape = "cube"
        self.gravity = "down"
        self.prev_x = 4
        self.prev_y = 2

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
class sheep:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class sheepegg:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class sheepmilk:
    def __init__(self,x,y):
        self.x=x
        self.y=y
blocksdict = dict()
inventory = Counter()
blok_in_hand=topsoil
sheeps=[sheep(1,1)]
for x,y in itertools.product(range(-1000,1000),range(-1,5)):
    if random(1,200)==1:
        sheeps.append(sheep(x,y))
deepbricks = [topsoil(16, 2), topsoil(0, -1), topsoil(1, 0), topsoil(2, 0), topsoil(3, 0), topsoil(9, 0), topsoil(6, 0), topsoil(7, 0),
              topsoil(8, 0), topsoil(9, 0), topsoil(10, 0), topsoil(11, 0), topsoil(12, 0), topsoil(13, 0),
              topsoil(4, 0), topsoil(14, 0), topsoil(8, 0), topsoil(14, 6), topsoil(18, 0), topsoil(18, 3),
              topsoil(21, 2), topsoil(58, 13), topsoil(60, 13), topsoil(96, 0), topsoil(36, 2)]
# blocks cooridinates &rename make sprite
blocks = [water(5, 0), water(20, 3), water(68, 13), water(71, 13), water(71, 12), water(79, 8), water(95, 0), water(70, -2)]
ores=[diamondore,emeraldore,rubyore,coal,goldore]
#referance for newclass.py[stays after lists] DO NOT EDIT OR DELETE(2)
# bricks
classlist=[topsoil,water,dirt,stone,trunk,flower,leaf,diamondore,emeraldore,rubyore,coal,goldore,sheepegg]
brickslist = [deepbricks, blocks,sheeps]
for bricktype in brickslist:
    for brick in bricktype:
        blocksdict[(brick.x, brick.y)] = brick
ashleep=False
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
                if type(creature)==Player and creature.x == blok.x  and (creature.y == blok.y or creature.y+1==blok.y):
                    creature.anti_collide()
                if creature.x == blok.x and creature.y == blok.y:
                    creature.anti_collide()
                if creature.x+1 == blok.x and creature.y == blok.y and type(creature)==cat:
                    creature.anti_collide()

    # moving stuff
    def one_second(self, _):
        for creature in self.creatures:
            if self.creatureOnFloor(creature) == False:
                creature.fall()
    def movesheep(self,_):
        def deletesheep(coords):
            if type(blocksdict[coords])==sheep:
                del blocksdict[coords]
        sheeplist=[]
        for coords,blok in blocksdict.items():
            if type(blok)==sheep:
                sheeplist.append(coords)
        for coords in sheeplist:
            sheepexists=True
            try:
                blocksdict[coords]
            except KeyError:sheepexists=False
            if not sheepexists:continue
            if random(1,20)==1:
                deletesheep(coords)
                blocksdict[(coords[0], coords[1] + 3)] = sheep(coords[0], coords[1] + 3)
                continue
            if not self.creatureOnFloor(coords):
                deletesheep(coords)
                blocksdict[(coords[0], coords[1]-1)] = sheep(coords[0], coords[1]-1)
                continue
            distance = random(-2, 2)
            deletesheep(coords)
            blocksdict[(coords[0] - distance, coords[1])] = sheep(coords[0] - distance, coords[1])
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
    def go_to_shleep(self, sheep_x, sheep_y):
        self.player.x=sheep_x
        self.player.y=sheep_y
        global ashleep
        ashleep=True
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
        if type(creature)==tuple:
            for coords,blok in blocksdict.items():
                if creature[1]==blok.y+1 and creature[0]==blok.x:
                    return True
        else:
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
try:
    background=pyglet.image.load("./assets/images/night-test.png")
except:
    urlretrieve("https://drive.google.com/uc?export=download&id=1KvmPuDHo26Fqx1uk6FqabqjX7FBqyA7z", "./assets/images/night-test.png")
    print("downloaded night please restart program")
    exit()
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
shleep_length=0
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
cats=[]
shleep_morning=False
drawdict=dict()
for x,y in itertools.product(range(game_window.width // cube_size), range(game_window.height // cube_size)):
    drawdict[x,y]="y"
def update():
    global speed, blok_in_hand_x, blok_in_hand_y, blok_in_hand,sun_x,sun_y,game_length,cabbagegrowth,shleep_length,shleep_morning,dependencies
    if night.color[3]>100:
        background.blit(0,0)
    else:
        game_window.clear()
    if game_length>10:cabbagegrowth=13
    sun.blit(sun_x,sun_y)
    camera = 0
    images=[]
    sun_rise()
    if ashleep:
        night.color = (0, 0, 0, int(shleep_length *12))
    else:
        night.color=(0,0,0,int(game_length/2))
    def loadimages():
        for image in dependencies:
            images.append(pyglet.image.load(image[1]))
    todraw=[]
    if len(fps.label.text)==4:
        if float(fps.label.text)<game_speed:
            speed+=1
        if float(fps.label.text)>game_speed and speed>0.1:
            speed-=1

    loadimages()
    if not inventoryshown:
        for screen_x,screen_y in (itertools.product(range(game_window.width // cube_size), range(game_window.height // cube_size))):
            blok_cord = (level1.player.x-15+screen_x,level1.player.y-5+screen_y)
            if (level1.cat.x,level1.cat.y) == blok_cord:
                pyglet.image.load("./assets/images/kitty.2.png").blit(screen_x * cube_size - camera, screen_y * cube_size)
            if blok_cord in blocksdict:
                blok=blocksdict[blok_cord]
            else:continue
            if type(blok) == topsoil:
                bloktype=0
            elif type(blok) == leaf:
                bloktype=2
            elif type(blok) == water:
                bloktype=3
            elif type(blok) == trunk:
                bloktype=4
            elif type(blok) == stone:
                bloktype=5
            elif type(blok) == lava:
                pyglet.shapes.Rectangle(screen_x * cube_size, screen_y * cube_size, cube_size, cube_size, blok.color).draw()
            elif type(blok) == dirt:
                bloktype=1
            elif type(blok) == flower:
                bloktype=6
            elif type(blok) == emeraldore:
                bloktype=8
            elif type(blok) == diamondore:
                bloktype=7
            elif type(blok) == rubyore:
                bloktype=9
            elif type(blok) == goldore:
                bloktype=10
            elif type(blok) == coal:
                bloktype=11
            elif type(blok) == cabbage:
                todraw.append(pyglet.sprite.Sprite(images[cabbagegrowth], screen_x * cube_size, screen_y * cube_size, batch=batch))
            elif type(blok)==sheep:
                bloktype=14
            elif type(blok)==sheepegg:
                bloktype=15
            for k, v in drawdict.items():
                coord = (level1.player.x - 15 + k[0], level1.player.y - 5 + k[1])
                if coord[0] == blok.x and coord[1] == blok.y and v == "y":
                    try:
                        images[bloktype].blit(screen_x * cube_size, screen_y * cube_size)
                    except UnboundLocalError as error: print(str(error)+"Huh, figure out why it errors")
        fps.draw()
        #Draw the player
        pyglet.sprite.Sprite(pyglet.image.load("./assets/images/draftforcharecter.png"),15*cube_size,5*cube_size).draw()
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
    if ashleep:
        if shleep_length<240/12 and shleep_morning==False:
            shleep_length=int(time.time())-int(game_start_time)
        else:
            shleep_morning=True
        if shleep_morning:
            print(game_length-shleep_length)
            shleep_length=int(time.time())-int(game_start_time)
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
    if key=="Z":level1.go_to_shleep(1,1)
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
        try:blocksdict[adjusted_mouse_x, adjusted_mouse_y]
        except:
            if inventory[str(blok_in_hand.__name__)] > 0:
                blocksdict[adjusted_mouse_x, adjusted_mouse_y] = blok_in_hand(adjusted_mouse_x, adjusted_mouse_y)
                inventory[str(blok_in_hand.__name__)] -= 1
        else:
            if type(blocksdict[adjusted_mouse_x, adjusted_mouse_y])==sheep:
                level1.go_to_shleep(adjusted_mouse_x, adjusted_mouse_y)
    if button == 4:
        try:
            print(type(blocksdict[adjusted_mouse_x, adjusted_mouse_y]).__name__)
            if type(blocksdict[adjusted_mouse_x, adjusted_mouse_y])==sheep:
                level1.add_to_inventory("sheepegg")
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
pyglet.clock.schedule_interval(level1.movesheep, 0.5)
pyglet.app.run()
