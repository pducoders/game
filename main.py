import pyglet
import random
from pyglet.window import key
keys=key.KeyStateHandler()
piglet=pyglet.window.Window()
piglet.push_handlers(keys)
rectangle=pyglet.shapes.Rectangle(555,55,4,4,(2,56,43))
circle=pyglet.shapes.Circle(600,67,0,3,(255,255,255))
def on_draw():
    speed=1
    if random.randint(1,10)==1:

        rectangle.y+= 5
        rectangle.x-=5
    if keys[key.D]:

        rectangle.x=rectangle.x+5
        #circle.radius=circle.radius+speed
        speed+=1
    if keys[key.S]:
        rectangle.y = rectangle.y - 5
        #circle.radius = circle.radius + speed
        speed-=1
    if keys[key.A]:
        rectangle.x = rectangle.x - 5
        #circle.radius = circle.radius + speed
        speed+=1
    if keys[key.W]:
        rectangle.y = rectangle.y + 5
        #circle.radius = circle.radius + speed
        speed-=1

    #piglet.clear()
    rectangle.draw()
    circle.draw()

piglet.on_draw=on_draw
pyglet.app.run()

