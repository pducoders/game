main=open("./gdash.py","r")
print("Newclass.py has been deprecated on the latest update; do not use.")
raise Exception("Deprecated")
newfile=open("./new.py","w")
classname=input("Classname: ")
filename=input("Filename? ")
islayer=input("Is this a layer of blocks? (y/n) ")
if islayer=="y":
    blokymin=str(input("Farthest down block reaches(number)? "))
    blokymax=str(input("Farthest up block reaches(number)? "))
    funcfile = ["def make" + classname + "():\n",
                "    for x,y in itertools.product(range(-1000, 1000), range(" + blokymin + "," + blokymax + ")):\n",
                "       blocksdict[(x,y)] = " + classname + "(x,y)\n","make"+classname+"()\n","#referance for newclass.py[stays between layer making functions and their calls] DO NOT EDIT OR DELETE(1)\n"]
classfile=["class "+classname+"():\n","   def __init__(self,x,y):\n","      self.x=x\n","      self.y=y\n","blocksdict=dict()\n"]
indexedfile=[]
for line in main:
    indexedfile.append(line)
numimg=-1
brickslist=None
for line in indexedfile:
    if "(pyglet.image.load" in line and( "#" or "kitty") not in line:
        numimg+=1
    if "brickslist ="in line:
        brickslist=line
print(brickslist)
imagesfile = "        images.append(pyglet.image.load('./assets/images/" + filename + "'))\n    todraw=[]\n"
drawfile=["            elif type(blok) == "+classname+":\n","                todraw.append(pyglet.sprite.Sprite(images["+str((int(numimg)+1))+"], screen_x * cube_size, screen_y * cube_size, batch=batch))\n","        batch.draw()\n"]
listfile=[classname+"s = []\n",brickslist[0:(len(brickslist)-2)]+","+classname+"s]\n"]
for listline in range(len(listfile)):
    print(str(listfile[listline]))
for line in indexedfile:
    if "dict()" in line:
        for classline in range(4):
            newfile.write(str(classfile[classline]))
    if "todraw=[]" in line:
        newfile.write(str(imagesfile))
    if "DELETE(1)" in line and islayer=="y":
        for funcline in range(len(funcfile)):
            newfile.write(str(funcfile[funcline]))
    if "DELETE(2)" in line and islayer!="y":
        for listline in range(len(listfile)):
            newfile.write(str(listfile[listline]))
    if "brickslist =" in line and classname not in line and islayer!="y":
        continue
    if "batch.draw()" in line:
        for drawline in range(len(drawfile)):
            newfile.write(str(drawfile[drawline]))
    else:
        newfile.write(str(indexedfile[indexedfile.index(line)]))
