import pyglet
#nothing other than import above here
#summons window
game_window = pyglet.window.Window(resizable=True, width=1200, height=300)
#your player &rename it later
class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.shape = "cube"
        self.gravity = "down"
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
class cat():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.gravity = "down"
    #jump
    def jump(self):
        if self.gravity == "down":
            self.y = self.y + 3
        else:
            self.y = self.y - 3
    #gravity
    def fall(self):
        if self.gravity == "down":
            self.y = self.y - 1
        else:
            self.y = self.y+1



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
#topsoil & rename
deepbrickbatch=pyglet.graphics.Batch()
deepbricks=[topsoil(0, -1), topsoil(1, 0), topsoil(2, 0), topsoil(3, 0), topsoil(9, 0), topsoil(6, 0), topsoil(7, 0), topsoil(8, 0), topsoil(9, 0), topsoil(10, 0), topsoil(11, 0), topsoil(12, 0), topsoil(13, 0), topsoil(4, 0), topsoil(14, 0), topsoil(8, 0), topsoil(14, 6), topsoil(18, 0), topsoil(18, 3), topsoil(21, 2), topsoil(58, 13), topsoil(60, 13), topsoil(96, 0), topsoil(36, 2)]
#blocks cooridinates &rename make sprite
blocks = [block(5, 0), block(20, 3), block(68, 13), block(71, 13), block(71, 12), block(79, 8), block(95, 0)]
trunks=[trunk(50, 0), trunk(50, -1), trunk(30, 0), trunk(30, -1), trunk(67, 0), trunk(67, -1), trunk(22, 0), trunk(22, -1), trunk(74, 0), trunk(74, -1), trunk(43, 0), trunk(43, -1), trunk(100, -1), trunk(100, 0), trunk(89, -1), trunk(89, 0), trunk(123, -1), trunk(123, 0), trunk(97, -1), trunk(97, -1), trunk(107, 0), trunk(107, -1), trunk(114, 0), trunk(114, -1), trunk(130, 0), trunk(130, -1)]
#bricks
brickslist=[deepbricks,blocks,trunks]

#makes deep ground
def MAKEDIRT():
    for ground in range(150):
       deepbricks.append(topsoil(ground, -2))
MAKEDIRT()
#makes all the stuff
class level():
    def __init__(self, deepbricks, end, player, blocks,cat,creatures,trunks):
        self.deepbricks = deepbricks
        self.end = end
        self.player = player
        self.exploFrame = 0
        self.blocks = blocks
        self.cat=cat
        self.creatures=[self.cat,self.player]
        self.trunks=trunks
    def movecamera(self,direction,amount):
        if direction == "down":
            level1.player.y+=amount
            for block in self.blocks:
                block.y+=amount
            for block in self.deepbricks:
                block.y+=amount
            for block in self.trunks:
                block.y+=amount
        else:
            level1.player.y -= amount
            for block in self.blocks:
                block.y -= amount
            for block in self.deepbricks:
                block.y -= amount
            for block in self.trunks:
                block.y-=amount
    #dont walk into blacks
    def anti_collide(self,_):
        for creature in level1.creatures:
            for i in level1.trunks:
                if creature.x==i.x and creature.y==i.y:
                    creature.x=i.x-1
                    if "cat" in str(creature): creature.jump()
            for i in level1.deepbricks:
                if creature.x==i.x and creature.y==i.y:
                    creature.x=i.x-1
                    if "cat" in str(creature): creature.jump()
            for i in level1.blocks:
                if creature.x==i.x and creature.y==i.y:
                    creature.x=i.x-1
                    if "cat" in str(creature): creature.jump()

    #moving stuff
    def one_second(self, _):
        for creature in self.creatures:
            if self.playerOnFloor(creature) == False:
                creature.fall()
    def movecat(self,_):
        if self.cat.x<self.player.x-3:
            self.cat.x+=1
        if self.cat.x>self.player.x-3:
            self.cat.x-=1
    def mine(self,direction):
        for i in self.deepbricks:
            if direction == "down":
                if i.y==self.player.y-1 and i.x==self.player.x:
                    #absuoltlty horrible fix
                    i.y=1000
            if direction == "up":
                if i.y==self.player.y+1 and i.x==self.player.x:
                    #absuoltlty horrible fix
                    i.y=1000
            if direction == "left":
                if i.y==self.player.y and i.x==self.player.x-1:
                    #absuoltlty horrible fix
                    i.y=1000
            if direction == "right":
                if i.y==self.player.y and i.x==self.player.x+1:
                    #absuoltlty horrible fix
                    i.y=1000

    def placeLeft(self):
        if self.playerOnFloor(level1.player)==True:
            deepbricks.append(topsoil(self.player.x-1,self.player.y))

    def placeRight(self):
        if self.playerOnFloor(level1.player)==True:
            deepbricks.append(topsoil(self.player.x + 1, self.player.y))

    def placeUp(self):
        if self.playerOnFloor(level1.player)==True:
            deepbricks.append(topsoil(self.player.x, self.player.y + 1))

    def placeDown(self):
        if self.playerOnFloor(level1.player)==True:
            deepbricks.append(topsoil(self.player.x, self.player.y - 1))

    #stay on blocks &condense int one for loop
    def playerOnFloor(self,creature):

        for blok in level1.blocks:
            if creature.y == blok.y + 1 and creature.x == blok.x:

                return True

            if creature.y == -1:
                pass
        for brick in level1.deepbricks:

            if creature.y == brick.y + 1 and creature.x == brick.x:
                return True
            if creature.y == -1:
                pass

        return False
    def auto_downscroll(self):
        self.movecamera("down" , level1.player.y*-1+2)
    def noinfinitefalling(self,_):
        for creature in self.creatures:
            if deepbricks[0].y==3 or creature.y==-2:
                creature.y=3
                creature.x+=1
#summons level
level1 = level(
deepbricks = deepbricks,
end = endPoint(140, (200, 150, 5)),
player = Player(),
blocks = blocks,
cat=cat(),
creatures=[cat(),Player()],
trunks=trunks,
)
#size of everything do not chnage
cubeSize = 32
def update():
    game_window.clear()
    level1.auto_downscroll()
    camera = level1.player.x*cubeSize-game_window.width/4
    #defines images uses colin magic

    pyglet.shapes.Rectangle(level1.cat.x * cubeSize - camera, level1.cat.y * cubeSize + 10, cubeSize,
                            cubeSize,(0,255,100)).draw()
    pyglet.shapes.Rectangle(level1.player.x * cubeSize-camera, level1.player.y * cubeSize + 10, cubeSize, cubeSize).draw()
    for blade in level1.deepbricks:
        pyglet.image.load("././game-main/assets/image1.png").blit(blade.x * cubeSize-camera, blade.y * cubeSize+10)
    for blok in level1.blocks:
        pyglet.shapes.Rectangle(blok.x * cubeSize-camera, blok.y * cubeSize + 10, cubeSize, cubeSize,
                                color=(1, 50, 100)).draw()
    pyglet.shapes.Rectangle(level1.end.x*cubeSize-camera, 0, cubeSize, game_window.height, color=level1.end.color).draw()

    for log in level1.trunks:
        pyglet.image.load("././game-main/assets/image6.png").blit(log.x * cubeSize-camera, log.y * cubeSize+10)

    #moving
def on_key_press(space, _):
    key = pyglet.window.key.symbol_string(space)
    if key == "UP":
        if level1.playerOnFloor(level1.player):
            level1.player.jump()

    if key == "DOWN":
        if level1.playerOnFloor(level1.player)==False:
            level1.player.fall()
    if key == "LEFT":
        level1.player.x -= 1
    if key == "RIGHT":
        level1.player.x += 1
    if key =="SLASH":
        level1.movecamera("down",1)
    if key=="PERIOD":
        level1.mine("down")
    if key=="L":
        level1.movecamera("up",1)
    if key=="P":
        level1.placeRight()
    if key=="U":
        level1.placeLeft()
    if key=="I":
        level1.placeDown()
    if key=="O":
        level1.placeUp()
    if key=="W":
        level1.mine("up")
    if key=="D":
        level1.mine("right")
    if key=="A":
        level1.mine("left")
    if key=="S":
        level1.mine("down")
    #& add minining
#run it nothing below here expect for run
game_window.on_draw = update
game_window.on_key_press = on_key_press
pyglet.clock.schedule_interval(level1.one_second, 0.5)
pyglet.clock.schedule_interval(level1.noinfinitefalling, 0.5)
pyglet.clock.schedule_interval(level1.anti_collide, 0.05)
pyglet.clock.schedule_interval(level1.movecat, 0.5)
pyglet.app.run()





#]:~—~Names~—~:[#
#dont mess with stuff on other peoples line !! so dont use control z ever
# also if you want to type gibberish type in here not in the code
#{&~~:AVNI("Yellow"):~~&}#<[$(@^💾^*~|~*^💻^*~|~*^💿^*~|~*^⌨^*~|~*^🖱^@)$]>
#rosa :3:3:3 idk how to do python r.i.p. me ig & $$$$$$
#ayda
#sylvia|〜(￣▽￣〜)
#colin ,}{...}[oter]/\?:"fnf"%%*,90+?&&&&@><^><#$$||}}}^^?27;;::''''>>><<<)("<">"!\\/:$?&?%?@?!?*?^?***K-boi.^**!2>>&https//.^:;;'}{#>+@**>?"=%^_-_-_-_-69_-_-_-_@$//?;+!*^><][^^-_$;L-bruh??#>>{=}$--+--"B"@&<?>*Boi*%<//'"
#ridge | (づ￣ u￣)づ
#finley
