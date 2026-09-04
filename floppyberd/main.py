import turtle
import time
import keyboard
import random

while True:
    upd = 0
    piperate = 75 #out of every update, theres 1/x chance a pipe spawns
    pipespeed = 10
    ups = 45 #UPDATES PER SECOND

    pls = [(600, 40, 150)] #pipe list

    live = True
    birdcol = (255,0,0)
    txt = turtle.Pen()
    txt.speed(0)
    txt.pu()
    txt.hideturtle()
    txt.goto(0,200)
    t = turtle.Pen()
    t.pu()
    bird = turtle.Pen()
    bird.hideturtle()
    bird.pu()
    bird.speed(0)
    pipe = turtle.Pen()
    pipe.hideturtle()
    pipe.pu()
    pipe.speed(0)
    pipew = 40
    birdsize = 20
    t.hideturtle()
    t.speed(0)
    w = turtle.Screen()
    w.tracer(0)
    w.setup(500,500)
    w.colormode(255)
    w.bgcolor(0, 255, 250)
    pipe.color(0,255,0)
    g = -9.87/50
    ta = 0
    tai = 0
    tv = 0
    tp = 0
    
    txt.color(255,0,0)
    jump_time = time.time()
    c_time = time.time()
    btf_time = 0

    hold_check = False


    def jump():
        if live:
            global jump_time
            global tai
            global ta
            global tv
            global tp
            jump_time = time.time()
            if tv < 0:
                tv = 0
            ta = 0
            tai = -g*15


    def drawBird(y):
        bird.setheading(t.heading())
        bird.clear()
        bird.goto(bird.xcor(), y)
        bird.right(30)
        bird.backward(birdsize)
        bird.color(birdcol)
        for i in range(3):
            for x in range(birdsize):
                bird.forward(1)
                bird.dot(3)
                if i == 0 and (x == 7 or x == 8 or x == 9):
                    if live:
                        bird.color(0,0,0)
                    bird.dot(6)
                    bird.color(birdcol)
            if i == 0:
                bird.color(255,165,0)
                bird.dot(6)
                bird.color(birdcol)
            bird.right(120)
        bird.forward(birdsize)
        #bird.dot(10)
        ##print()


    def drawPipe(x,h,d):
        pipe.pu()
        pipe.goto(x,h)
        pipe.left(90)
        pipe.forward(d/2)
        pipe.left(90)
        pipe.forward(pipew/2)
        pipe.right(180)
        #pipe.pd()
        pipe.begin_fill()
        pipe.color(0,0,0)
        pipe.pd()
        for i in range(4):
            pipe.forward(pipew + ((i%2 == 1) * pipew * 10))
            pipe.left(90)
        pipe.pu()
        pipe.color(0,255,0)
        pipe.end_fill()

        pipe.goto(x,h)
        pipe.right(90)
        pipe.forward(d/2)
        pipe.left(90)
        pipe.forward(pipew/2)
        pipe.right(180)
        #pipe.pd()
        pipe.begin_fill()
        pipe.color(0,0,0)
        pipe.pd()
        for i in range(4):
            pipe.forward(pipew + ((i%2 == 1) * pipew * 10))
            pipe.left(90)
        pipe.pu()
        pipe.color(0,255,0)
        pipe.end_fill()

    def handlePipe():
        #draw pipes
        pipe.clear()
        global pls
        outls = []
        for pipes in pls:
            x, h, d = pipes
            if x >= -500:
                x = x - pipespeed
                drawPipe(x,h,d)
                outls.append((x,h,d))
            if live and len(pls)!= 0:
                if x - (pipew/2) < 0 and x + (pipew/2) > 0:
                    if t.ycor() > h + (d/2) or t.ycor() < h - (d/2):
                        #print(f'hit at {t.ycor(), {h + (d/2)}, {h - (d/2)}}')
                        killBird()
        pls = outls 

    def killBird():
        global live
        global tv
        global birdcol
        live = False
        tv = 10
        for i in range(255 - 50):
            w.bgcolor(0,255 - i,255 - i)
            #time.sleep((1/ups)/100)

    #drawPipe(0,0,150)
    while True:
        if live:
            upd += 1
        score = (f'{upd/ups:.0f}')
        txt.clear()
        txt.write(score, False, 'center', ("arial", 16, "bold"))
        #kill bird if hit border
        if abs(t.ycor()) >= 250 and live:
            
            killBird()

        #pipe spawn
        if random.randint(0,piperate) == 1:
            pls.append((300 * random.randint(2,5), random.randint(-100, 100), random.randint(75, 300)))
            #print('pipe spawned')
        drawBird(t.ycor())
        handlePipe()

        tv = tv + (ta)
        ta = (g) + tai
        tp += tv

        #rotate bird
        if tv < 50 and tv > -50:
            t.setheading(max(-90, min((tv/50) * 180, 45)))

        t.goto(0,tp)

        if tai >= 0:
            tai -= 1 
        elif tai < 0:
            tai = 0

        if (keyboard.is_pressed('space')):
            if (hold_check == False):
                #print('space')
                jump()
                hold_check = True
        else:
            hold_check = False

        btf_time = c_time - jump_time

        c_time = time.time()
        w.update()
        time.sleep(1/ups)
        if btf_time > 10:
            #print('dead')
            turtle.clear()
            w.clear()
            break
            