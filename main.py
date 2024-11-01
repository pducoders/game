import pyglet
from pyglet.window import key
#nothing other than import above here
#summons window
game_window = pyglet.window.Window(resizable=True, width=1200, height=300)
keys=key.KeyStateHandler()
game_window.push_handlers(keys)
#your player &rename it later
class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.shape = "cube"
        self.gravity = "down"
        self.prev_x = 0
        self.prev_y = 0
    #jump
    def jump(self):
        if self.gravity == "down":
            self.y +=1
            level1.anti_collide(None)
            self.y += 1
            level1.anti_collide(None)
            self.y += 1
            level1.anti_collide(None)
        else:
            self.y-=1
            level1.anti_collide(None)
            self.y -= 1
            level1.anti_collide(None)
            self.y -= 1
            level1.anti_collide(None)
    #gravity
    def fall(self):
        if self.gravity == "down":
            self.y = self.y - 1
        else:
            self.y = self.y+1
    #anti-collide which is called when the player is in a block
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
    #jump
    def jump(self):
        if self.gravity == "down":
            self.y = self.y + 3
        else:
            self.y = self.y -3
    #gravity
    def fall(self):
        if self.gravity == "down":
            self.y = self.y - 1
        else:
            self.y = self.y+1
    #anti-collide
    def anti_collide(self):
        self.jump()



#topsoil &rename
class topsoil():
    def __init__(self, x, y):
        self.x = x
        self.y = y
#bricks useful &change to sprite
class block():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class trunk():
    def __init__(self, x, y):
        self.x = x
        self.y = y
#&remove
class endPoint():
    def __init__(self, x, color):
        self.x = x
        self.color = color
blocksdict=dict()
deepbrickbatch=pyglet.graphics.Batch()
deepbricks=[topsoil(0, -1), topsoil(1, 0), topsoil(2, 0), topsoil(3, 0), topsoil(9, 0), topsoil(6, 0), topsoil(7, 0), topsoil(8, 0), topsoil(9, 0), topsoil(10, 0), topsoil(11, 0), topsoil(12, 0), topsoil(13, 0), topsoil(4, 0), topsoil(14, 0), topsoil(8, 0), topsoil(14, 6), topsoil(18, 0), topsoil(18, 3), topsoil(21, 2), topsoil(58, 13), topsoil(60, 13), topsoil(96, 0), topsoil(36, 2)]
#blocks cooridinates &rename make sprite
blocks = [block(5, 0), block(20, 3), block(68, 13), block(71, 13), block(71, 12), block(79, 8), block(95, 0)]
trunks=[trunk(50, 0), trunk(50, -1), trunk(30, 0), trunk(30, -1), trunk(67, 0), trunk(67, -1), trunk(22, 0), trunk(22, -1), trunk(74, 0), trunk(74, -1), trunk(43, 0), trunk(43, -1), trunk(100, -1), trunk(100, 0), trunk(89, -1), trunk(89, 0), trunk(123, -1), trunk(123, 0), trunk(97, -1), trunk(97, -1), trunk(107, 0), trunk(107, -1), trunk(114, 0), trunk(114, -1), trunk(130, 0), trunk(130, -1)]
#bricks
brickslist=[deepbricks,blocks,trunks]
for bricktype in brickslist:
    for brick in bricktype:
        blocksdict[(brick.x,brick.y)]=brick
#makes deep ground
def MAKEDIRT():
    for ground in range(150):
       blocksdict[(ground,-2)]=topsoil(ground,-2)
MAKEDIRT()
#makes all the stuff
class level():
    def __init__(self, deepbricks, end, player, blocks,cat,creatures,trunks,dict):
        self.deepbricks = deepbricks
        self.end = end
        self.player = player
        self.exploFrame = 0
        self.blocks = blocks
        self.cat=cat
        self.creatures=[self.cat,self.player]
        self.trunks=trunks
        self.dict=blocksdict
    def movecamera(self,direction,amount):
        for coords,blok in blocksdict.items():
            if direction == "down":
                blok.y+=amount
            else:
                blok.y-=amount
        if direction=="down":
            self.player.y+=amount
        else:
            self.player.y-=amount
    #dont walk into blocks
    def anti_collide(self,_):
        for creature in level1.creatures:
            for coords,blok in blocksdict.items():
                
                if creature.x == blok.x and creature.y == blok.y:
                    creature.anti_collide()
    #moving stuff
    def one_second(self, _):
        for creature in self.creatures:
            if self.creatureOnFloor(creature) == False:
                creature.fall()
    def movecat(self,_):
        if self.cat.x<self.player.x-3:
            self.cat.x+=1
        if self.cat.x>self.player.x-3:
            self.cat.x-=1
    def mine(self,direction):
        for coords, blok in blocksdict.items():
            if direction == "down":
                if blok.y == self.player.y - 1 and blok.x == self.player.x:
                    blok.y=100
            if direction == "up":
                if blok.y == self.player.y + 1 and blok.x == self.player.x:
                    blok.y=100
            if direction == "right":
                if blok.y == self.player.y and blok.x == self.player.x+1:
                    blok.y=100
            if direction == "left":
                if blok.y == self.player.y and blok.x == self.player.x-1:
                    blok.y=100
    def place(self,direction):
        for coords,blok in blocksdict.items():
            if direction=="down":
                blocksdict[(self.player.x,self.player.y-1)]=topsoil(self.player.x,self.player.y-1)
            if direction=="up":
                blocksdict[(self.player.x,self.player.y+1)]=topsoil(self.player.x,self.player.y+1)
            if direction=="left":
                blocksdict[(self.player.x+1,self.player.y)]=topsoil(self.player.x+1,self.player.y)
            if direction=="right":
                blocksdict[(self.player.x-1,self.player.y)]=topsoil(self.player.x-1,self.player.y)
    #stay on blocks &condense int one for loop
    def creatureOnFloor(self, creature):
        for coords,blok in blocksdict.items():
            if creature.y == blok.y + 1 and creature.x == blok.x:
                return True
        return False
    def auto_downscroll(self):
        self.movecamera("down" , level1.player.y*-1+3)
#summons level
level1 = level(
deepbricks = deepbricks,
end = endPoint(140, (200, 150, 5)),
player = Player(),
blocks = blocks,
cat=cat(),
creatures=[cat(),Player()],
trunks=trunks,
dict=blocksdict,
)
#size of everything do not chnage
cubeSize = 32
def update():
    game_window.clear()
    level1.auto_downscroll()
    camera = level1.player.x*cubeSize-game_window.width/4
    #defines images uses colin magic
    pyglet.image.load("./assets/kitty2.png").blit(level1.cat.x * cubeSize - camera, level1.cat.y * cubeSize + 10)
    pyglet.image.load("./assets/draftforcharecter.png").blit(level1.player.x * cubeSize - camera,
                                                             level1.player.y * cubeSize + 10)
    for coords,blok in blocksdict.items():
        if type(blok)== topsoil:
            pyglet.image.load("./assets/image1.png").blit(blok.x * cubeSize - camera, blok.y * cubeSize + 10)
        elif type(blok) == block:
            pyglet.image.load("./assets/image8.png").blit(blok.x * cubeSize - camera, blok.y * cubeSize + 10)
        elif type(blok)== trunk:
            pyglet.image.load("./assets/image6.png").blit(blok.x * cubeSize - camera, blok.y * cubeSize + 10)
def on_key_press(space, _):
    key = pyglet.window.key.symbol_string(space)
    level1.player.prev_x = level1.player.x
    level1.player.prev_y = level1.player.y
    if key == "UP":
        if level1.creatureOnFloor(level1.player):
            level1.player.jump()

    if key == "DOWN":
        if level1.creatureOnFloor(level1.player)==False:
            level1.player.fall()
    if key =="SLASH":
        level1.movecamera("down",1)
    if key=="PERIOD":
        level1.mine("down")
    if key=="L":
        level1.movecamera("up",1)
    if key=="P":
        level1.place("right")
    if key=="U":
        level1.place("left")
    if key=="I":
        level1.place("down")
    if key=="O":
        level1.place("up")
    if key=="W":
        level1.mine("up")
    if key=="D":
        level1.mine("right")
    if key=="A":
        level1.mine("left")
    if key=="S":
        level1.mine("down")
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
#run it nothing below here expect for run
game_window.on_draw = update
game_window.on_key_press = on_key_press
pyglet.clock.schedule_interval(leftrightmarker, 0.1)
pyglet.clock.schedule_interval(level1.one_second, 0.5)
pyglet.clock.schedule_interval(level1.anti_collide, 0.05)
pyglet.clock.schedule_interval(level1.movecat, 0.5)
pyglet.app.run()
