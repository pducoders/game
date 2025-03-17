import time
import pyglet
from pyglet.window import key
import itertools
from random import randint as random
from collections import Counter
from urllib.request import urlretrieve
import os
import pickle
level1exists=False
cube_size = 32
# nothing other than import above here
game_start_time=time.time()
# summons window
game_window = pyglet.window.Window(resizable=True, width=1200, height=300)
keys = key.KeyStateHandler()
game_window.push_handlers(keys)
dependencies=dict()
for image in os.listdir("./assets/images"):
    dependencies[image.split(".")[0]]="./assets/images/"+image
for k, v in dependencies.items():
    print(k,v)
def btos(sheepx, sheepy):
    if not level1exists:
        screenx = (sheepx - 5 + 15) * cube_size
        screeny = (sheepy - 2 + 5) * cube_size
    else:
        screenx=(sheepx-level1.player.x +15)*cube_size
        screeny=(sheepy-level1.player.y+5)*cube_size
    return screenx, screeny
images = dict()
for k,image in dependencies.items():
    images[k]=(pyglet.image.load(image))
# your player
class Player:
    def __init__(self):
        self.x = 5
        self.y = 2
        self.shape = "cube"
        self.gravity = "down"
        self.mine_speed=5
        self.blok_being_mined=(0,0)
        self.prev_x = 5
        self.prev_y = 2
        self.sprite=pyglet.sprite.Sprite(images["playerright"], 15*cube_size, 5*cube_size)

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


class sheep:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        x,y=btos(x,y)
        self.sprite = pyglet.sprite.Sprite(
            pyglet.image.load(dependencies["cabbagegrown"]),
            x, y,
        )
    def fall(self):
        self.sprite.x, self.sprite.y=btos(self.x, self.y)
        self.y=self.y-1
class block:
    def __init__(self,x,y,name):
        self.x=x
        self.y=y
        self.name=name
    def name(self):
        return self.name
blocksdict = dict()
inventory = Counter()
blok_in_hand="topsoil"
sheeps=[sheep(1,1)]
for sheepx,sheepy in itertools.product(range(-1000,1000),range(-1,5)):
    if random(1,700)==1:
        sheeps.append(sheep(sheepx,sheepy))
# blocks cooridinates &rename make sprite
ores=["diamondore","emeraldore","rubyore","coal","goldore"]
coins=0
# bricks
brickslist = []
for bricktype in brickslist:
    for brick in bricktype:
        blocksdict[(brick.x, brick.y)] = brick
ashleep=False

def export_world():
    file=open("./game.pickle","wb")
    pickle.dump(blocksdict,file)
    inventoryfile = open("./save.inventory", "w")
    inventoryfile.write(f"{inventory}")
def import_world():
    global blocksdict
    file=open("./game.pickle","rb")
    blocksdict=pickle.load(file)
    global inventory
    inventoryfile =open("./save.inventory","r")
    read=inventoryfile.read()
    if "Counter" not in read:
        print("Invalid inventory file")
        return
    inventory=eval(read)
def makeblocks():
    for x,y in itertools.product(range(-1000, 1000), range(-30, -2)):
        if y > -10:
            blocksdict[(x,y)] = block(x,y,"dirt")
        if -20 >= y >= -30:
            blocksdict[(x, y)] = block(x, y,"laava")
        if -10>= y >=-20:
            if random(1, 100) == 1:
                blocksdict[(x, y)] =block(x, y, ores[random(0, len(ores) - 1)])
            else:
                blocksdict[(x, y)] = block(x, y,"stone")
    for x in range(-1000,1000):
        blocksdict[(x, -2)] = block(x, -2,"topsoil")
        if x % random(1, 70) == 0:
            if (x,-1)or(x,0) not in blocksdict:
                tree_height=random(1,10)
                for tree_y in range(tree_height):
                    blocksdict[x,tree_y-1]=block(x,tree_y-1,"trunk")
                    if tree_height==tree_y+1:
                        blocksdict[x-1,tree_y]=block(x-1,tree_y,"leaf")
                        blocksdict[x , tree_y] = block(x - 1, tree_y,"leaf")
                        blocksdict[x + 1, tree_y] = block(x - 1, tree_y,"leaf")
                        blocksdict[x, tree_y+1] = block(x, tree_y+1,"leaf")
        if x % random(1,50) == 0:
            if (x,-1) not in blocksdict:
                blocksdict[x,-1]=block(x,-1,"flower")
makeblocks()
def round_to_cube_size(number):
    return cube_size*round(number/cube_size)
game_length=0
def mine(mine_mouse_x, mine_mouse_y):
    if level1.mine_frame>=level1.player.mine_speed:
        mine_mouse_x,mine_mouse_y=level1.player.blok_being_mined
        try:
            print(blocksdict[mine_mouse_x, mine_mouse_y].name)
            inventory[blocksdict[mine_mouse_x, mine_mouse_y].name] += 1
            blocksdict.pop((mine_mouse_x, mine_mouse_y))
        except KeyError:
            pass
        level1.mine_frame=0
        level1.player.blok_being_mined=None
    else:
        if level1.mine_frame==0:
            level1.player.blok_being_mined=(mine_mouse_x,mine_mouse_y)
        level1.mine_frame+=1
def place(place_mouse_x, place_mouse_y):
    try:
        blocksdict[place_mouse_x, place_mouse_y]
    except:
        if inventory[str(blok_in_hand)] > 0:
            if blok_in_hand=="sheepegg":
                level1.creatures.append(sheep(place_mouse_x,place_mouse_y))
            else:
                blocksdict[place_mouse_x, place_mouse_y] = block(place_mouse_x, place_mouse_y,blok_in_hand)
            inventory[str(blok_in_hand)] -= 1
    else:
        if type(blocksdict[place_mouse_x, place_mouse_y]) == sheep:
            level1.go_to_shleep(place_mouse_x, place_mouse_y)
class level():
    def __init__(self,  player, cat, creatures, dict):
        self.player = player
        self.mine_frame = 0
        self.cat = cat
        self.creatures = [self.cat, self.player] + creatures
        self.dict = blocksdict

    # dont walk into blocks
    def anti_collide(self, _):
        for creature in level1.creatures:
            if (creature.x, creature.y) in blocksdict:
                if blocksdict[(creature.x,creature.y)].name !="trunk":
                    if type(creature) != sheep:
                        creature.anti_collide()

    # moving stuff
    def one_second(self, _):
        for creature in self.creatures:
            if self.creatureOnFloor(creature) == False:
                creature.fall()
    def movesheep(self,_):
        sheeplist=[]
        for creature in self.creatures:
            if type(creature)==sheep:
                sheeplist.append(creature)
        for this_sheep in sheeplist:
            if random(1,20)==1:
                this_sheep.y+=3
                continue
            if random(1,200)==1:
                blocksdict[this_sheep.x+1,this_sheep.y]=block(this_sheep.x+1,this_sheep.y,"sheepegg")
            distance = random(-2, 2)
            for i in range(distance):
                if (this_sheep.x+distance-i,this_sheep.y) not in blocksdict:
                    this_sheep.x += distance
                else:
                    distance-=1
                    continue
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
                inventory["topsoil"] += 1
            if direction == "up":
                del blocksdict[self.player.x, self.player.y + 1]
                inventory["topsoil"] += 1
            if direction == "right":
                del blocksdict[self.player.x + 1, self.player.y]
                inventory["topsoil"] += 1
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
        return
    # stay on blocks &condense int one for loop
    def creatureOnFloor(self, creature):
        if type(creature)==tuple:
            if (creature[0], creature[1]-1) in blocksdict:
                return True
        else:
            if (creature.x, creature.y-1) in blocksdict:
                    return True
        return False
# summons level
level1 = level(
    player=Player(),
    cat=cat(),
    creatures=[cat(), Player()] + sheeps,
    dict=blocksdict,
)
level1exists=True
# size of everything do not chnage
batch=pyglet.graphics.Batch()
inventoryshown=False
turbo_mode=False
fps=pyglet.window.FPSDisplay(window=game_window)
speed=1
game_speed=3
try:
    background=pyglet.sprite.Sprite(pyglet.image.load("./assets/images/night-test.png"),0,0)
    background.scale=3
except:
    urlretrieve("https://drive.google.com/uc?export=download&id=1KvmPuDHo26Fqx1uk6FqabqjX7FBqyA7z", "./assets/images/night-test.png")
    print("downloaded night please restart program")
    exit()
night=pyglet.shapes.Rectangle(0,0,1200,900,(0,0,0,0))
sun=pyglet.image.load("./assets/images/bookshelf.png")
sun_x=0
sun_y=0
game_window.set_mouse_cursor(game_window.get_system_mouse_cursor(game_window.CURSOR_CROSSHAIR))
#mouse=pyglet.shapes.Rectangle(0,0,cube_size,cube_size,(255,255,255,100))
blok_in_hand_x = 0
blok_in_hand_y = 0
sun_falling = False
shleep_length=0
def sun_rise():
    global sun_x, sun_y, sun_falling
    if sun_y > 8:
        sun_falling=True
    if sun_falling:
        sun_y -= 1
    else:
        sun_y += 1
    sun_x += 1
cabbagegrowth=12
cats=[]
shleep_morning=False
drawdict=dict()
for x,y in itertools.product(range(game_window.width // cube_size), range(game_window.height // cube_size)):
    drawdict[x,y]="y"
mine_animation=pyglet.shapes.Rectangle(0,0,32,32,(255,255,255,0))
def update():
    global speed, blok_in_hand_x, blok_in_hand_y, blok_in_hand,sun_x,sun_y,game_length,cabbagegrowth,shleep_length,shleep_morning,dependencies
    if turbo_mode:
        leftrightmarker("")
        level1.anti_collide("")
    fps.label.opacity=255
    if level1.mine_frame>0:
        x,y=level1.player.blok_being_mined
        mine(x,y)
        if level1.mine_frame>1:
            mine_animation.x,mine_animation.y=level1.player.blok_being_mined
            mine_animation.x*=cube_size
            mine_animation.y*=cube_size
        mine_animation.color=(255,255,255,level1.mine_frame*6)
        mine_animation.draw()
    if fps.label.text=='':fps.label.text="1000"
    if float(fps.label.text)>5:
        fps.label.color=(39,105,3)
    elif float(fps.label.text)>3:
        fps.label.color=(245,228,33)
    else:
        fps.label.color=(105,27,3)
    if night.color[3]>100:
        background.draw()
    else:
        game_window.clear()
    if game_length>10:cabbagegrowth=13
    sun.blit(sun_x,sun_y)
    camera = 0
    sun_rise()
    if ashleep:
        night.color = (0, 0, 0, int(shleep_length *12))
    else:
        night.color=(0,0,0,int(game_length))
    todraw=[]
    if len(fps.label.text)==4:
        if float(fps.label.text)<game_speed:
            speed+=1
        if float(fps.label.text)>game_speed and speed>0.1:
            speed -= 1

    if not inventoryshown:
        for drawsheep in level1.creatures:
            if type(drawsheep)==sheep:
                if  level1.player.x-15<=drawsheep.x<=level1.player.x+ game_window.width/cube_size-15:
                    #drawsheep.sprite.x, drawsheep.sprite.y = btos(drawsheep.x, drawsheep.y)
                    screen_x, screen_y = btos(drawsheep.x, drawsheep.y)
                    images["cabbagegrown"].blit(screen_x, screen_y)

        for screen_x,screen_y in (itertools.product(range(game_window.width // cube_size), range(game_window.height // cube_size))):
            blok_cord = (level1.player.x-15+screen_x,level1.player.y-5+screen_y)
            if (level1.cat.x,level1.cat.y) == blok_cord:
                images["kitty2"].blit(screen_x*cube_size, screen_y*cube_size)
            if blok_cord in blocksdict:
                blok=blocksdict[blok_cord]
            else:continue
            try:
                images[blok.name].blit(screen_x * cube_size, screen_y * cube_size)
            except:pass

        fps.draw()

        #Draw the player
        level1.player.sprite.draw()
        night.draw()
    if inventoryshown:
        game_window.clear()
        inventorys=[]
        for k,v in zip(images.keys(),images.values()):
            inventorys.append((k,v))
        i=0
        for y in range(2):
            for x in range(int(game_window.width/cube_size)):
                try:
                    blockname,image=inventorys[i]
                except:pass
                if image is not None:
                    #if inventory[blockname]>0:
                    if x>game_window.width/cube_size:
                        x=0
                    if image.width != cube_size or image.height != cube_size:
                        spritevar = pyglet.sprite.Sprite(image, x*cube_size, y*cube_size)
                        spritevar.scale=.5
                        spritevar.draw()
                    else:
                        image.blit(x*cube_size,y*cube_size)
                    pyglet.text.Label(str(inventory[blockname]),x=x*cube_size,y=y*cube_size).draw()
                if blok_in_hand_x ==x and blok_in_hand_y==y:blok_in_hand= blockname
                i+=1
        pyglet.shapes.Rectangle(blok_in_hand_x*cube_size,blok_in_hand_y*cube_size,cube_size,cube_size,(0,100,255,200)).draw()
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
    global inventoryshown,blok_in_hand_y,blok_in_hand_x,coins,costs,inventory,turbo_mode
    key = pyglet.window.key.symbol_string(space)
    level1.player.prev_x = level1.player.x
    level1.player.prev_y = level1.player.y
    if inventoryshown:
        if key=="RIGHT": blok_in_hand_x += 1
        if key=="LEFT": blok_in_hand_x -= 1
        if key=="TAB":export_world()
        if key=="BACKSPACE":import_world()
        if key=="T":
            if turbo_mode:
                turbo_mode=False
            else:
                turbo_mode=True
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
        if inventoryshown:
            inventoryshown=False
        else:
            inventoryshown=True
    if key=="Z":
        mine(level1.player.x + 1, level1.player.y+1)
        mine(level1.player.x+1,level1.player.y)
def leftrightmarker(_):
    if keys[key.LEFT]:
        level1.player.prev_x = level1.player.x
        level1.player.prev_y = level1.player.y
        level1.player.x -= 1
        level1.anti_collide(_)
        level1.player.sprite.image = images["playerleft"]
    if keys[key.RIGHT]:
        level1.player.prev_x = level1.player.x
        level1.player.prev_y = level1.player.y
        level1.player.x += 1
        level1.anti_collide(_)
        level1.player.sprite.image = images["playerright"]
@game_window.event
def on_mouse_press(x,y,button,modifiers):
    adjusted_mouse_x = int(x / 32) - 15 + level1.player.x
    adjusted_mouse_y = int(y / 32) - 5 + level1.player.y
    if button == 1:
        place(adjusted_mouse_x, adjusted_mouse_y)
    if button == 4:
        mine(adjusted_mouse_x, adjusted_mouse_y)
# run it nothing below here expect for run
game_window.on_draw = update
game_window.on_key_press = on_key_press
if not turbo_mode:
    pyglet.clock.schedule_interval(leftrightmarker, 0.1)
    pyglet.clock.schedule_interval(level1.anti_collide, 0.05)
pyglet.clock.schedule_interval(level1.one_second, 0.5)
pyglet.clock.schedule_interval(level1.movecat, 0.2)
pyglet.clock.schedule_interval(level1.movesheep, 0.5)
pyglet.app.run()
