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
            self.y = self.y -3
    #gravity
    def fall(self):
        if self.gravity == "down":
            self.y = self.y - 1
        else:
            self.y = self.y+1



#topsoil &rename
class sawblade():
    def __init__(self, x, y):
        self.x = x
        self.y = y
#bricks useful &change to sprite
class block():
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
deepbricks=[sawblade(0, -1),sawblade(1, 0), sawblade(2, 0), sawblade(3, 0), sawblade(9, 0), sawblade(6, 0),sawblade(7, 0), sawblade(8, 0),sawblade(9, 0), sawblade(10, 0), sawblade(11, 0),sawblade(12, 0), sawblade(13, 0), sawblade(4, 0), sawblade(14, 0), sawblade(8, 0), sawblade(14, 6), sawblade(18, 0), sawblade(18, 3), sawblade(21, 2), sawblade(58, 13), sawblade(60, 13), sawblade(96, 0), sawblade(36, 2)]
#blocks cooridinates &rename make sprite
blocks = [block(5, 0), block(20, 3), block(68, 13), block(71, 13), block(71, 12), block(79, 8), block(95, 0)]
#bricks
brickslist=[deepbricks,blocks]
#makes deep ground
def MAKEDIRT():
    for ground in range(150):
       deepbricks.append(sawblade(ground,-2))
MAKEDIRT()
#makes all the stuff
class level():
    def __init__(self, deepbricks, end, player, blocks,cat,creatures):
        self.deepbricks = deepbricks
        self.end = end
        self.player = player
        self.exploFrame = 0
        self.blocks = blocks
        self.cat=cat
        self.creatures=[self.cat,self.player]
    def movecamera(self,direction,amount):
        if direction == "down":
            level1.player.y+=amount
            for block in self.blocks:
                block.y+=amount
            for block in self.deepbricks:
                block.y+=amount
        else:
            level1.player.y -= amount
            for block in self.blocks:
                block.y -= amount
            for block in self.deepbricks:
                block.y -= amount
    #dont walk into blacks
    def anti_collide(self,_):
        for creature in level1.creatures:
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
    def mine(self):
        for i in self.deepbricks:
            if i.y==self.player.y-1and i.x==self.player.x:
                #absuoltlty horrible fix
                i.y=1000
                print(i.y)
    def place(self):
        deepbricks.append(sawblade(self.player.x-1,self.player.y))
    def movecat(self,_):
        if self.cat.x<self.player.x-3:
             self.cat.x+=1
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
        pyglet.image.load("./assets/image1.png").blit(blade.x * cubeSize-camera, blade.y * cubeSize+10)
    for blok in level1.blocks:
        pyglet.shapes.Rectangle(blok.x * cubeSize-camera, blok.y * cubeSize + 10, cubeSize, cubeSize,
                                color=(1, 50, 100)).draw()
    pyglet.shapes.Rectangle(level1.end.x*cubeSize-camera, 0, cubeSize, game_window.height, color=level1.end.color).draw()

    #moving
def on_key_press(space, _):
    key = pyglet.window.key.symbol_string(space)
    if key == "UP":
        if level1.playerOnFloor(level1.player):
            level1.player.jump()
        if level1.player.y > 13:
            level1.player.y = 13
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
        level1.mine()
    if key=="L":
        level1.movecamera("up",1)
    if key=="P":
        level1.place()
    #& add minining
#run it nothing below here expect for run
game_window.on_draw = update
game_window.on_key_press = on_key_press
pyglet.clock.schedule_interval(level1.one_second, 0.5)
pyglet.clock.schedule_interval(level1.noinfinitefalling, 0.5)
pyglet.clock.schedule_interval(level1.anti_collide, 0.05)
pyglet.clock.schedule_interval(level1.movecat, 0.5)
# pyglet.app.run()





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