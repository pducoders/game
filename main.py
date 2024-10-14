import pyglet
#nothing other than import above here
#summons window
game_window = pyglet.window.Window(resizable=True, width=1200, height=300)
#your player &rename it later
class cube():
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



#&remove later
class jumpad():
    def __init__(self, color, x, y):
        if color == "yellow":
            self.launchHeight = 4
            self.color = (255, 254, 0)  # Yellow
        if color == "pink":
            self.launchHeight = 2
            self.color = (254, 93, 243)
        if color == "orange":
            self.launchHeight = 5
            self.color = (255, 94, 45)
        self.x = x
        self.y = y
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
#&remove
class Portal():
    def __init__(self, x,y):
        self.x = x
        self.y =y*20
#topsoil & rename
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
    def __init__(self, deepbricks, end, player, blocks):
        self.deepbricks = deepbricks
        self.end = end
        self.player = player
        self.exploFrame = 0
        self.blocks = blocks

    def movecamera(self,direction):
        if direction == "down":
            for block in self.blocks:
                block.y+=1
            for block in self.deepbricks:
                block.y+=1
        else:
            for block in self.blocks:
                block.y -= 1
            for block in self.deepbricks:
                block.y -= 1
    #dont walk into blacks
    def anti_collide(self,_):
        for i in level1.deepbricks:
            if self.player.x==i.x and self.player.y==i.y:
                self.player.x=i.x-1
        for i in level1.blocks:
            if self.player.x==i.x and self.player.y==i.y:
                self.player.x=i.x-1
    #moving stuff
    def one_second(self, _):
        if self.playerOnFloor() == False:
            self.player.fall()
    def mine(self):
        for i in self.deepbricks:
            if i.x==self.player.x-1 and i.y==self.player.y:
                i.delete()
    #stay on blocks &condense int one for loop
    def playerOnFloor(self):
        #dont fall through trees
        for blok in level1.blocks:
            if self.player.gravity == "down":
                if self.player.y == blok.y + 1 and self.player.x == blok.x:
                    return True
                if self.player.y == -1:
                    pass
            else:
                if self.player.y == blok.y-1 and self.player.x == blok.x:
                    return True
                if self.player.y == 13:
                    pass
        for brick in level1.deepbricks:
            if self.player.gravity == "down":
                if self.player.y == brick.y + 1 and self.player.x == brick.x:
                    return True
                if self.player.y == 0:
                    pass
            else:
                if self.player.y == brick.y-1 and self.player.x == brick.x:
                    return True
                if self.player.y == 13:
                    return True
        return False
#summons level
level1 = level(
deepbricks = deepbricks,
end = endPoint(140, (200, 150, 5)),
player = cube(),
blocks = blocks,
)
#size of everything do not chnage
cubeSize = 32
#runs te code
def update():
    game_window.clear()
    camera = level1.player.x*cubeSize-game_window.width/4
    #i dont even no what this all is summoning images mabyye
    pyglet.shapes.Rectangle(0,game_window.height-10, game_window.width, 10, color=(1, 60, 154)).draw()
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
        if level1.playerOnFloor():
            level1.player.jump()
        if level1.player.y > 13:
            level1.player.y = 13
    if key == "DOWN":
        if level1.playerOnFloor()==False:
            level1.player.fall()
    if key == "LEFT":
        level1.player.x -= 1
    if key == "RIGHT":
        level1.player.x += 1
    if key =="SLASH":
        level1.movecamera("down")
    if key=="PERIOD":
        level1.mine()
    #& add minining
#run it nothing below here expect for run
game_window.on_draw = update
game_window.on_key_press = on_key_press
pyglet.clock.schedule_interval(level1.one_second, 0.5)
pyglet.clock.schedule_interval(level1.anti_collide, 0.05)
pyglet.app.run()





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