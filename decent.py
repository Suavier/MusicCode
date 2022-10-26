import turtle
import random
#setting up the building blocks
t = turtle.Turtle()
h = 100
n = -400
t.speed(speed=8)

#good ole staff line
t.pu()
t.goto(n,h)

for x in ['black', 'black', 'black', 'black', 'black']:
    t.pd()
    t.color(x)
    t.forward(n*-2)
    h = h - 40
    t.pu()
    t.goto(n,h)
    
r = 20
n = n + 40
color = ['black','black','black','black','black','black','black',
        'black','black','black']

for x in reversed(color):
    #list of notes to go through and their positioning
    Notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    k = len(Notes)
    f = random.randrange(k)
    h = f*20

    #determines which octave to write in
    Oct = ['High', 'Low']
    o = len(Oct)
    taves = random.randrange(o)


    if f in [3, 4, 5, 6]:
        if taves in [1]:
            h = h - 140
    if f in [0, 2]:
        if taves in [1]:
            h = h - 140
            t.goto(n - r*2, h + 40)
            t.pd()
            t.forward(r*4)
            t.pu()
            t.goto(n - r*2, h)
            t.pd()
            t.forward(r*4)

    if f in [1]:
        if taves in [1]:
            h = h - 140
            t.goto(n - r*2, h + r)
            t.pd()
            t.forward(r*4)
        
        #draws note head and pole thingy
        
    t.pu()
    if taves in [0]:
        t.goto(n, h-20)
        t.pd()
        t.circle(radius=r, extent=None, steps=None)
        t.pu()
        t.goto(n - r, h+r/2)
        h = h - 125
        t.pd()
        t.goto(n - r,h)
        t.pu()

    if taves in [1]:
        t.goto(n, h-20)
        t.pd()
        t.circle(radius=r, extent=None, steps=None)
        t.pu()
        t.goto(n + r, h+r/2)
        h = h + 125
        t.pd()
        t.goto(n + r,h)
        t.pu()

    n = n + 80

def loading():
    t.lt(90)
    t.lt(90)
    t.lt(90)
    t.lt(90)
    t.lt(90)

t.speed(speed=1)
t.goto(-400, -60)
t.pd()
for x in reversed(color):
    loading()
    loading()


t.forward(800)

for x in reversed(color):
    loading()
    loading()
